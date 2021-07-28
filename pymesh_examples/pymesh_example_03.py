import pymesh
import numpy as np
import math

def mesh_trans(mesh, x, y, z):
   return pymesh.form_mesh(mesh.vertices + [[x, y, z]], mesh.faces)

def mesh_rotate(mesh, x, y, z, angle):
   rot = pymesh.Quaternion.fromAxisAngle(np.array([x, y, z]), math.pi*2*angle/360)
   return pymesh.form_mesh(np.dot(rot.to_matrix(), mesh.vertices.T).T, mesh.faces)

sponge = pymesh.generate_box_mesh([0,0,0], [1,1,1])
bool_box = pymesh.generate_box_mesh([0.4,0.4,-0.1], [0.6,0.6,1.1])
sponge = pymesh.boolean(sponge, bool_box, operation='difference', engine="igl")

bool_box = mesh_rotate(mesh = bool_box, x = 1, y = 0, z = 0, angle = 90)
bool_box = mesh_trans(mesh = bool_box, x = 0, y = 1, z = 0)
sponge = pymesh.boolean(sponge, bool_box, operation='difference', engine="igl")

filename = "/pymesh_examples/pymesh_example_03.stl"
pymesh.save_mesh(filename, sponge, ascii=False)
