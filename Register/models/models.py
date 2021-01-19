# -*- coding: utf-8 -*-
from datetime import datetime
from Register.database import db


class Message(db.Model):

    __tablename__ = 'message'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    line_user_id=db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<message_id = {message_id}, line_user_id = {line_user_id}, message = {message}>'.format(
            message_id=self.message_id,
            line_user_id=self.line_user_id,
            message=self.message
        )
