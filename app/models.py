from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    assistants = db.relationship('Assistant', backref='creator', lazy='dynamic')
    threads = db.relationship('Thread', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Assistant(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(500))
    instructions = db.Column(db.Text)
    model = db.Column(db.String(64), default="gpt-4o")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    files = db.relationship('File', backref='assistant', lazy='dynamic')
    threads = db.relationship('Thread', backref='assistant', lazy='dynamic')

    def __repr__(self):
        return f'<Assistant {self.name}>'


class File(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    filename = db.Column(db.String(256))
    purpose = db.Column(db.String(64), default="assistants")
    file_type = db.Column(db.String(64))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    local_path = db.Column(db.String(512))
    assistant_id = db.Column(db.String(128), db.ForeignKey('assistant.id'))

    def __repr__(self):
        return f'<File {self.filename}>'


class Thread(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    title = db.Column(db.String(128), default="New Thread")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    assistant_id = db.Column(db.String(128), db.ForeignKey('assistant.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    messages = db.relationship('Message', backref='thread', lazy='dynamic')

    def __repr__(self):
        return f'<Thread {self.id}>'


class Message(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    role = db.Column(db.String(20))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    thread_id = db.Column(db.String(128), db.ForeignKey('thread.id'))
    
    def __repr__(self):
        return f'<Message {self.id}>'
