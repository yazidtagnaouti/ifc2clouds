import open3d as o3d
import numpy as np

def visualize_point_cloud_open3d(points):
    """Visualizes a 3D point cloud interactively using Open3D."""
    points = np.array(points)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd])
