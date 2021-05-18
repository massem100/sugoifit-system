"""empty message

Revision ID: b8b023c52cfe
Revises: 8b4a041e4566
Create Date: 2021-04-17 15:09:18.939164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b023c52cfe'
down_revision = '8b4a041e4566'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'role', ['userID'])
    op.create_unique_constraint(None, 'usercredentials', ['userID'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usercredentials', type_='unique')
    op.drop_constraint(None, 'role', type_='unique')
    # ### end Alembic commands ###