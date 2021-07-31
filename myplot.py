from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


def plot_verticles(vertices, isosurf = False, filename = None):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]    
    if isosurf:
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
    else:
        ax.scatter(x, y, z, c='r', marker='o')    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)


def plot_mesh(
    your_mesh, 
    size_x=10, 
    size_y=10, 
    dpi=80, 
    filename = None
    ):
    # Create a new plot
    figure = plt.figure(figsize=(size_x, size_y), dpi=dpi)
    axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors, edgecolor="black"))
    figure.add_axes(axes)
    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)


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
    