from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()

class RelevesCFauneModel(db.Model):
    __tablename__       = 't_releves_cfaune'
    __table_args__      = {'schema':'contactfaune'}
    id_releve_cfaune    = db.Column(db.BigInteger, primary_key=True)
    id_lot              = db.Column(db.Integer)
    id_numerisateur     = db.Column(db.Integer)
    date_min            = db.Column(db.Date, nullable=False)
    date_max            = db.Column(db.Date, nullable=False)
    heure_obs           = db.Column(db.Integer)
    insee               = db.Column(db.Text(length='5'))
    altitude_min        = db.Column(db.Integer)
    altitude_max        = db.Column(db.Integer)
    saisie_initiale     = db.Column(db.Text(length='20'))
    supprime            = db.Column(db.BOOLEAN(create_constraint=False))
    date_insert         = db.Column(db.Date, nullable=False)
    date_update         = db.Column(db.Date, nullable=False)
    commentaire         = db.Column(db.Text)
    the_geom_local      = db.Column(Geometry)
    the_geom_3857       = db.Column(Geometry)
    id_nomenclature_technique_obs   = db.Column(db.Integer, nullable=False)
    id_nomenclature_eta_bio         = db.Column(db.Integer, nullable=False)

    def __init__(self, id_releve_cfaune):
        self.id_releve_cfaune = id_releve_cfaune
    
    def json(self):
        return {column.key: getattr(self, column.key) if not isinstance(column.type, db.Date) else str(getattr(self, column.key)) for column in self.__table__.columns }

    @classmethod
    def find_by_id(cls, id_releve_cfaune):
        return cls.query.filter_by(id_releve_cfaune=id_releve_cfaune).first()