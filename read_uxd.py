import numpy as np
def read_uxd(file_name):
    '''Function to extract the angles and intensities from a uxd file'''
    with open(file_name, "r") as infile:
        cleaned = np.zeros(2)
        for line in infile:
            if not line.startswith(";"):
                if not line.startswith("_"):
                    if line.strip():
                        a, b = line.split()
                        cleaned = np.column_stack((cleaned,np.array([float(a), float(b)])))
    return np.delete(cleaned,0,1).T
