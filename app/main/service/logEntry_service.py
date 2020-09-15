import uuid
import datetime

from app.main import db
from app.main.model.logEntry import LogEntry
from app.main.model.user import User
from app.main.model.group import Group


def save_log_entry(data):
    authorId = User.query.filter_by(public_id=data['author_id']).first().id
    groupId = Group.query.filter_by(public_id=data['group_id']).first().id

    new_entry = LogEntry(
        public_id=str(uuid.uuid4()),
        timestamp=datetime.datetime.utcnow(),
        subject=data['subject'],
        author_id=authorId,
        group_id=groupId,
        text=data['text'],
    )
    save_changes(new_entry)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.',
        'id': new_entry.public_id
    }
    return response_object, 201


def get_entries_by_date(date):
    return User.query.all()


def get_entries_by_subject(subject):
    return LogEntry.query.filter_by(subject=subject)


def search_entries(searchString):
    pass


def get_an_entry(public_id):
    return LogEntry.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
