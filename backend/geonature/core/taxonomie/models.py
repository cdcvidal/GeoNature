from geonature.utils.env import DB
from geonature.utils.utilssqlalchemy import serializable


@serializable
class TaxrefProtectionArticles(DB.Model):
    __tablename__ = 'taxref_protection_articles'
    __table_args__ = {'schema': 'taxonomie'}
    cd_protection = DB.Column(DB.Unicode, primary_key=True)
    article = DB.Column(DB.Unicode)
    intitule = DB.Column(DB.Unicode)
    arrete = DB.Column(DB.Unicode)
    cd_arrete = DB.Column(DB.Integer)
    url_inpn = DB.Column(DB.Unicode)
    cd_doc = DB.Column(DB.Integer)
    url = DB.Column(DB.Unicode)
    date_arrete = DB.Column(DB.Integer)
    type_protection = DB.Column(DB.Unicode)
    concerne_mon_territoire = DB.Column(DB.Boolean)

    def __repr__(self):
        return '<TaxrefProtectionArticles %r>' % self.article


@serializable
class TaxrefProtectionEspeces(DB.Model):
    __tablename__ = 'taxref_protection_especes'
    __table_args__ = {'schema': 'taxonomie'}
    cd_nom = DB.Column(DB.Unicode, primary_key=True)
    cd_protection = DB.Column(DB.Unicode, primary_key=True)
    nom_cite = DB.Column(DB.Unicode)
    syn_cite = DB.Column(DB.Unicode)
    nom_francais_cite = DB.Column(DB.Unicode)
    precisions = DB.Column(DB.Unicode)
    cd_nom_cite = DB.Column(DB.Unicode, primary_key=True)


@serializable
class Taxref(DB.Model):
    __tablename__ = 'taxref'
    __table_args__ = {'schema': 'taxonomie'}
    cd_nom = DB.Column(DB.Integer, primary_key=True)
    id_statut = DB.Column(DB.Unicode)
    id_habitat = DB.Column(DB.Integer)
    id_rang = DB.Column(DB.Unicode)
    regne = DB.Column(DB.Unicode)
    phylum = DB.Column(DB.Unicode)
    classe = DB.Column(DB.Unicode)
    regne = DB.Column(DB.Unicode)
    ordre = DB.Column(DB.Unicode)
    famille = DB.Column(DB.Unicode)
    sous_famille = DB.Column(DB.Unicode)
    tribu = DB.Column(DB.Unicode)
    cd_taxsup = DB.Column(DB.Integer)
    cd_sup = DB.Column(DB.Integer)
    cd_ref = DB.Column(DB.Integer)
    lb_nom = DB.Column(DB.Unicode)
    lb_auteur = DB.Column(DB.Unicode)
    nom_complet = DB.Column(DB.Unicode)
    nom_complet_html = DB.Column(DB.Unicode)
    nom_vern = DB.Column(DB.Unicode)
    nom_valide = DB.Column(DB.Unicode)
    nom_vern_eng = DB.Column(DB.Unicode)
    group1_inpn = DB.Column(DB.Unicode)
    group2_inpn = DB.Column(DB.Unicode)
    url = DB.Column(DB.Unicode)

    def __repr__(self):
        return '<Taxref %r>' % self.nom_complet