""" Define table models for episode table and episode instances """
from engine.db import Base
from sqlalchemy import Column, Integer, String


class Episode(Base):
    """ Episode table inherits from declarative base to define columns """
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    date = Column(String(20), nullable=False, unique=True)
    black_gesso = Column(Integer, nullable=False, default=0)
    bright_red = Column(Integer, nullable=False, default=0)
    burnt_umber = Column(Integer, nullable=False, default=0)
    cadmium_yellow = Column(Integer, nullable=False, default=0)
    dark_sienna = Column(Integer, nullable=False, default=0)
    indian_red = Column(Integer, nullable=False, default=0)
    indian_yellow = Column(Integer, nullable=False, default=0)
    liquid_black = Column(Integer, nullable=False, default=0)
    liquid_clear = Column(Integer, nullable=False, default=0)
    midnight_black = Column(Integer, nullable=False, default=0)
    phthalo_blue = Column(Integer, nullable=False, default=0)
    phthalo_green = Column(Integer, nullable=False, default=0)
    prussian_blue = Column(Integer, nullable=False, default=0)
    sap_green = Column(Integer, nullable=False, default=0)
    titanium_white = Column(Integer, nullable=False, default=0)
    van_dyke_brown = Column(Integer, nullable=False, default=0)
    yellow_ochre = Column(Integer, nullable=False, default=0)
    alizarin_crimson = Column(Integer, nullable=False, default=0)
    aurora_borealis = Column(Integer, nullable=False, default=0)
    barn = Column(Integer, nullable=False, default=0)
    beach = Column(Integer, nullable=False, default=0)
    boat = Column(Integer, nullable=False, default=0)
    bridge = Column(Integer, nullable=False, default=0)
    building = Column(Integer, nullable=False, default=0)
    bushes = Column(Integer, nullable=False, default=0)
    cabin = Column(Integer, nullable=False, default=0)
    cactus = Column(Integer, nullable=False, default=0)
    cirrus = Column(Integer, nullable=False, default=0)
    cliff = Column(Integer, nullable=False, default=0)
    clouds = Column(Integer, nullable=False, default=0)
    conifer = Column(Integer, nullable=False, default=0)
    cumulus = Column(Integer, nullable=False, default=0)
    deciduous = Column(Integer, nullable=False, default=0)
    dock = Column(Integer, nullable=False, default=0)
    farm = Column(Integer, nullable=False, default=0)
    fence = Column(Integer, nullable=False, default=0)
    fire = Column(Integer, nullable=False, default=0)
    flowers = Column(Integer, nullable=False, default=0)
    fog = Column(Integer, nullable=False, default=0)
    grass = Column(Integer, nullable=False, default=0)
    hills = Column(Integer, nullable=False, default=0)
    lake = Column(Integer, nullable=False, default=0)
    lighthouse = Column(Integer, nullable=False, default=0)
    mill = Column(Integer, nullable=False, default=0)
    moon = Column(Integer, nullable=False, default=0)
    mountain = Column(Integer, nullable=False, default=0)
    mountains = Column(Integer, nullable=False, default=0)
    night = Column(Integer, nullable=False, default=0)
    ocean = Column(Integer, nullable=False, default=0)
    palm_trees = Column(Integer, nullable=False, default=0)
    path = Column(Integer, nullable=False, default=0)
    person = Column(Integer, nullable=False, default=0)
    portrait = Column(Integer, nullable=False, default=0)
    river = Column(Integer, nullable=False, default=0)
    rocks = Column(Integer, nullable=False, default=0)
    snow = Column(Integer, nullable=False, default=0)
    snowy_mountain = Column(Integer, nullable=False, default=0)
    structure = Column(Integer, nullable=False, default=0)
    sun = Column(Integer, nullable=False, default=0)
    tree = Column(Integer, nullable=False, default=0)
    trees = Column(Integer, nullable=False, default=0)
    waterfall = Column(Integer, nullable=False, default=0)
    waves = Column(Integer, nullable=False, default=0)
    windmill = Column(Integer, nullable=False, default=0)
    winter = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        """ Return string representation of object """
        return f'<Episode {self.title}>'
    return f'<Episode {self.column_name}>'