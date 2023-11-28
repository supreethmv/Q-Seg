import numpy as np

def decode_binary_string(x, height, width):
    """
    Decode a binary string into a binary segmentation mask.

    Parameters:
    x (list): Binary string representing the segmentation.
    height (int): Height of the image.
    width (int): Width of the image.

    Returns:
    numpy.ndarray: Segmentation mask.
    """
    mask = np.zeros([height, width])
    for index, segment in enumerate(x):
        mask[index // width, index % width] = segment
    return mask
