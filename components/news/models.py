from datetime import datetime

import sqlalchemy as sq
from sqlalchemy.sql import text


from database.db_sync import Base, db_session


class News(Base):
    __tablename__: str = 'news'

    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)
    content: str = sq.Column(sq.String)
    title: str = sq.Column(sq.String)
    created_at: sq.DateTime = sq.Column(sq.DateTime)
    company_id: int = sq.Column(sq.Integer, sq.ForeignKey("companies.id"))

    @classmethod
    def insert(cls, title: str, content: str, created_at: datetime, company_id: int):
        db_session.execute(
            text("""INSERT INTO news (content, title, created_at, company_id)
                    VALUES (:content, :title, :created_id, :company_id) """),
            params={
                'content': content,
                'title': title,
                'created_at': created_at,
                'company_id': company_id
            }
        )

