from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class crop_conditions_kansas(db.Model):
    id = db.Column('crop_conditions_kansas_id', db.Integer, primary_key=True)
    week_ending = db.Column(db.Date())
    state_name = db.Column(db.String(128), nullable=False)
    country_code = db.Column(db.Integer(), nullable=True)
    location_desc = db.Column(db.String(128), nullable=True)
    begin_code = db.Column(db.Integer(), nullable=True)
    zip_5 = db.Column(db.String(), nullable=True)
    county_ansi = db.Column(db.String(), nullable=True)
    state_alpha = db.Column(db.String(10), nullable=True)
    util_practice_desc = db.Column(db.String(), nullable=True)
    domain_desc = db.Column(db.String(), nullable=True)
    asd_desc = db.Column(db.String(), nullable=True)
    freq_desc = db.Column(db.String(), nullable=True)
    prodn_practice_desc = db.Column(db.String(), nullable=True)
    end_code = db.Column(db.Integer(), nullable=True)
    sector_desc = db.Column(db.String(), nullable=True)
    short_desc = db.Column(db.String(256), nullable=True)
    country_name = db.Column(db.String(120), nullable=True)
    value = db.Column(db.Integer(), nullable=False)
    reference_period_desc = db.Column(db.String(100), nullable=True)
    class_desc = db.Column(db.String(), nullable=True)
    asd_code = db.Column(db.String(), nullable=True)
    agg_level_desc = db.Column(db.String(), nullable=True)
    county_name = db.Column(db.String(), nullable=True)
    region_desc = db.Column(db.String(), nullable=True)
    watershed_desc = db.Column(db.String(), nullable=True)
    state_ansi = db.Column(db.Integer(), nullable=True)
    congr_district_code = db.Column(db.String(), nullable=True)
    domaincat_desc = db.Column(db.String(), nullable=True)
    state_fips_code = db.Column(db.Integer(), nullable=True)
    group_desc = db.Column(db.String(), nullable=True)
    watershed_code = db.Column(db.String(), nullable=True)
    unit_desc = db.Column(db.String(), nullable=True)
    source_desc = db.Column(db.String(), nullable=True)
    load_time = db.Column(db.DateTime(), nullable=True)
    statisticcat_desc = db.Column(db.String(100), nullable=True)
    commodity_desc = db.Column(db.String(50), nullable=True)
    year = db.Column(db.Integer())
    

    def __init__(self, name, city, addr):
        self.week_ending = week_ending
        self.state_name = state_name
        self.country_code = country_code
        self.location_desc = location_desc
        self.begin_code = begin_code
        self.zip_5 = zip_5
        self.county_ansi = county_ansi
        self.state_alpha = state_alpha
        self.util_practice_desc = util_practice_desc
        self.domain_desc = domain_desc
        self.asd_desc = asd_desc
        self.freq_desc = freq_desc
        self.prodn_practice_desc = prodn_practice_desc
        self.end_code = end_code
        self.sector_desc = sector_desc
        self.short_desc = short_desc
        self.country_name = country_name
        self.value = value
        self.reference_period_desc = reference_period_desc
        self.class_desc = class_desc
        self.asd_code = asd_code
        self.agg_level_desc = agg_level_desc
        self.county_name = county_name
        self.region_desc = region_desc
        self.watershed_desc = watershed_desc
        self.state_ansi = state_ansi
        self.congr_district_code = congr_district_code
        self.domaincat_desc = domaincat_desc
        self.state_fips_code = state_fips_code
        self.group_desc = group_desc
        self.watershed_code = watershed_code
        self.unit_desc = unit_desc
        self.source_desc = source_desc
        self.load_time = load_time
        self.county_code = county_code
        self.statisticcat_desc = statisticcat_desc
        self.commodity_desc = commodity_desc
        self.year = year
