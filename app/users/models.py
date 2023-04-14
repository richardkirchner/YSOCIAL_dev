from app.extensions.database import db, CRUDMixin
#from flask_login import UserMixin



class User(db.Model,CRUDMixin,):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80), index=True, unique=True)
  password = db.Column(db.String(80))


#class email(db.Model, CRUDMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(80))
#    password = db.relationship('Password', backref='email', uselist=False, lazy=True)

#class Password(db.Model,CRUDMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    password = db.Column(db.String(25))
#    email_id = db.Column(db.Integer, db.ForeignKey('email.id'))

#class event_title(db.Model,CRUDMixin):
 #   id = db.Column(db.Integer, primary_key=True)
  #  event_title = db.Column(db.String(50), unique=True)
   # event_date = db.Column(db.Integer(8), unique=True)
    #event_discription =db.Column(db.String(250), unique=True)
    #event_date = db.relationship('event_date', backref='event_title', uselist=False, lazy=True)
    #event_discription = db.relationship('event_discription', backref='event_title', uselist=False, lazy=True)


#class event_date(db.Model,CRUDMixin):
 #   id = db.Column(db.Integer, primary_key=True)
  #  event_date = db.Column(db.Integer(8))
  #  event_tilte_id = db.Column(db.Integer, db.ForeignKey('event_title.id'))
#class event_discription(db.Model,CRUDMixin):
 #   id = db.Column(db.Integer, primary_key=True)
  #  event_discription = db.Column(db.String(250))
   # event_title_id = db.Column(db.Integer, db.ForeignKey('event_title.id'))
