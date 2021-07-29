import pymesh
import numpy as np
from myplot import plot_vf

sponge = pymesh.meshio.load_mesh('pymesh_examples/pymesh_example_04_3.stl')

vertices = sponge.vertices
faces = sponge.faces

colors = np.array([int(f*8/len(faces)) for f in range(len(faces))])

plot_vf(vertices, faces, colors, filename = 'pymesh_example_04_3_0.png')
