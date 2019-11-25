import subprocess
import pathlib
import os
import argparse
import tempfile
from skimage.metrics import mean_squared_error, structural_similarity
from skimage.io import imread
from skimage import color
import numpy as np
from dtxmp import xmp


def execute_darktable_cli(input_img, output_img, conf, xmpfn=None):
    dt_cli = ['darktable-cli', str(input_img)]
    if xmpfn is not None:
        dt_cli.append(str(xmpfn))
    dt_cli.extend([str(output_img), '--width', '2000', '--height', '2000'])

    dt_cli.extend(['--core'])
    if conf:
        dt_cli.append('--conf')
        for i, arg in enumerate(conf):
            if i % 2 == 1:
                dt_cli.append('--conf')
            dt_cli.append(arg)

    rv = subprocess.run(dt_cli, capture_output=True)
    return rv


def read_dt_conf(fn):
    """Read override conf parameters from a file

    Arguments:
        fn (str): filename
    Returns:
        (list)
    """
    conf = []
    with open(fn, 'r') as cfg:
        for L in map(str.strip, cfg):
            if L.lower().startswith('opencl='):
                # ignore opencl setting
                continue
            conf.append(L)
    return conf

def measure_cpu_gpu(input_image, xmp_file, output_image, conf_opts=None, keep_outputs=False):
    if conf_opts is not None:
        dt_conf = read_dt_conf(conf_opts)
    else:
        dt_conf = []

    output_image = pathlib.Path(output_image)

    # Execute with CPU
    dt_conf_cpu = ['opencl=false', 'plugins/imageio/storage/disk/overwrite=1']
    cpu_output = output_image.with_suffix('.cpu.tif')
    cpu_rv = execute_darktable_cli(input_image, cpu_output, dt_conf + dt_conf_cpu, xmpfn=xmp_file)

    # Execute with GPU
    dt_conf_gpu = ['opencl=true', 'plugins/imageio/storage/disk/overwrite=1']
    gpu_output = output_image.with_suffix('.gpu.tif')
    gpu_rv = execute_darktable_cli(input_image, gpu_output, dt_conf + dt_conf_gpu, xmpfn=xmp_file)

    if cpu_rv.returncode > 0:
        print("CPU exited with error")
        print(cpu_rv)
        return
    if gpu_rv.returncode > 0:
        print("GPU exited with error")
        print(gpu_rv)
        return

    rmse = compare_images(cpu_output, gpu_output)
    if not keep_outputs:
        cpu_output.unlink()
        gpu_output.unlink()

    return rmse

def main(args):
    rmse, ne = measure_cpu_gpu(args.input_image, args.xmp, args.output_prefix, conf_opts=args.conf, keep_outputs=args.keep)

    if rmse > args.threshold:
        print("threshold exceeeded.  Walking edit history")
        if args.xmp is None:
            iimg = pathlib.Path(args.input_image)
            document = xmp.parse_document(str(iimg.with_suffix('.nef.xmp')))
        else:
            document = xmp.parse_document(args.xmp)

        xmphistory = tuple(xmp.get_dt_history(document))
        for i in range(len(xmphistory)):
            contents = xmp.define_history_list(document, xmphistory[:i+1])
            # create temporary xmp file
            fd, tmp_xmp = tempfile.mkstemp('.xmp')
            tmp = os.fdopen(fd, mode='wb')
            tmp.write(xmp.tostring(contents))
            tmp.flush()
            tmp.close()
            rmse, ne = measure_cpu_gpu(args.input_image, tmp_xmp, args.output_prefix, conf_opts=args.conf)
            print(f"{args.input_image}: {rmse} {ne} (edit {i})")
            os.unlink(tmp_xmp)
    else:
        print(f"{args.input_image}: {rmse} {ne}")


def compare_images(img1, img2):
    i1 = imread(img1)
    i2 = imread(img2)
    rmse = mean_squared_error(i1, i2) ** .5
    n = np.count_nonzero(~np.isclose(i1, i2))
    return rmse, n/i1.size

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument('--conf', default=None, help="Path to darktablerc configuration")
    args_parser.add_argument('--xmp', default=None, help='Apply an existing xmp to input image')
    args_parser.add_argument('--keep', action='store_true', default=False, help="Keep output images")
    args_parser.add_argument('--threshold', type=float, default=1.0, help="RMSE threshold.")
    args_parser.add_argument('input_image', type=str, help='Image to test with')
    args_parser.add_argument('output_prefix', type=str, help='Image output location')

    pargs = args_parser.parse_args()
    # if input_image is a directory, process all RAW in directory
    iimg = pathlib.Path(pargs.input_image)
    if iimg.is_dir():
        for img in iimg.glob('*.nef'):
            pargs.input_image = img
            main(pargs)
    else:
        main(pargs)