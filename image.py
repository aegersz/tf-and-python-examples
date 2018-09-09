"""
------------------------

IMAGE ARRAY MANIPULATION

------------------------

see http://learningtensorflow.com/lesson3/ """
"""

import tensorflow as tf
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# load the image
dirpath= "/samba/anonymous/"
filename = dirpath + "/MarshOrchid.jpg"
image = mpimg.imread(filename)

# load it's properties
height, width, depth = image.shape

# print out the dimensions and some of the array
print image.shape
print image

# init tf variables
x = tf.Variable(image, name='x')
w = tf.Variable(image, name='w')

model = tf.global_variables_initializer()

# tf main logic
with tf.Session() as session:

# rotate 90 degress
#   x = tf.transpose(x, perm=[1, 0, 2])
#
# flipped on vertical
#   x = tf.reverse_sequence(x, [width] * height, 1, batch_dim=0)
#   x = tf.reverse_sequence(x, np.ones((height,)) * width, 1, batch_dim=0)
#
# flipped on horizontal
#   x = tf.reverse_sequence(x, np.ones((width,)) * height, 0, batch_dim=1)
#   x = x + 10
#
# double up
#   x = tf.concat([x, x], 0)
#
# split horizontally and reverse mirror the top half
    w, x = tf.split(x, num_or_size_splits=2, axis=0)
    w = tf.reverse_sequence(x, np.ones((height/2,)) * width, 1, batch_dim=0)
    w = tf.reverse_sequence(w, np.ones((width,)) * height/2, 0, batch_dim=1)
    x = tf.concat([x, w], 0)
# apply "color blast"
#   x = x*2

    session.run(model)
    result = session.run(x)
#
# display image image on GUI
#   plt.imshow(result)
#   plt.show()
# save image as a jpeg for viewing in a graphical client
   plt.imsave('/samba/anonymous/test2.jpg', result)
