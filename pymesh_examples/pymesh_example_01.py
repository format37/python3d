import pymesh

box_a = pymesh.generate_box_mesh([0,0,0], [1,1,1])
filename = "/pymesh_examples/pymesh_example_01.stl"
pymesh.save_mesh(filename, box_a, ascii=False)
