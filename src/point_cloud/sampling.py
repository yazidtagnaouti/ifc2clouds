import numpy as np

def sample_edge(v1, v2, num_points=100):
    """Generate points along an edge."""
    return [tuple(v1 + t * (v2 - v1)) for t in np.linspace(0, 1, num_points)]

def sample_face(v1, v2, v3, num_points=1000):
    """Generate points inside a triangular face using barycentric coordinates."""
    points = []
    for _ in range(num_points):
        r1, r2 = np.random.rand(), np.random.rand()
        if r1 + r2 > 1:
            r1, r2 = 1 - r1, 1 - r2
        point = (1 - r1 - r2) * v1 + r1 * v2 + r2 * v3
        points.append(tuple(point))
    return points

def generate_point_cloud(geometry, edge_samples=5, face_samples=50):
    """Generates a point cloud from IFC geometry."""
    vertices, edges, faces = geometry["vertices"], geometry["edges"], geometry["faces"]
    point_cloud = set(vertices)

    for edge in edges:
        v1, v2 = np.array(vertices[edge[0]]), np.array(vertices[edge[1]])
        point_cloud.update(sample_edge(v1, v2, edge_samples))

    for face in faces:
        v1, v2, v3 = np.array(vertices[face[0]]), np.array(vertices[face[1]]), np.array(vertices[face[2]])
        point_cloud.update(sample_face(v1, v2, v3, face_samples))

    return list(point_cloud)
