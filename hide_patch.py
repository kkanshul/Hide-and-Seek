# code to hide the patches of an image randomly 
# input argument : path of the image

import mxnet as mx
import random
import matplotlib.pyplot as plt
import sys
def hide_patch(img):
    # get width and height of the image
    s = img.shape
    wd = s[0]
    ht = s[1]

    # possible grid size, 0 means no hiding
    grid_sizes=[0,16,32,44,56]

    # hiding probability
    hide_prob = 0.5
 
    # randomly choose one grid size
    grid_size= grid_sizes[random.randint(0,len(grid_sizes)-1)]

    # hide the patches
    if(grid_size>0):
         for x in range(0,wd,grid_size):
             for y in range(0,ht,grid_size):
                 x_end = min(wd, x+grid_size)  
                 y_end = min(ht, y+grid_size)
                 if(random.random() <=  hide_prob):
                       img[x:x_end,y:y_end,:]=0

    return img
              
    


#path of the image
im_path=sys.argv[1]

# read the input image
img = mx.image.imdecode(open(im_path, 'rb').read())

#resize the image
img = mx.image.imresize(img, 224, 224)

#subtract mean and divide standard deviation before calling hide_patch in actual training

img=  hide_patch(img)


plt.imshow(img.asnumpy()); plt.show()
