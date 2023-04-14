from flask import Blueprint, jsonify, request
from .services.serialize_events import serialize_events
from app.events.models import event
from os import environ


blueprint = Blueprint('api',__name__)

@blueprint.get('/api/v1/events')
def events():
    if environ.get('API_KEY') == request.header.get('X-API-KEY'):
        events=event.query.all()

        return jsonify(
         serialize_events(events)
        )
    else:
        return jsonify({'error': 'Invalid API key'}), 401

def serialize_events(events):
     events_list = []

     for event in events:
        events_list.append({
            'id' : event.id,
            'event': {
                'name': event.name,
                'date': event.date,
                'desc': event.desc,
            }
        })
     return events_list