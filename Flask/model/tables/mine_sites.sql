CREATE TABLE IF NOT EXISTS mine_sites (
    id INTEGER PRIMARY KEY,
    proj_code VARCHAR(10),
    short_title VARCHAR(255),
    site_type VARCHAR(50),
    sub_type VARCHAR(50),
    stage VARCHAR(50),
    longitude NUMERIC(18,15),
    latitude NUMERIC(18,15)
)