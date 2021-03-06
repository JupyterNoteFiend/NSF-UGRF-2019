#Alternative way of rebinning image 

def avg_val_pic(img, numtiles,reshape_x,reshape_y): #input your img as file path
	from skimage import img_as_float
	import numpy as np
	import matplotlib.pyplot as plt
	import image_slicer
	from PIL import Image
	from skimage.filters import sobel
	
	
	
	imag = Image.open(img)
	image = sobel(img_as_float(imag))# Applies Sobel filter to image
	tiles = image_slicer.slice(img, numtiles, save=False)# Tiles the images into numtiles
	strg_arr = np.zeros((numtiles), dtype=np.uint16)  # storage array of zeros
	
	for f,tile in enumerate(tiles): 
		tl_img = tile.image
		pixels = (np.sum(tl_img))	# take sum pix value from sliced images
		strg_arr[f] = pixels 		# sets all values in empty array to mean of the tile
	
	strg_arr = strg_arr.reshape( np.sqrt(numtiles),np.sqrt(numtiles))#reshape_x, reshape_y)
	plt.imshow(strg_arr, origin='lower', vmin=strg_arr.std(), vmax=strg_arr.max())
	plt.show()
