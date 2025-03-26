from ifc_utils.ifc_geolocation import get_global_origin
from ifc_utils.ifc_geometry import get_geom
from ifc_utils.ifc_transformation import get_wall_transformation
from point_cloud.sampling import generate_point_cloud
from config import SETTINGS

def get_storey(ifc_file, storey_name):
    """Finds an IfcBuildingStorey by name."""
    for storey in ifc_file.by_type("IfcBuildingStorey"):
        if storey.Name and storey_name.lower() in storey.Name.lower():
            return storey
    return None

def get_walls_in_storey(ifc_file, storey):
    """Finds all walls contained in a specific storey."""
    walls_in_storey = []
    for wall in ifc_file.by_type("IfcWall"):
        if wall.ContainedInStructure:
            for rel in wall.ContainedInStructure:
                if rel.RelatingStructure == storey:
                    walls_in_storey.append(wall)
    return walls_in_storey

def transform_to_global(local_points, global_origin, wall_transform):
    """Transforms local points to global coordinates."""
    return [point + wall_transform + global_origin for point in local_points]

def process_storey_point_cloud(ifc_file, storey_name, edge_samples=5, face_samples=25):
    """Generates a point cloud for walls in a specific storey."""
    global_origin = get_global_origin(ifc_file)
    storey = get_storey(ifc_file, storey_name)
    
    if not storey:
        print(f"Storey '{storey_name}' not found!")
        return []

    walls = get_walls_in_storey(ifc_file, storey)
    
    all_points = []
    
    for wall in walls:
        ifc_geometry = get_geom(settings=SETTINGS, entity=wall)
        local_points = generate_point_cloud(ifc_geometry, edge_samples=edge_samples, face_samples=face_samples)
        
        # Get wall location and orientation (axis)
        wall_location = get_wall_transformation(wall)
        
        # Transform local points to global points
        global_points = transform_to_global(local_points, global_origin, wall_location)
        
        all_points.extend(global_points)
    
    return all_points


def process_ifc_walls(ifc_file):
    """Processes all walls in an IFC file and applies georeferencing with orientation."""
    global_origin = get_global_origin(ifc_file)
    walls = ifc_file.by_type("IfcWall")
    
    all_points = []
    
    for wall in walls:
        ifc_geometry = get_geom(settings=SETTINGS, entity=wall)
        local_points = generate_point_cloud(ifc_geometry, edge_samples=10, face_samples=100)
        
        # Get wall location and orientation (axis)
        wall_location = get_wall_transformation(wall)
        
        # Transform local points to global points
        global_points = transform_to_global(local_points, global_origin, wall_location)
        
        all_points.extend(global_points)
    
    return all_points
