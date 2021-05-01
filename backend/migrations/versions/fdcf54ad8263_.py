"""empty message

Revision ID: fdcf54ad8263
Revises: 4284dbef474e
Create Date: 2021-04-29 17:09:00.418662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdcf54ad8263'
down_revision = '4284dbef474e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('financialstmt',
    sa.Column('stmtID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fs_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('stmtID'),
    sa.UniqueConstraint('fs_name'),
    sa.UniqueConstraint('stmtID')
    )
    op.create_table('financialstmtline',
    sa.Column('lineID', sa.Integer(), nullable=False),
    sa.Column('fstmtID', sa.Integer(), nullable=False),
    sa.Column('line_name', sa.String(length=250), nullable=True),
    sa.Column('lineDesc', sa.String(length=50), nullable=True),
    sa.Column('tag', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['fstmtID'], ['financialstmt.stmtID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('lineID'),
    sa.UniqueConstraint('fstmtID'),
    sa.UniqueConstraint('lineID')
    )
    op.create_table('financialstmtdesc',
    sa.Column('fStmtDescID', sa.Integer(), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=False),
    sa.Column('fsLineID', sa.Integer(), nullable=False),
    sa.Column('fiscalYear', sa.Integer(), nullable=True),
    sa.Column('fiscalPeriod', sa.Date(), nullable=True),
    sa.Column('fillingDATE', sa.Date(), nullable=True),
    sa.Column('startDATE', sa.Date(), nullable=True),
    sa.Column('endDATE', sa.Date(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['fsLineID'], ['financialstmtline.lineID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('fStmtDescID'),
    sa.UniqueConstraint('busID'),
    sa.UniqueConstraint('busID', 'fsLineID', 'fiscalYear', 'fiscalPeriod'),
    sa.UniqueConstraint('fStmtDescID'),
    sa.UniqueConstraint('fsLineID')
    )
    op.create_table('financialstmtlinealias',
    sa.Column('aliasID', sa.Integer(), nullable=False),
    sa.Column('lineID', sa.Integer(), nullable=False),
    sa.Column('lineAlias', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['lineID'], ['financialstmtline.lineID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('aliasID'),
    sa.UniqueConstraint('aliasID'),
    sa.UniqueConstraint('lineAlias')
    )
    op.create_table('financialstmtlineseq',
    sa.Column('lineSeqID', sa.Integer(), nullable=False),
    sa.Column('fsStmtID', sa.Integer(), nullable=False),
    sa.Column('fsStmtLineID', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fsStmtID'], ['financialstmt.stmtID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['fsStmtLineID'], ['financialstmtline.lineID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('lineSeqID'),
    sa.UniqueConstraint('fsStmtID', 'fsStmtLineID')
    )
    op.create_index(op.f('ix_financialstmtlineseq_fsStmtID'), 'financialstmtlineseq', ['fsStmtID'], unique=False)
    op.create_index(op.f('ix_financialstmtlineseq_fsStmtLineID'), 'financialstmtlineseq', ['fsStmtLineID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_financialstmtlineseq_fsStmtLineID'), table_name='financialstmtlineseq')
    op.drop_index(op.f('ix_financialstmtlineseq_fsStmtID'), table_name='financialstmtlineseq')
    op.drop_table('financialstmtlineseq')
    op.drop_table('financialstmtlinealias')
    op.drop_table('financialstmtdesc')
    op.drop_table('financialstmtline')
    op.drop_table('financialstmt')
    # ### end Alembic commands ###
