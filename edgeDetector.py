import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.ndimage.filters import convolve
from skimage.filters import threshold_mean

Gx_filter = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
Gy_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
laplace_filter = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
laplace_filter_diag = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

filename = 'D:\\upResNet\\temp\\training\\test.jpg'

plt.gray()
img = Image.open(filename).convert('L')
img_gauss = gaussian_filter(img, sigma=1.4)

imgx = convolve(img_gauss, Gx_filter)
imgy = convolve(img_gauss, Gy_filter)
imgL = convolve(img_gauss, laplace_filter)
imgLd = convolve(img_gauss, laplace_filter_diag)
imgxy = np.add(imgx, imgy)

def get_threshold(img):
    return img > 225 #threshold_mean(img)

imgx_thresh = get_threshold(imgx)
imgy_thresh = get_threshold(imgy)
imgL_thresh = get_threshold(imgL)
imgLd_thresh = get_threshold(imgLd)
imgxy_thresh = get_threshold(imgxy)

def display_all():
    fig,ax = plt.subplots(2,5,sharex=True,sharey=True)
    ax[0,0].imshow(imgx, aspect="auto")
    ax[0,0].set_title("Gx")
    ax[1,0].imshow(imgx_thresh, aspect="auto")
    ax[0,1].imshow(imgy, aspect="auto")
    ax[0,1].set_title("Gy")
    ax[1,1].imshow(imgy_thresh, aspect="auto")
    ax[0,2].imshow(imgxy, aspect="auto")
    ax[0,2].set_title("Gx + Gy")
    ax[1,2].imshow(imgxy_thresh, aspect="auto")
    ax[0,3].imshow(imgL, aspect="auto")
    ax[0,3].set_title("Laplace")
    ax[1,3].imshow(imgL_thresh, aspect="auto")
    ax[0,4].imshow(imgLd, aspect="auto")
    ax[0,4].set_title("Laplace with diagonals")
    ax[1,4].imshow(imgLd_thresh, aspect="auto")
    plt.show()

display_all()