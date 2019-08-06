# ARW
Handling ARW files in python

Several python libraries will be needed before any of these will run:
h5py
rawpy
numpy
argparse
imageio
PIL
matplotlib

example usage:
In a terminal enter the following:python "ARW_to_HDF5.py" "file/path/to/file.ARW"
for example:python "ARW_to_HDF5.py" "TCB02521.ARW"

ARW_to_HDF5.py - will convert an input ARW file into a HDF5 file while maintining all raw data values
ARW_to_TIFF.py - will convert an input ARW file into a TIFF file while maintining all raw data values

HDF5_viewer.py - allows you to view the histograms and a preview image from an HDF5 file, has a stretch_percentage parameter in the main() function that can be modified as desired (see*). While the HDF5 file maintians the true raw sensor values, the image preview is scaled between 0 and 255.

HDF5_to_JPG.py - allows you to convert an input HDF5 file into a JPG file, has a stretch_percentage parameter in the main() function that can be modified as desired (see*).

(*) A linear percent stretch allows you to trim extreme values from both ends of the histogram using a specified percentage. For example, assume that the pixel values in an image range from 164 to 1908. If you select a 2% linear stretch, the lowest 2% of histogram values are less than 179 and the highest 2% are greater than 698. Values less than 179 are set to 0, and values greater than 698 are set to 255. Values in between are distributed from 0 to 255.
