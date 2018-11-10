/* CRYO FILE ANALYSIS */

CREATE SCHEMA IF NOT EXISTS xml_files;

DROP TABLE IF EXISTS xml_files;

CREATE TABLE IF NOT EXISTS xml_files
(
  -- Put field types here
  filename VARCHAR,
  admin_date DATE, 
  grid VARCHAR,
  grid_material VARCHAR,
  grid_mesh INT,
  microscope VARCHAR,
  e_source VARCHAR,
  acc_volt INT,
  illumination VARCHAR,
  imaging_mode VARCHAR,
  detector VARCHAR,
  nom_defocus_min DECIMAL,
  nom_defocus_max DECIMAL,
  avg_exp_time DECIMAL,
  e_exposure DECIMAL,
  res DECIMAL,
  res_est_method VARCHAR,
  struct_method VARCHAR,
  map_size INT,
  pixel_space DECIMAL,
  refine_prog VARCHAR,
  refine_prog_v VARCHAR,
  ctf_prog VARCHAR,
  ctf_prog_v VARCHAR,
  vox_den_min DECIMAL,
  vox_den_max DECIMAL,
  vox_den_avg DECIMAL,
  vox_den_std DECIMAL
  
);

CREATE INDEX cryo_name on xml_files (filename);

INSERT INTO xml_files VALUES

