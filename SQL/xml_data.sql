/* CRYO FILE ANALYSIS */

CREATE SCHEMA IF NOT EXISTS cryo.xml_files;

DROP TABLE IF EXISTS cryo.xml_files;

CREATE TABLE IF NOT EXISTS cryo.xml_files
(
  -- Put field types here
  filename VARCHAR,
  admin_date TIMESTAMP
);

CREATE INDEX cryo_name on cryo.xml_files (filename);

INSERT INTO cryo.xml_files VALUES
