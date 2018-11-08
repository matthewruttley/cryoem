
def get_list_of_search_terms():
  """
    Returns the terms to find in the XML files
  """
  useful_fields = [
    ['admin_date', ['emd', 'admin', 'current_status', 'date']],
    ['admin_date', ['emd', 'admin', 'current_status', 'date']],
    # Grid
    ['grid', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'model']],
    ['grid_material', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'material']],
    ['grid_mesh', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'mesh']],
    ['grid_film', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'support_film']],
    # plasma cleaning
    ['pretreatment', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'pretreatment', 'type']],
    # Vitrification
    ['cryogen', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'cryogen_name']],
    ['humidity', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'chamber_humidity']],
    ['temp', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'chamber_temperature']],
    ['Vitrobot', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'instrument']],
  
    #   Microscopy
    # 
    ['Microscope', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'microscope']],
    ['Illumination', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'illumination_mode']],
    ['Imaging_mode', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'imaging_mode']],
    ['Electron_Source', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'electron_source']],
    ['Accelereation_voltage', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'acceleration_voltage']],
    ['nominal_defocus_min', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'nominal_defocus_min']],
    ['nominal_defocus_max', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'nominal_defocus_max']],
    ['calibrated_magnification', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'calibrated_magnification']],
    ['specimen_holder_model', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'specimen_holder_model']],
    # Image recording
  # Add cols to pick out here'
  ]
  return useful_fields
