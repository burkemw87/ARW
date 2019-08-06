import h5py
import numpy as np
from PIL import Image
import argparse


def main():
    # file_path = "TCB02521.hdf"
    file_path = parse_the_file_path()
    stretch_percentage = 2
    hdf5_to_JPG(file_path, stretch_percentage)


def hdf5_to_JPG(file_path, stretch_percentage):
    h5f_file = h5py.File(file_path, "r")
    red_array = h5f_file["Red"][()]
    green_array = h5f_file["Green"][()]
    blue_array = h5f_file["Blue"][()]

    red_array = get_the_scale(red_array, stretch_percentage)
    green_array = get_the_scale(green_array, stretch_percentage)
    blue_array = get_the_scale(blue_array, stretch_percentage)

    stacked_array = np.dstack((red_array, green_array, blue_array))
    stacked_array = np.uint8(stacked_array)
    im = Image.fromarray(stacked_array)

    file_path = file_path.split('.')[0] + '.jpg'
    im.save(file_path, "JPEG")


def get_the_scale(array, stretch_percentage):
    pmin = np.percentile(array, 0 + stretch_percentage)
    pmax = np.percentile(array, 100 - stretch_percentage)
    array[array > pmax] = pmax
    array[array < pmin] = pmin
    array = ((array - pmin) / (pmax - pmin)) * 255
    return array


def parse_the_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="enter the file path")
    args = parser.parse_args()
    return args.file_path


if __name__ == '__main__':
    main()
