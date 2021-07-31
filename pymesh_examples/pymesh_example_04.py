import numpy as np
import datetime
import pymesh
import math
import sys

time_start = datetime.datetime.now()

depth = int(sys.argv[1])

def mesh_trans(mesh, x, y, z):
   return pymesh.form_mesh(mesh.vertices + [[x, y, z]], mesh.faces)

def mesh_rotate(mesh, x, y, z, angle):
   rot = pymesh.Quaternion.fromAxisAngle(np.array([x, y, z]), math.pi*2*angle/360)
   return pymesh.form_mesh(np.dot(rot.to_matrix(), mesh.vertices.T).T, mesh.faces)

def menger_sponge(depth):
   mesh_fractal = pymesh.generate_box_mesh([0,0,0], [1,1,1])
   z = [-0.1,1.1]
   side = 1
   for d in range(1, depth+1):
      side /= 3
      for x in range(1,3**d,3):
         for y in range(1,3**d,3):
               print(datetime.datetime.now(), d, x, y, '/', depth, ':', 3**d)
               box_a = pymesh.generate_box_mesh([side*x,side*y,z[0]], [side*x+side,side*y+side,z[1]])
            
               box_b = mesh_rotate(mesh = box_a, x = 1, y = 0, z = 0, angle = 90)
               box_b = mesh_trans(mesh = box_b, x = 0, y = 1, z = 0)

               box_c = mesh_rotate(mesh = box_a, x = 0, y = 1, z = 0, angle = 90)
               box_c = mesh_trans(mesh = box_c, x = 0, y = 0, z = 1)

               mesh_fractal = pymesh.boolean(mesh_fractal, box_a, operation='difference', engine="igl")
               mesh_fractal = pymesh.boolean(mesh_fractal, box_b, operation='difference', engine="igl")
               mesh_fractal = pymesh.boolean(mesh_fractal, box_c, operation='difference', engine="igl")           

   return mesh_fractal

mesh_fractal = menger_sponge(depth)

pymesh.save_mesh("/pymesh_examples/pymesh_example_04_"+str(depth)+".stl", mesh_fractal, ascii=False)

time_end = datetime.datetime.now()
print('spent', (time_end - time_start).seconds, 'seconds')
