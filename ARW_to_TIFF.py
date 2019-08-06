import rawpy
import imageio
import argparse


def main():
    # file_path = "TCB02521.ARW"
    file_path = parse_the_file_path()
    arw_to_hdf5(file_path)


def arw_to_hdf5(file_path):

    with rawpy.imread(file_path) as raw:
        rgb = raw.postprocess(gamma=(1, 1), no_auto_bright=True, output_bps=16)
    print(rgb.shape)

    output_file_path = file_path.split('.')[0]
    output_file_path = output_file_path + ".tiff"

    imageio.imsave(output_file_path, rgb)


def parse_the_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="enter the file path")
    args = parser.parse_args()
    return args.file_path


if __name__ == '__main__':
    main()
