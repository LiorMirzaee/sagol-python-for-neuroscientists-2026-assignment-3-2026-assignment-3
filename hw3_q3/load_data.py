
import numpy as np

def load_data(fname: str):
    """ Load and return an '.npy' file """
    return np.load(fname)

def find_in_range(data: np.ndarray, num_range: tuple=(0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    mask = (data > num_range[0]) & (data < num_range[1])
    return data[mask]

def first_after_val(data: np.ndarray, val: float=0.9) -> np.ndarray:
    """ Return the position of the first value larger than val """
    index = np.argwhere(data> val)
    return index[0]