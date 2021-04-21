"""empty message

Revision ID: 159c749c4cfd
Revises: b8b023c52cfe
Create Date: 2021-04-17 15:17:34.915828

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '159c749c4cfd'
down_revision = 'b8b023c52cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.alter_column('role', 'userID',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_index('userID', table_name='role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('userID', 'role', ['userID'], unique=True)
    op.alter_column('role', 'userID',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_column('role', 'id')
    # ### end Alembic commands ###