import os
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, Session
from datetime import datetime


Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


# Read the DB URL from an environment variable, fall back to localhost for local dev
DB_URL = os.environ.get(
    "DB_URL", "mysql+pymysql://notes_user:password123@localhost/notes_db"
)

engine = create_engine(DB_URL)

# Create the table if it doesn't exist yet — runs once when the module first loads
Base.metadata.create_all(engine)


def get_all_notes():
    with Session(engine) as session:
        notes = session.query(Note).all()
        return [n.to_dict() for n in notes]


def get_note(note_id):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        return note.to_dict() if note else None


def create_note(content):
    with Session(engine) as session:
        note = Note(content=content)
        session.add(note)
        session.commit()
        session.refresh(note)
        return note.to_dict()


def delete_note(note_id):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        if note is None:
            return False
        session.delete(note)
        session.commit()
        return True
