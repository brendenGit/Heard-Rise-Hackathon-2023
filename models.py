"""Models for heard app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Employee(db.Model):
    """Employee model"""

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    submissions = db.relationship('Submission', backref='employee')


class Submission(db.Model):
    """Submission model"""

    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submission_start = db.Column(db.String, nullable=False)
    prompt_1 = db.Column(db.String)
    prompt_1_resp = db.Column(db.String)
    prompt_2 = db.Column(db.String)
    prompt_2_resp = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'employees.id'), nullable=False)


class Team(db.Model):
    """Team model"""

    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    employees = db.relationship('Employee', backref='team')
