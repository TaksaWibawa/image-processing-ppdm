from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, entropy

def img_to_pixels(img_path):
    return io.imread(img_path)


def get_colour_histogram(img_pixels):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(img_pixels.ravel(), bins=255, color='red', alpha=0.7, rwidth=0.85)
    ax.set_title('Colour Histogram', fontweight='bold', fontsize=16)
    ax.set_xlabel('Colour Distribution')
    ax.set_ylabel('Count')
    return fig


def first_order_statistics(img):
    mean = np.mean(img)
    variance = np.var(img)
    skewness = skew(np.reshape(img, (48 * 48)))
    kurtos = kurtosis(np.reshape(img, (48 * 48)))
    entrope = entropy(np.reshape(img, (48 * 48)))
    return mean, variance, skewness, kurtos, entrope
