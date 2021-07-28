from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def plot_mesh(your_mesh, filename = None):
    # Create a new plot
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vertices))    
    # Show or save the plot
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
