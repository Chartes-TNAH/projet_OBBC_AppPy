from app.app import db
from sqlalchemy import Column, Integer, String

#  On importe l'objet SQLAlchemy du module flask_sqlachemy

#  On crée une class pour la table ; une ligne par colonne

class ChansonBB(db.Model):

    __tablename__ = "chansonBB"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titre_fr = db.Column(db.String(45), index=True, unique=True)
    titre_brz = db.Column(db.String(45), index=True, unique=True)
    dialecte = db.Column(db.String(64))
    theme = db.Column(db.String(64))
    chanson_fr = db.Column(db.Text, index=True, unique=True)
    chanson_brz = db.Column(db.Text, index=True, unique=True)
    cheminPartition = db.Column(db.String(64), index=True, unique=True)

