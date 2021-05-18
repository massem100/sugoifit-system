"""empty message

Revision ID: 8b4a041e4566
Revises: c7becceb8a76
Create Date: 2021-04-17 15:00:53.732186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8b4a041e4566'
down_revision = 'c7becceb8a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('business', 'date_joined',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('role', 'role_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'role_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('business', 'date_joined',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###