"""empty message

Revision ID: 3f84fde3399b
Revises: b93c50f539ba
Create Date: 2021-04-17 15:21:05.411296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f84fde3399b'
down_revision = 'b93c50f539ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userID', sa.String(length=100), nullable=True),
    sa.Column('role_name', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['userID'], ['usercredentials.userID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    # ### end Alembic commands ###
