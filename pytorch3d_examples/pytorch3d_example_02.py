import torch
from pytorch3d.io import IO
from pytorch3d.structures.meshes import Meshes
from pytorch3d.structures import join_meshes_as_scene
from pytorch3d.transforms import RotateAxisAngle
from pytorch3d.transforms import Translate
from scipy import spatial
import numpy as np

if torch.cuda.is_available():
   device = torch.device("cuda:0")
   torch.cuda.set_device(device)
else:
   device = torch.device("cpu")

with_grad = False

host_verts = [
       [-3, -3, 0],
       [+3, -3, 0],
       [+3, +3, 0],
       [-3, +3, 0],
       [+0, +0, +3]
   ]

verts = torch.tensor(
   host_verts,
   device=device,
   dtype=torch.float32,
   requires_grad=with_grad,
)

hull = spatial.ConvexHull(host_verts)
faces = torch.tensor(
   hull.simplices,
   device=device,
   dtype=torch.int64,
)

mesh_a = Meshes(verts=[verts], faces=[faces])

rot = RotateAxisAngle(180,'X', device=device)
verts_b = rot.transform_points(mesh_a.verts_list()[0])

trans = Translate(0,0,5, device=device)
verts_b = trans.transform_points(verts_b)

mesh_b = Meshes(verts=[verts_b], faces=[faces])

mesh = join_meshes_as_scene([mesh_a, mesh_b])
IO().save_mesh(mesh, 'pytorch3d_example_02.obj')
