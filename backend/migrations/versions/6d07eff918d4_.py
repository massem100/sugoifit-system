"""empty message

Revision ID: 6d07eff918d4
Revises: b13d50832dce
Create Date: 2021-05-16 07:40:57.617967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d07eff918d4'
down_revision = 'b13d50832dce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('prodType', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'prodType')
    # ### end Alembic commands ###
