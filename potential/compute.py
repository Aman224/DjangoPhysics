from numpy import exp, cos, linspace
import os, time, glob

def compute(m,h):
    """Return filename of plot of the damped_vibration function."""
    e=9.8*float(m*h)
    return e
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1))