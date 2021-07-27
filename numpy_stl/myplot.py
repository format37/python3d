from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


def plot_verticles(vertices, isosurf = False):
    
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

    plt.show()


def plot_mesh(your_mesh, filename = None):
    # Create a new plot
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    figure.add_axes(axes)
    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    # Show the plot to the screen
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)