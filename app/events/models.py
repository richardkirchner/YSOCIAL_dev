from app.extensions.database import db, CRUDMixin

class event(db.Model,CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    date = db.Column(db.Integer)
    desc =db.Column(db.String(1024))




