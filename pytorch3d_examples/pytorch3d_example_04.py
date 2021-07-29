 # Imports
import torch
from pytorch3d.structures.meshes import Meshes
#from pytorch3d.io import IO, load_objs_as_meshes #load_obj
from pytorch3d.io import IO, load_obj
from pytorch3d.renderer import (
    FoVPerspectiveCameras, look_at_view_transform,
    RasterizationSettings, BlendParams,
    MeshRenderer, MeshRasterizer, HardPhongShader
)

"""if torch.cuda.is_available():
   device = torch.device("cuda:0")
   torch.cuda.set_device(device)
else:
   device = torch.device("cpu")
"""
device = torch.device("cpu")

# Initialize an OpenGL perspective camera.
R, T = look_at_view_transform(2.7, 10, 20)
cameras = FoVPerspectiveCameras(device=device, R=R, T=T)

# Define the settings for rasterization and shading. Here we set the output image to be of size
# 512x512. As we are rendering images for visualization purposes only we will set faces_per_pixel=1
# and blur_radius=0.0. Refer to rasterize_meshes.py for explanations of these parameters.
raster_settings = RasterizationSettings(
    image_size=512,
    blur_radius=0.0,
    faces_per_pixel=1,
)

# Create a phong renderer by composing a rasterizer and a shader. Here we can use a predefined
# PhongShader, passing in the device on which to initialize the default parameters
renderer = MeshRenderer(
    rasterizer=MeshRasterizer(cameras=cameras, raster_settings=raster_settings),
    shader=HardPhongShader(device=device, cameras=cameras)
)

verts, faces, aux = load_obj('pytorch3d_example_01.obj')
# textures = TexturesVertex(verts_features=verts_rgb.to(device))
#mesh = Meshes(verts=[verts], faces=[faces.verts_idx])[0]
#mesh = load_objs_as_meshes(['pytorch3d_example_01.obj'], device=device)

### create texture
#verts_uvs = aux.verts_uvs[None, ...]  # (1, V, 2)
#faces_uvs = faces.textures_idx[None, ...]  # (1, F, 3)
verts_uvs = verts
faces_uvs = faces
tex_maps = aux.texture_images

# tex_maps is a dictionary of {material name: texture image}.
# Take the first image:
texture_image = list(tex_maps.values())[0]
texture_image = texture_image[None, ...]  # (1, H, W, 3)

# Create a textures object
tex = Textures(verts_uvs=verts_uvs, faces_uvs=faces_uvs, maps=texture_image)

# Initialise the mesh with textures
meshes = Meshes(verts=[verts], faces=[faces.verts_idx], textures=tex)


"""images = renderer(mesh)
plt.figure(figsize=(10, 10))
plt.imshow(images[0, ..., :3].cpu().numpy())
plt.axis("off")
"""