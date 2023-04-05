from typing import Tuple

import sqlalchemy as sq
from sqlalchemy.sql import text


from database.db_sync import Base, db_session


class CompanyNews(Base):
    __tablename__: str = 'companies_news'

    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)

    company_id: int = sq.Column(sq.Integer, sq.ForeignKey("companies.id"))
    news_id: int = sq.Column(sq.Integer, sq.ForeignKey("news.id"))

    @classmethod
    def insert(cls, company_id: int, news_id: int):
        if cls.is_in_table(company_id=company_id, news_id=news_id):
            return

        db_session.execute(
            text("""INSERT INTO companies_news (company_id, news_id)
                    VALUES (:company_id, :news_id) 
                    RETURNING *"""),
            params={
                'company_id': company_id,
                'news_id': news_id
            }
        )

        db_session.commit()

    @classmethod
    def is_in_table(cls, company_id: int, news_id: int) -> Tuple:
        return db_session.execute(
            text("""SELECT * FROM companies_news
                    WHERE company_id = :company_id and news_id = :news_id """),
            params={
                'company_id': company_id,
                'news_id': news_id
            }
        ).fetchone()
