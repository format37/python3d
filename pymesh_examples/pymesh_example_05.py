import pymesh
from myplot import plot_vf
import imageio
import os

sponge = pymesh.meshio.load_mesh('/pymesh_examples/pymesh_example_04_3.stl')

filenames = []
images = []

# rendering
for i in range(30):
    vertices = sponge.vertices
    faces = sponge.faces
    filename = '/pymesh_examples/pymesh_example_05_3_'+str(i)+'.png'
    print(filename)
    filenames.append(filename)    
    plot_vf(vertices, faces, cam_x=i, cam_y=i, filename = filename)
    images.append(imageio.imread(filename))

# back rendering
i = 29
while i>0:
    images.append(imageio.imread(filenames[i]))
    i-=1

# save gif
imageio.mimsave('/pymesh_examples/pymesh_example_05_3.gif', images)

# remove images
for filename in filenames:
    os.remove(filename)
