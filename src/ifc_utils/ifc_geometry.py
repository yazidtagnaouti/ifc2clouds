import ifcopenshell


def get_geom(settings, entity):
    """Extracts geometric information from an IFC entity."""
    shape = ifcopenshell.geom.create_shape(settings, entity)
    ios_vertices = shape.geometry.verts
    ios_edges = shape.geometry.edges
    ios_faces = shape.geometry.faces

    vertices = [tuple(ios_vertices[i:i+3]) for i in range(0, len(ios_vertices), 3)]
    edges = [ios_edges[i:i+2] for i in range(0, len(ios_edges), 2)]
    faces = [tuple(ios_faces[i:i+3]) for i in range(0, len(ios_faces), 3)]

    return {'vertices': vertices, 'edges': edges, 'faces': faces}
