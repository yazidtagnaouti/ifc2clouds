from ifc_utils.ifc_loader import load_ifc
from ifc_utils.ifc_geolocation import get_global_origin
from point_cloud.visualization import visualize_point_cloud_open3d
from ifc_utils.ifc_processing import process_ifc_walls, process_storey_point_cloud

if __name__ == "__main__":
    ifc_file_path = "../test_data\PN1833_05_EXE_BIM_000013_01_17IGR_SGO_Structure_ifc2x3.ifc"
    storey_name = "S01"

    ifc_data = load_ifc(ifc_file_path)
    global_origin = get_global_origin(ifc_data)
    
    # Process point cloud for the given storey
    point_cloud = process_storey_point_cloud(ifc_data, storey_name)
    # point_cloud = process_ifc_walls(ifc_data)
    
    # Visualize the point cloud
    visualize_point_cloud_open3d(point_cloud)
