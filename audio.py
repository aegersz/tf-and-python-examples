"""
------------------------

AUDIO ARRAY MANIPULATION

------------------------

see also > https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html
"""

import os
import numpy as np
import wavio

# 1 second MONO WAV files
# "NO"
w  = wavio.read('/samba/anonymous/01648c51_nohash_0.wav')
# "YES"
w2 = wavio.read('/samba/anonymous/004ae714_nohash_0.wav')

# print full
# np.set_printoptions(threshold=np.inf)

print("w: %s" % w)
print(w.rate)
print(w.sampwidth)

data = w.data
data2 = w2.data

print("data:")
print(data)
print(data.shape)
print(data.size)
print(data.ndim)
print(data.dtype)

# reverse the audio array
rev_data = data[::-1]
print
print("rev_data is:")
print(rev_data)

# (off) concatenate 3 audio arrays
#data = np.concatenate([data,rev_data,w2.data])

# overlay two audio arrays
data = data/2
data2 = data2/2
data = data+data2

# (off) repeat every element (low pitch, slow it down)
#data = np.repeat(data, 2)

# (off) remove every second element (high pitch, speed it up)
#data = data[1::2]

print
print("---------")
print("after ...")
print(data)
print(data.size)
print(len(data))

rate = w.rate
sampwidth = w.sampwidth
wavio.write("bar.wav", data, rate, sampwidth=sampwidth)

# copy the new wav file to Windows
cmd = "cp bar.wav /samba/anonymous/"
