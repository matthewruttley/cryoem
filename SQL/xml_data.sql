/* CRYO FILE ANALYSIS */

CREATE SCHEMA IF NOT EXISTS cryo.xml_files;

DROP TABLE IF EXISTS cryo.xml_files;

CREATE TABLE IF NOT EXISTS cryo.xml_files
(
  -- Put field types here
  filename VARCHAR,
  admin_date TIMESTAMP,
  grid VARCHAR,
  grid_material VARCHAR,
  grid_mesh INT,
  grid_film VARCHAR,
  pretreatment VARCHAR,
  cryogen VARCHAR,
  humidity INT,
  temp INT,
  Vitrobot VARCHAR,
  Microscope VARCHAR,
  Illumination VARCHAR,
  Imaging_mode VARCHAR,
  Electron_Source VARCHAR,
  Accelereation_voltage INT,
  nominal_defocus_min DECIMAL,
  nominal_defocus_max DECIMAL,
  calibrated_magnification DECIMAL,
  specimen_holder_model VARCHAR,
  detector VARCHAR,  
  detector_mode VARCHAR,
  average_exposure_time DECIMAL,
  electron_exposure DECIMAL,
  CTF_estimation_program VARCHAR,
  CTF_estimation_program_version DECIMAL,
  3D_classification_classes INT,
  symmetry_point_group VARCHAR,
  Resolution DECIMAL,
  resolution_est_method VARCHAR,
  refinement_program VARCHAR,
  refinement_program_version DECIMAL,
  Refinement_type VARCHAR,
  map_size INT,
  voxel_density_min INT,
  voxel_density_max INT,
  voxel_density_avg INT,
  voxel_density_std INT
  
);

CREATE INDEX cryo_name on cryo.xml_files (filename);

INSERT INTO cryo.xml_files VALUES
