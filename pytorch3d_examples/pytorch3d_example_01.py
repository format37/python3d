import torch
from pytorch3d.io import save_obj
from scipy import spatial
import numpy as np

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    torch.cuda.set_device(device)
else:
    device = torch.device("cpu")

with_grad = False

verts = torch.tensor(
    [
        [-3, -3, 0],
        [+3, -3, 0],
        [+3, +3, 0],
        [-3, +3, 0],
        [+0, +0, +3]
    ],
    device=device,
    dtype=torch.float32,
    requires_grad=with_grad,
)

hull = spatial.ConvexHull(verts.cpu().numpy())
faces_data = hull.simplices

faces = torch.tensor(
    faces_data,
    device=device,
    dtype=torch.int64,
)

save_obj('pytorch3d_example_01.obj', verts, faces)
