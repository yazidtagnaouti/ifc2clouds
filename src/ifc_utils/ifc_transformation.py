import numpy as np

def get_wall_transformation(ifc_entity):
    """Extracts the transformation matrix of an IFC element."""
    if ifc_entity.ObjectPlacement:
        placement = ifc_entity.ObjectPlacement.RelativePlacement
        location = np.array([
            placement.Location.Coordinates[0] if placement.Location else 0,
            placement.Location.Coordinates[1] if placement.Location else 0,
            placement.Location.Coordinates[2] if placement.Location else 0
        ])
        return location
    return np.array([0, 0, 0])  # Default if no placement
