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
  Accelereation_voltage INT,
  nominal_defocus_min DECIMAL,
  nominal_defocus_max DECIMAL,
  average_exposure_time DECIMAL,
  electron_exposure DECIMAL,
  Resolution DECIMAL,
  map_size INT,
  voxel_density_min DECIMAL,
  voxel_density_max DECIMAL,
  voxel_density_avg DECIMAL,
  voxel_density_std DECIMAL
  
);

CREATE INDEX cryo_name on xml_files (filename);

INSERT INTO xml_files VALUES
