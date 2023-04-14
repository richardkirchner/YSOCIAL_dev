
from app.app import create_app
from app.events.models import event
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()



event_data = {
  'test event':{'event' :'Hangout at Tempelhoferfeld','event_date': '03062022', 'event_discription': 'some discription'}
}

for slug, event in event_data.items():
  new_event =event(slug=slug, event= event ['event'], event_date= event['event_date'], event_discription=event['event_discription'])
  db.session.add(new_event)

db.session.commit()


# user_data = {
#   'Hans': {'email': 'hans@gmail.com', 'password': 'snahhans'},
#   'Anna': {'email': 'anna@gmail.com', 'password': '1q2w3e4r5t'},
#   'Daria': {'email': 'daria@gmail.com', 'password': 'secretpassword'},
# }
# print(user_data)

# for slug , user in user_data.items():
#   new_user = User(slug=slug, email=user['email'], password=user['password'])
#   print(new_user)
#   db.session.add(new_user)

# db.session.commit()


