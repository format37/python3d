import torch
from pytorch3d.structures.meshes import Meshes
from pytorch3d.io import IO, load_obj
from pytorch3d.renderer import (
    FoVPerspectiveCameras, look_at_view_transform,
    RasterizationSettings, BlendParams,
    MeshRenderer, MeshRasterizer, HardPhongShader, TexturesVertex
)
import matplotlib.pyplot as plt
import imageio
import os

gif_half_size = 27

if torch.cuda.is_available():
   device = torch.device("cuda:0")
   torch.cuda.set_device(device)
else:
   device = torch.device("cpu")

# Load object
verts, faces, aux = load_obj('pytorch3d_example_03.obj')

# init texture
verts_list = []
faces_list = []
texts_list = []

verts = torch.as_tensor(verts, dtype=torch.float32, device=device)
faces = torch.as_tensor(faces.verts_idx, dtype=torch.float32, device=device)
texts = torch.rand((len(verts), 3), dtype=torch.float32, device=device)
verts_list.append(verts)
faces_list.append(faces)
texts_list.append(texts)

# create textures
tex = TexturesVertex(texts_list)

# Initialise the mesh with textures
mesh = Meshes(verts=[verts], faces=[faces], textures=tex)[0]

filenames = []
imageio_images = []

# rendering
for i in range(gif_half_size):

    filename = 'pytorch3d_example_'+str(i)+'.png'
    print(filename)
    filenames.append(filename)

    # Select the viewpoint using spherical angles  
    distance = 3.5   # distance from camera to the object
    elevation = 0.0 + i   # angle of elevation in degrees
    azimuth = 0.0 + i  # No rotation so the camera is positioned on the +Z axis.

    # Get the position of the camera based on the spherical angles
    R, T = look_at_view_transform(distance, elevation, azimuth, device=device)

    # Initialize an OpenGL perspective camera.
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

    images = renderer(mesh)
    plt.figure(figsize=(10, 10))
    plt.imshow(images[0, ..., :3].cpu().numpy())
    plt.savefig(filename)
    plt.axis("off")
    imageio_images.append(imageio.imread(filename))
    

# reverse rendering
i = gif_half_size-1
while i>0:
    print(filenames[i])
    imageio_images.append(imageio.imread(filenames[i]))
    i-=1

# save gif
imageio.mimsave('pytorch3d_example_03.gif', imageio_images)

# remove images
for filename in filenames:
    os.remove(filename)
