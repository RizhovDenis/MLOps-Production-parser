from typing import List

import sqlalchemy as sq
from sqlalchemy.sql import text


from database.db_sync import Base, db_session


class Company(Base):
    __tablename__: str = 'companies'

    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)

    name: str = sq.Column(sq.String, nullable=False)
    description: str = sq.Column(sq.String)
    news_url: str = sq.Column(sq.String, nullable=False)

    @classmethod
    def insert(cls, name: str, description: str, news_url: str):
        db_session.execute(
            text("""INSERT INTO companies (name, description, news_url)
                    VALUES (:name, :description, :news_url)"""),
            params={
                'name': name,
                'description': description,
                'news_url': news_url
            }
        )

        db_session.commit()

    @classmethod
    def get_all(cls) -> List:
        return db_session.execute(
            text("""SELECT * FROM companies""")
        ).fetchall()






