from skimage import io
from matplotlib.pyplot import imshow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, entropy
from skimage.feature import graycomatrix, graycoprops
import matplotlib.ticker as ticker

def compute_glcm(img, angles):
    glcm = graycomatrix(img, distances=[1], angles=angles, levels=256, symmetric=True, normed=True)
    return glcm


def glcm(img, metric_texture):
    matrix = []
    for i in metric_texture:
        row = []
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        for j in angles:
            row.append(graycoprops(compute_glcm(img, [j]), prop=i)[0][0])
        matrix.append(row)
    return matrix

def get_texture_histogram(glcm_matrix, metric_texture):
    fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(15, 6))
    fig.subplots_adjust(hspace=0.4)
    fig.suptitle('Texture Histogram', fontweight='bold', fontsize=16)
    ax = ax.ravel()
    for i, a in enumerate(ax):
        a.hist(glcm_matrix[i], bins=255, color='red', alpha=0.7, rwidth=0.85)
        a.set_title(metric_texture[i])
        a.grid()
        formatter = ticker.ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-2, 3))
        a.xaxis.set_major_formatter(formatter)
    return fig