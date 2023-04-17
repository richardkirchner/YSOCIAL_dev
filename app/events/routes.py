from flask import Blueprint, Flask, render_template, redirect, url_for, request, current_app
from .models import event
#from app.events.models import event, event_date, event_discription, events
#from .services.create_event import create_event
from app.extensions.database import db
from flask_login import login_required


blueprint = Blueprint('events/',__name__)

@blueprint.route('/events')
def get_events():
  page_number = request.args.get('page', 1, type=int)
  events_pagination = event.query.paginate(page_number, current_app.config['EVENTS_MAX_PER_PAGE'])
  return render_template('events.html', events_pagination=events_pagination)

@blueprint.route('/register', methods=('GET','POST'))
@login_required
def post_events():

  if request.method == 'POST':
    new_event=event(
      name=request.form['event'],
      date=request.form['event_date'],
      desc=request.form['event_discription']
    )
    print(db)
    db.session.add(new_event)
    db.session.commit()
    print("new event is saved", new_event)
    return redirect(url_for('events/.get_events'))
  return render_template('register.html')

# @blueprint.route('/edit_event', methods=('GET','POST'))
# def post_events():

#   if request.method == 'POST':
#     new_event=event(
#       name=request.form['event'],
#       date=request.form['event_date'],
#       desc=request.form['event_discription']
#     )
#     print(db)
#     db.session.add(new_event)
#     db.session.commit()
#     print("new event is saved", new_event)
#     return redirect(url_for('events/.get_events'))
#   return render_template('edit_event.html')

@blueprint.route('/')
def index():
  return render_template('index.html')

@blueprint.route('/register')
def register():
  return render_template('register.html')

def register_blueprint(app: Flask):
   app.register_blueprint(event.routes.blueprint)


