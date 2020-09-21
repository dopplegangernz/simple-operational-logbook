import uuid
import datetime

from app.main import db
from app.main.model.logEntry import LogEntry
from app.main.model.user import User
from app.main.model.group import Group
import app.main.util.utilFunctions as utilFunctions


def save_log_entry(data):
    groupId = Group.query.filter_by(name=data['group_name']).first().id

    new_entry = LogEntry(
        public_id=str(uuid.uuid4()),
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        subject=data['subject'],
        author_id=data['author_id'],
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


def get_an_entry(public_id):
    return LogEntry.query.filter_by(public_id=public_id).first()


def get_entries_for_date(date):
    dayStart = utilFunctions.startOfLocalDay(date)
    dayEnd = utilFunctions.endOfLocalDay(date)

    return LogEntry.query.filter(
        db.and_(
            LogEntry.timestamp >= dayStart,
            LogEntry.timestamp <= dayEnd
        )
    ).order_by(LogEntry.timestamp.desc()).all()


def get_entries_by_subject(subject):
    return LogEntry.query.filter_by(subject=subject)


def search_entries(searchString):
    pass


def save_changes(data):
    db.session.add(data)
    db.session.commit()
