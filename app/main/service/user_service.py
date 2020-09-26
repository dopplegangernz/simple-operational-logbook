import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.group import Group


def save_new_user(data):
    group = Group.query.filter_by(name=data['group']).first()

    user = User.query.filter_by(email=data['email']).first()

    if not group:
        response_object = {
            'status': 'fail',
            'message': '{} is not a valid group name'.format(groupPublicId)
        }
        return response_object, 409
    elif not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            group_id=group.id,
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def update_a_user(user, group, userDetails):
    user.email = userDetails['email']
    user.username = userDetails['username']
    user.group_id = group.id

    if("password" in userDetails):
        user.password = userDetails['password']

    save_changes(user)


def save_changes(data):
    db.session.add(data)
    db.session.commit()
