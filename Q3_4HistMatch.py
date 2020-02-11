import cv2
import numpy as np

def find_nearest_above(ref, actual):
    diff = ref - actual
    mask = np.ma.less_equal(diff, -1)
    # We need to mask the negative differences
    # since we are looking for values above
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c # returns min index of the nearest if target is greater than any value
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()
def hist_match(original, specified):

    oldshape = original.shape
    original = original.ravel() #converts matrix to 1d array
    specified = specified.ravel()

    # get the set of unique pixel values and their corresponding indices and counts
    original_values, bin_idx, original_counts = np.unique(original, return_inverse=True,return_counts=True)
    ref_values, ref_counts = np.unique(specified, return_counts=True)

    # Calculate s_k for original image
    original_quantiles = np.cumsum(original_counts).astype(np.float64)
    original_quantiles /=original_quantiles[-1]
    
    # Calculate s_k for specified image
    ref_quantiles = np.cumsum(ref_counts).astype(np.float64)
    ref_quantiles /=ref_quantiles[-1]
    

    # Round the values
    original_temp = np.around(original_quantiles*255)
    ref_temp = np.around(ref_quantiles*255)
    
    # Map the rounded values
    b=[]
    for data in original_temp[:]:
        b.append(find_nearest_above(ref_temp,data))
    b= np.array(b,dtype='uint8')

    return b[bin_idx].reshape(oldshape)

# Load the images in greyscale
original = cv2.imread('pout-dark.jpg',0)
specified = cv2.imread('pout-bright.jpg',0)

# perform Histogram Matching
a = hist_match(original, specified)

# Display the image
cv2.imshow('MatchedImage',np.array(a,dtype='uint8'))
cv2.imshow('Original-PoutBright',original)
cv2.imshow('Specified-PoutDark',specified)
cv2.waitKey(0)  
cv2.destroyAllWindows()