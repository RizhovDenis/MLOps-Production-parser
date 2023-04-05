from datetime import datetime
from typing import Tuple

import sqlalchemy as sq
from sqlalchemy.sql import text


from database.db_sync import Base, db_session


class News(Base):
    __tablename__: str = 'news'

    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)
    content: str = sq.Column(sq.String)
    title: str = sq.Column(sq.String)
    url: str = sq.Column(sq.String)
    created_at: sq.DateTime = sq.Column(sq.DateTime)

    @classmethod
    def insert(cls, title: str, content: str, created_at: datetime, url: str) -> Tuple:
        news = cls.is_in_table(content=content, title=title, url=url)

        if news:
            return news

        news = db_session.execute(
            text("""INSERT INTO news (content, title, created_at, url)
                    VALUES (:content, :title, :created_at, :url) 
                    RETURNING *"""),
            params={
                'content': content,
                'title': title,
                'created_at': created_at,
                'url': url
            }
        ).fetchone()

        db_session.commit()
        return news

    @classmethod
    def is_in_table(cls, content: str, title: str, url: str) -> Tuple:
        return db_session.execute(
            text("""SELECT * FROM news
                    WHERE (content = :content and title = :title)
                            or url = :url"""),
            params={
                'content': content,
                'title': title,
                'url': url
            }
        ).fetchone()

