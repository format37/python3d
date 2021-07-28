import pymesh
from myplot import plot_mesh

sponge = pymesh.meshio.load_mesh('/pymesh_examples/pymesh_example_04_3.stl')
plot_mesh(sponge, '/pymesh_examples/pymesh_example_05_3_0.png')
