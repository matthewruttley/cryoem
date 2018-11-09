/* CRYO FILE ANALYSIS */

CREATE SCHEMA IF NOT EXISTS xml_files;

DROP TABLE IF EXISTS xml_files;

CREATE TABLE IF NOT EXISTS xml_files
(
  -- Put field types here
  filename VARCHAR,
  grid VARCHAR,
  grid_material VARCHAR,
  grid_mesh INT,
  Microscope VARCHAR,
  electron_source VARCHAR,
  Acceleration_voltage INT,
  illumination VARCHAR,
  imaging_mode VARCHAR,
  detector VARCHAR,
  nominal_defocus_min DECIMAL,
  nominal_defocus_max DECIMAL,
  average_exposure_time DECIMAL,
  electron_exposure DECIMAL,
  resolution DECIMAL,
  resolution_est_method VARCHAR,
  map_size INT,
  pixel_spacing DECIMAL,
  ctf_program VARCHAR,
  ctf_program_version DECIMAL,
  voxel_density_min DECIMAL,
  voxel_density_max DECIMAL,
  voxel_density_avg DECIMAL,
  voxel_density_std DECIMAL
  
);

CREATE INDEX cryo_name on xml_files (filename);

INSERT INTO xml_files VALUES

