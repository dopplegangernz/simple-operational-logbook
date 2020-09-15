import uuid
import datetime

from app.main import db
from app.main.model.group import Group


def save_new_group(data):
    group = Group.query.filter_by(name=data['name']).first()
    if not group:
        new_group = Group(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            description=data['description']
        )
        save_changes(new_group)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Group already exists.',
        }
        return response_object, 409


def get_all_groups():
    return Group.query.all()


def get_a_group(public_id):
    return Group.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
