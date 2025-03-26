import ifcopenshell

def load_ifc(ifc_file_path):
    """Loads an IFC file and returns the IFC model."""
    return ifcopenshell.open(ifc_file_path)