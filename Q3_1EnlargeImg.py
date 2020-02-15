import numpy as np
#from scipy.misc import imread, imshow
from scipy import ndimage
import cv2
 
def GetBilinearPixel(imArr, posX, posY):
	out = []
 
	#Get integer and fractional parts of numbers
	Xi = int(posX) 
	Yi = int(posY)
	Xf = posX - Xi
	Yf = posY - Yi
	Xi_n = min(Xi+1,imArr.shape[1]-1)
	Yi_n = min(Yi+1,imArr.shape[0]-1)
 
	#Get pixels in four corners
	for channel in range(imArr.shape[2]):
		bl = imArr[Yi, Xi, channel]
		br = imArr[Yi, Xi_n, channel]
		tl = imArr[Yi_n, Xi, channel]
		tr = imArr[Yi_n, Xi_n, channel]
 
		#Calculate interpolation
		b = Xf * br + (1. - Xf) * bl
		t = Xf * tr + (1. - Xf) * tl
		pxf = Yf * t + (1. - Yf) * b
		out.append(int(pxf))
 
	return out
 
if __name__=="__main__":
 
	im = cv2.imread("lena.png")
	window_name = 'Original image'
	cv2.imshow(window_name,im)
	cv2.waitKey()
	cv2.destroyAllWindows()
	print(im.shape)


	enlargedShape1 = list(map(int, [im.shape[0]*0.5, im.shape[1]*0.5, im.shape[2]])) #im.shape[2] = 3 for RGB
	enlargedShape2 = list(map(int, [im.shape[0]*1, im.shape[1]*1, im.shape[2]]))
	enlargedShape3 = list(map(int, [im.shape[0]*2, im.shape[1]*2, im.shape[2]]))
 
	window_name2="Enlarged image - 0.5"
	window_name3="Enlarged image - 1"
	window_name4="Enlarged image - 2"
	window_name5="Inbuilt fun - 0.5"
	window_name6="Inbuilt fun - 1"
	window_name7="Inbuilt fun - 2"


#new array of enlarged shaoe without intializing entries
	enlargedImg1 = np.empty(enlargedShape1, dtype=np.uint8) #uint8 - unsigned integer (0 to 255)
	enlargedImg2 = np.empty(enlargedShape2, dtype=np.uint8)
	enlargedImg3 = np.empty(enlargedShape3, dtype=np.uint8)

	rowScale1 = float(im.shape[0]) / float(enlargedImg1.shape[0])
	colScale1 = float(im.shape[1]) / float(enlargedImg1.shape[1])
 
	rowScale2 = float(im.shape[0]) / float(enlargedImg2.shape[0])
	colScale2 = float(im.shape[1]) / float(enlargedImg2.shape[1])

	rowScale3 = float(im.shape[0]) / float(enlargedImg3.shape[0])
	colScale3 = float(im.shape[1]) / float(enlargedImg3.shape[1])


	for r in range(enlargedImg1.shape[0]):
		for c in range(enlargedImg1.shape[1]):
			o_r = r * rowScale1 #Find position in original image
			o_c = c * colScale1
			enlargedImg1[r, c] = GetBilinearPixel(im, o_c, o_r)
	
	cv2.imshow(window_name2,enlargedImg1)
	im2 = cv2.resize(im,None,fx=0.5,fy=0.5)
	cv2.imshow(window_name5,im2)
	cv2.waitKey()
	cv2.destroyAllWindows()

	for r in range(enlargedImg2.shape[0]):
		for c in range(enlargedImg2.shape[1]):
			o_r = r * rowScale2 #Find position in original image
			o_c = c * colScale2
			enlargedImg2[r, c] = GetBilinearPixel(im, o_c, o_r)

	cv2.imshow(window_name3,enlargedImg2)
	im3 = cv2.resize(im,None,fx=1,fy=1)
	cv2.imshow(window_name6,im3)
	cv2.waitKey()
	cv2.destroyAllWindows()


	for r in range(enlargedImg3.shape[0]):
		for c in range(enlargedImg3.shape[1]):
			o_r = r * rowScale3 #Find position in original image
			o_c = c * colScale3
			enlargedImg3[r, c] = GetBilinearPixel(im, o_c, o_r)

	cv2.imshow(window_name4,enlargedImg3)
	im4 = cv2.resize(im,None,fx=2,fy=2)
	cv2.imshow(window_name7,im4)
	cv2.waitKey()
	cv2.destroyAllWindows()
