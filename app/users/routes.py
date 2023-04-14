from flask import Blueprint, render_template, request, url_for,redirect
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
blueprint = Blueprint('user', __name__)


@blueprint.get('/register_acc')
def get_register_acc():
   return render_template('users/register_acc.html')

@blueprint.post('/register_acc')
def post_register_acc():
  try:
    if request.form.get('password') != request.form.get('password_confirmation'):
        return render_template('users/register_acc.html', error='The password confirmation must match the password.')
    elif User.query.filter_by(email=request.form.get('email')).first():
      return render_template('users/register_acc.html', error='The email adress is already registered')

    user = User(
      email=request.form.get('email'),
      password=generate_password_hash(request.form.get('password'))
    )
    user.save()
    return redirect(url_for('events.events'))
  except Exception as error_meassage:
    error= error_meassage or 'An error ocurred while creating a user. Please make sure to enter valid data'
    return render_template('users/register_acc.html',error=error)

@blueprint.get('/login')
def get_login():
 return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()

    if not user:
      raise Exception('No user with the given email address was found.')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password does not appear to be correct.')
    
    return redirect(url_for('events.events'))
  except Exception as error_message:
    error = error_message or 'An error occured while logging in. Please verify your email and password'
    return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
  return 'User logged out'




