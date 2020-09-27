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
            'message': 'Successfully registered.',
            'id': new_group.public_id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Group already exists.',
            'id': group.public_id
        }
        return response_object, 409


def get_all_groups():
    return Group.query.all()


def get_a_group_by_id(public_id):
    return Group.query.filter_by(public_id=public_id).first()


def get_a_group_by_name(group_name):
    return Group.query.filter_by(name=group_name).first()


def update_a_group(group, data):
    group.name = data['name']
    group.description = data['description']

    save_changes(group)
    return group


def save_changes(data):
    db.session.add(data)
    db.session.commit()
