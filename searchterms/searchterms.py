
def get_list_of_search_terms():
  """
    Returns the terms to find in the XML files
  """
  useful_fields = [
    # Grid
    ['grid', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'model']],
    ['grid_material', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'material']],
    ['grid_mesh', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'mesh']],
    ['Microscope', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'microscope']],
    ['Accelereation_voltage', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'acceleration_voltage', '#text']],
    ['Illumination', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'illumination_mode']],
    ['Imaging_mode', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'imaging_mode']],
    ['detector', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'film_or_detector_model', '#text']],
    ['nominal_defocus_min', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'nominal_defocus_min', '#text']],
    ['nominal_defocus_max', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'nominal_defocus_max', '#text']],
    ['average_exposure_time', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'average_exposure_time', '#text']],
    ['electron_exposure', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'average_electron_dose_per_image', '#text']],
    ['Resolution', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'resolution', '#text']],
    ['resolution_est_method', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'resolution_method']],
    ['map_size', ['emd', 'map', 'dimensions', 'col']],
    ['map_size', ['emd', 'map', 'pixel_spacing', 'x', '#text']],
    ['voxel_density_min', ['emd', 'map', 'statistics', 'minimum']],
    ['CTF_estimation_program', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'ctf_correction', 'software_list', 'software', 'name']],
    ['CTF_estimation_program_version', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'ctf_correction', 'software_list', 'software', 'version']],
    ['voxel_density_max', ['emd', 'map', 'statistics', 'maximum']],
    ['voxel_density_avg', ['emd', 'map', 'statistics', 'average']],
    ['voxel_density_std', ['emd', 'map', 'statistics', 'std']],
  ]
  return useful_fields
   # plasma cleaning
  #  ['pretreatment', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'grid', 'pretreatment', 'type']],
   # Vitrification
  #  ['cryogen', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'cryogen_name']],
  #  ['humidity', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'chamber_humidity', '#text']],
  #  ['temperature', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'chamber_temperature','#text']],
  #  ['Vitrobot', ['emd', 'structure_determination_list', 'structure_determination', 'specimen_preparation_list', 'single_particle_preparation', 'vitrification', 'instrument']],
  
    #   Microscopy
    # Programs - refinement
 #   ['refinement_program', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'software_list', 'software', 'name']],
#    ['refinement_program_version', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'software_list', 'software', 'version']],
    # Programs - refinement assignment 
#    ['Refinement_type', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'initial_angle_assignment', 'type']],
 #   ['calibrated_magnification', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'calibrated_magnification']],
 #   ['specimen_holder_model', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'specimen_holder_model']],
    # Image recording
#    ['detector_mode', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'detector_mode']],
#    ['average_exposure_units', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'average_exposure_time', '@units']],
#    ['electron_exposure_units', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'image_recording_list', 'image_recording', 'average_electron_dose_per_image', '@units']],
    # Programs - CTF estimation
    # Symmetry
#    ['threeD_classification_classes', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'number_classes_used']],
  #  ['symmetry_point_group', ['emd', 'structure_determination_list', 'structure_determination', 'singleparticle_processing', 'final_reconstruction', 'applied_symmetry', 'point_group']],
 #   ['Electron_Source', ['emd', 'structure_determination_list', 'structure_determination', 'microscopy_list', 'single_particle_microscopy', 'electron_source']],
