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
  Resolution DECIMAL  
  
);

CREATE INDEX cryo_name on cryo.xml_files (filename);

INSERT INTO cryo.xml_files VALUES
('emd-3802-v30.xml', '2018-10-17', '2018-10-17', 'C-flat-4/2', 'COPPER', '400', [OrderedDict([(u'@film_type_id', u'1'), (u'film_material', u'CARBON'), (u'film_topology', u'HOLEY')]), OrderedDict([(u'@film_type_id', u'2'), (u'film_material', u'CARBON'), (u'film_topology', u'CONTINUOUS')])], 'PLASMA CLEANING', 'ETHANE', OrderedDict([(u'@units', u'percentage'), ('#text', u'100')]), OrderedDict([(u'@units', u'K'), ('#text', u'278.15')]), 'FEI VITROBOT MARK IV', 'FEI TITAN', 'FLOOD BEAM', 'BRIGHT FIELD', 'FIELD EMISSION GUN', OrderedDict([(u'@units', u'kV'), ('#text', u'300')]), OrderedDict([(u'@units', u'\xb5m'), ('#text', u'2.0')]), OrderedDict([(u'@units', u'\xb5m'), ('#text', u'4.5')]), '37879.', 'GATAN 626 SINGLE TILT LIQUID NITROGEN CRYO TRANSFER HOLDER', 'GATAN K2 SUMMIT (4k x 4k)', 'COUNTING', OrderedDict([(u'@units', u's'), ('#text', u'8.7')]), OrderedDict([(u'@units', u'e/\u212b^2'), ('#text', u'40.0')]), 'CTFFIND', '4', '3', 'C1', OrderedDict([(u'@res_type', u'BY AUTHOR'), (u'@units', u'\u212b'), ('#text', u'4.4')])),('emd-9616-v30.xml', '2018-10-17', '2018-10-17', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'ETHANE', 'NULL', 'NULL', 'NULL', 'FEI TITAN KRIOS', 'FLOOD BEAM', 'DIFFRACTION', 'FIELD EMISSION GUN', OrderedDict([(u'@units', u'kV'), ('#text', u'300')]), 'NULL', 'NULL', 'NULL', 'NULL', 'GATAN K2 SUMMIT (4k x 4k)', 'NULL', 'NULL', OrderedDict([(u'@units', u'e/\u212b^2'), ('#text', u'50.0')]), 'NULL', 'NULL', 'NULL', 'NULL', OrderedDict([(u'@res_type', u'BY AUTHOR'), (u'@units', u'\u212b'), ('#text', u'3.48')]))
;