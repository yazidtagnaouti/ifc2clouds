import numpy as np

def dms_to_decimal(dms_tuple):
    """Converts (Degrees, Minutes, Seconds, Millionths) to decimal degrees."""
    if not dms_tuple or len(dms_tuple) < 3:
        return 0.0
    degrees, minutes, seconds, millionths = dms_tuple + (0,) * (4 - len(dms_tuple))
    return degrees + minutes / 60 + (seconds + millionths / 1e6) / 3600

def get_global_origin(ifc_file):
    """Extracts the global origin from IfcSite."""
    site = ifc_file.by_type("IfcSite")
    if site:
        lat = dms_to_decimal(site[0].RefLatitude)
        lon = dms_to_decimal(site[0].RefLongitude)
        elev = site[0].RefElevation if site[0].RefElevation else 0.0
        return np.array([lon, lat, elev])
    return np.array([0, 0, 0])  # Default
