import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_vf(vertices, faces, colors, size_x=10, size_y=10, dpi=80, filename = None):

    fig = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    ax = mplot3d.Axes3D(fig)

    norm = plt.Normalize(colors.min(), colors.max())
    colors = plt.cm.viridis(norm(colors))

    pc = mplot3d.art3d.Poly3DCollection(vertices[faces], facecolors=colors, edgecolor="black")
    ax.add_collection(pc)

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
