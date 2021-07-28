import pymesh

box_a = pymesh.generate_box_mesh([0,0,0], [1,1,1])
box_b = pymesh.generate_box_mesh([0.4,0.4,0], [0.6,0.6,1])
box_c = pymesh.boolean(box_a, box_b, operation='difference', engine="igl")

filename = "/pymesh_examples/pymesh_example_02.stl"
pymesh.save_mesh(filename, box_c, ascii=False)
