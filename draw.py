import sys
sys.path.append("./")import numpy as np
import open3d as py3d
import copy

print("read ply points#############################")
print("input file pass 1 ?#############################")
# input your object full-pass
pcd1 = py3d.io.read_point_cloud("/home/nao/work/Open3D/examples/python/work/source.ply")
print("pcd1:", pcd1)
print("has points?", pcd1.has_points())
point_array = np.asarray(pcd1.points)
print(point_array.shape, "points:\n", point_array)
print("has color?", pcd1.has_colors())
print("colors:", np.asarray(pcd1.colors))
print("has normals?", pcd1.has_normals())

print("input file pass 2 ?#############################")
# input your object full-pass
pcd2 = py3d.io.read_point_cloud("/home/nao/work/Open3D/examples/python/work/my_output_file.ply") # メッシュなしply
print("pcd2:", pcd2)
print("has points?", pcd2.has_points())
point_array = np.asarray(pcd2.points)
print(point_array.shape, "points:\n", point_array)
print("has color?", pcd2.has_colors())
print("colors:", np.asarray(pcd2.colors))
print("has normals?", pcd2.has_normals())

size = len(pcd1.points)
pcd1 += pcd2
# Number of lines from 0
count=0
limit=200

lines=[]
for l in range(size) :
    lines+=[[l,l+size]]
    count=count+1
    if count==limit:
        break
line_set = py3d.geometry.LineSet(
    points=pcd1.points,
    lines=py3d.utility.Vector2iVector(lines),
)
colors = [[1, 0, 0] for i in range(len(lines))]
line_set.colors = py3d.utility.Vector3dVector(colors)
py3d.visualization.draw_geometries([pcd1,line_set], window_name="pcd1 without normals", width=640, height=480)
