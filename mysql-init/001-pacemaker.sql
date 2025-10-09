-- mysql-init/001-pacemaker.sql

CREATE TABLE IF NOT EXISTS pacemaker_readings(
  id VARCHAR(64) NOT NULL,
  bpm INT NOT NULL,
  temperature DECIMAL(4,1) NOT NULL,
  battery_percent DECIMAL(5,2) NOT NULL,
  alert BOOLEAN NOT NULL,
  lon DECIMAL(9,6) NOT NULL,
  lat DECIMAL(9,6) NOT NULL,
  ts BIGINT NOT NULL,
  PRIMARY KEY (id, ts)
) ENGINE=InnoDB;
