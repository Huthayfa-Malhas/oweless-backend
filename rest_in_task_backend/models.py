from .db import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from werkzeug.security import check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(db.String(100))
    last_name: Mapped[str] = mapped_column(db.String(100))
    date_of_birth: Mapped[str] = mapped_column(db.Date)
    gender: Mapped[str] = mapped_column(db.String(10))
    created_at: Mapped[str] = mapped_column(db.DateTime, default=db.func.now())
    updated_at: Mapped[str] = mapped_column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(db.Boolean, default=False)
    role: Mapped[str] = mapped_column(db.String(50), default='user')
    last_login_at: Mapped[str] = mapped_column(db.DateTime)
    failed_login_attempts: Mapped[int] = mapped_column(db.Integer, default=0)

    tasks: Mapped[List["Task"]] = db.relationship('Task', back_populates='user')

    __table_args__ = (
        db.CheckConstraint("email LIKE '%@%'", name='chk_email'),
    )

    def check_password(self, password, password_hash):
        return check_password_hash(password_hash, password)

class Task(db.Model):
    __tablename__ = 'tasks'

    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[str] = mapped_column(default='pending') # pending, complete
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'))
    user: Mapped["User"] = db.relationship('User', back_populates='tasks')
    created_at: Mapped[str] = mapped_column(db.DateTime, default=db.func.now())
    updated_at: Mapped[str] = mapped_column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
