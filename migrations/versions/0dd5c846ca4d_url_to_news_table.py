"""url to news table

Revision ID: 0dd5c846ca4d
Revises: 2161a56dc688
Create Date: 2023-04-05 20:32:30.299607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dd5c846ca4d'
down_revision = '2161a56dc688'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'url')
    # ### end Alembic commands ###