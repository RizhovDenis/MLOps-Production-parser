import sqlalchemy as sq
from sqlalchemy.sql import text


from database.db_sync import Base, db_session


class Company(Base):
    __tablename__: str = 'companies'

    id: int = sq.Column(sq.Integer, primary_key=True, autoincrement=True, nullable=False)

    name: str = sq.Column(sq.String, nullable=False)
    description: str = sq.Column(sq.String)

    @classmethod
    def insert(cls, name: str, description: str):
        db_session.execute(
            text("""INSERT INTO companies (name, description)
                    VALUES (:name, :description)"""),
            params={
                'name': name,
                'description': description
            }
        )

        db_session.commit()





