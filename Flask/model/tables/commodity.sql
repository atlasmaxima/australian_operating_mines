CREATE TABLE IF NOT EXISTS commodity (
    id INTEGER PRIMARY KEY,
    proj_code VARCHAR(10),
    commodities VARCHAR(255),
    commodity_group_name VARCHAR(50),
    target_group_name VARCHAR(50),
    FOREIGN KEY (id) REFERENCES mine_sites (id)
)

