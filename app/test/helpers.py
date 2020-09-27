import json
from app.main import db
from app.main.model.user import User
from app.main.model.group import Group
import datetime


def create_group(self):
    group = Group(
        name='adminGroup',
        description='A group for bootstrapping testing'
    )
    db.session.add(group)
    db.session.commit()

    return group.id


def create_admin_user(self):
    group_id = create_group(self)
    user = User(
        username='admin',
        email='admin@example.com',
        password='admin',
        group_id=group_id,
        admin=True,
        public_id='1',
        registered_on=datetime.datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    return {
        'userId': user.public_id,
        'groupId': group_id,
        'authKey': User.encode_auth_token(user.id)
    }


def create_nonadmin_user(self):
    group_id = create_group(self)
    user = User(
        username='steve',
        email='steve@steve.com',
        password='steve',
        group_id=group_id,
        admin=False,
        registered_on=datetime.datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    return {
        'userId': user.public_id,
        'groupId': group_id,
        'authKey': User.encode_auth_token(user.id)
    }


def get_nonadmin_authKey(self):
    create_nonadmin_user(self)
    # registered user login
    loginResponse = self.client.post(
        '/api/auth/login',
        data=json.dumps(dict(
            email='steve@steve.com',
            password='steve'
        )),
        content_type='application/json'
    )
    return json.loads(loginResponse.data.decode())['Authorization']


def get_admin_authKey(self):
    create_admin_user(self)
    # registered user login
    loginResponse = self.client.post(
        '/api/auth/login',
        data=json.dumps(dict(
            email='admin@example.com',
            password='admin'
        )),
        content_type='application/json'
    )
    return json.loads(loginResponse.data.decode())['Authorization']

# def register_group(self):
#     return self.client.post(
#         '/api/group/',
#         data=json.dumps(dict(
#             name='testGroup',
#             description='A group for testing'
#         )),
#         content_type='application/json'
#     )


# def register_user(self):
#     register_group(self)

#     return self.client.post(
#         '/api/user/',
#         data=json.dumps(dict(
#             email='joe@example.com',
#             username='test username',
#             group='testGroup',
#             password='123456'
#         )),
#         content_type='application/json'
#     )


# def register_user_with_bad_group(self):
#     return self.client.post(
#         '/api/user/',
#         data=json.dumps(dict(
#             email='joe@example.com',
#             username='username',
#             group='nonexistentgroup',
#             password='123456'
#         )),
#         content_type='application/json'
#     )


def create_log_entry(self, authKey, subject, text):
    return self.client.post(
        '/api/entry/',
        headers=dict(
            Authorization=authKey
        ),
        data=json.dumps(dict(
            subject=subject,
            text=text,
            group_name="adminGroup"
        )),
        content_type='application/json'
    )
