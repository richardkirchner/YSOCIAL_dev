from flask import Blueprint, Flask, render_template, redirect, url_for, request, current_app
from .models import event
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

@blueprint.post('/register/delete')
@login_required
def delete_event():
  event_id = request.form['event_id']
  print(event_id)
  event_to_delete = event.query.filter_by(id=event_id).first()
  print(event_to_delete)
  db.session.delete(event_to_delete)
  db.session.commit()

  return redirect('/events')


@blueprint.route('/edit_event/<id>', methods=('GET','POST'))
def post_events_edit(id):
  if request.method == 'POST':
    update_event=event.query.filter_by(id=id).first()

    update_event.name=request.form['event']
    update_event.date=int(request.form['event_date']) 
    update_event.desc=request.form['event_discription']

    db.session.add(update_event)
    db.session.commit()

    print("new event is saved", update_event)
    return redirect(url_for('events/.get_events'))
  print(id)
  curr_event = event.query.filter_by(id=id).first()
  return render_template('edit_event.html', event=curr_event)

@blueprint.route('/')
def index():
  return render_template('index.html')
