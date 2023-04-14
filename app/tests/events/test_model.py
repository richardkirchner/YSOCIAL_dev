from app.extensions.database import db
from app.events.models import event

# def test_event_update(client):
#     event=event(name='hangout', date='12042023', desc='some desc')
#     db.session.add(event)
#     db.session.commit()

#     event.name = 'hangin'
#     event.save()

#     updated_event = event.query.filter_by(name='hangout').first()
#     assert updated_event.name == 'hangin'

# def test_event_delete(client):
#     event = event(name='sdfgb', date='247189231', desc='sddsfbadgvdg')
#     db.session.add(event)
#     db.session.commit()
#     event.delete()

#     deleted_event = event.query.filter_by(name='sdfgb').first()
#     assert deleted_event is None