
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt


class LogEntry(db.Model):
    """ Log entry Model """
    __tablename__ = "log_entries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    author_id = db.Column(db.String(50), db.ForeignKey(
        'user.id'), nullable=False)
    author = db.relationship("User")
    group_id = db.Column(db.String(50), db.ForeignKey(
        'group.id'), nullable=False)
    group = db.relationship("Group")
    text = db.colum(db.String(), nullable=False)

    def __repr__(self):
        return "<LogEntry '{} - {}'>".format(self.subject, self.text)
