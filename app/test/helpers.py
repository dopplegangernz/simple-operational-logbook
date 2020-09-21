import json


def register_group(self):
    return self.client.post(
        '/group/',
        data=json.dumps(dict(
            name='testGroup',
            description='A group for testing'
        )),
        content_type='application/json'
    )


def register_user(self):
    groupResponse = register_group(self)
    groupData = json.loads(groupResponse.data.decode())
    groupId = groupData['id']

    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='joe@example.com',
            username='test username',
            group_id=groupId,
            password='123456'
        )),
        content_type='application/json'
    )


def register_user_with_bad_group(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='joe@example.com',
            username='username',
            group_id='nonexistentgroup',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='joe@example.com',
            password='123456'
        )),
        content_type='application/json'
    )


def create_log_entry(self, authKey, subject, text):
    return self.client.post(
        '/entry/',
        headers=dict(
            Authorization=authKey
        ),
        data=json.dumps(dict(
            subject=subject,
            text=text,
            group_name="testGroup"
        )),
        content_type='application/json'
    )
