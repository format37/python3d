import pymesh
from myplot_vf import plot_vf
import imageio
import os
import datetime

gif_half_size = 30

sponge = pymesh.meshio.load_mesh('/pymesh_examples/pymesh_example_04_3.stl')

filenames = []
imageio_images = []

# rendering
for i in range(gif_half_size):
    vertices = sponge.vertices
    faces = sponge.faces
    filename = '/pymesh_examples/pymesh_example_05_3_'+str(i)+'.png'
    print(filename)
    filenames.append(filename)    
    plot_vf(vertices, faces, cam_x=i, cam_y=i, filename = filename)

print('forward rendering..')
for i in range(gif_half_size):
    print(datetime.datetime.now(), filenames[i])
    imageio_images.append(imageio.imread(filenames[i]))
    i-=1

print('reverse rendering..')
i = gif_half_size-1
while i>0:
    print(datetime.datetime.now(), filenames[i])
    images.append(imageio.imread(filenames[i]))
    i-=1

# save gif
imageio.mimsave('/pymesh_examples/pymesh_example_05_3.gif', imageio_images)

# remove images
for filename in filenames:
    os.remove(filename)
