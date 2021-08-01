from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def plot_vf(
    vertices, 
    faces, 
    colors=None, 
    cam_x=0, 
    cam_y=0, 
    size_x=10, 
    size_y=10, 
    dpi=80, 
    filename = None
    ):

    if colors is None:
        colors = np.array([int(f*8/len(faces)) for f in range(len(faces))])

    fig = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    ax = mplot3d.Axes3D(fig)

    ax.view_init(elev=cam_x, azim=cam_y)

    norm = plt.Normalize(colors.min(), colors.max())
    colors = plt.cm.viridis(norm(colors))

    pc = mplot3d.art3d.Poly3DCollection(vertices[faces], facecolors=colors, edgecolor="black")
    ax.add_collection(pc)

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
    