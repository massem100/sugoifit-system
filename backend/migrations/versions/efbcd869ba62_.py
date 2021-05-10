"""empty message

Revision ID: efbcd869ba62
Revises: 850dc5b3979f
Create Date: 2021-05-10 00:24:27.862288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'efbcd869ba62'
down_revision = '850dc5b3979f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'con_service', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'con_service', 'con_service_sale_item', ['cssiID'], ['cssiID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'con_service_sale_item', 'service', ['serviceID'], ['serviceID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('currentasset', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'currentasset', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('currentliability', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'currentliability', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'custorder', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'custorder', 'customer', ['custID'], ['custID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'custorder', 'invoice', ['invoiceID'], ['custID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('equity', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'equity', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.alter_column('financialstmt', 'fs_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.create_unique_constraint(None, 'financialstmt', ['fs_name'])
    op.create_foreign_key(None, 'financialstmtdesc', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'financialstmtdesc', 'financialstmtline', ['fsLineID'], ['lineID'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_index('fstmtID', table_name='financialstmtline')
    op.drop_column('financialstmtline', 'lineDesc')
    op.drop_column('financialstmtline', 'fstmtID')
    op.create_foreign_key(None, 'financialstmtlinealias', 'financialstmtline', ['lineID'], ['lineID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'financialstmtlineseq', 'financialstmtline', ['fsStmtLineID'], ['lineID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'financialstmtlineseq', 'financialstmt', ['fsStmtID'], ['stmtID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'genledger', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'invoice', 'customer', ['custID'], ['custID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'invoice', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'ledgerdetails', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'ledgerdetails', 'genledger', ['ledgerID'], ['ledgerID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('longtermliability', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'longtermliability', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('noncurrentasset', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'noncurrentasset', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('nonopex', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'nonopex', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('nonoprev', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'nonoprev', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('opex', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'opex', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('oprev', sa.Column('tag', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'oprev', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'orderdetails', 'custorder', ['orderID'], ['orderID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('product', sa.Column('avg_lead', sa.Integer(), nullable=True))
    op.add_column('product', sa.Column('longest_lead', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'product_sale_item', 'product', ['prodID'], ['prodID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'product_sale_item', 'customer', ['customerID'], ['custID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receipt', 'custorder', ['orderID'], ['orderID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receipt', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receiptdetails', 'service', ['serviceID'], ['serviceID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receiptdetails', 'receipt', ['receiptID'], ['receiptID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receiptdetails', 'product', ['prodID'], ['prodID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'receiptdetails', 'custorder', ['orderID'], ['orderID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'role', 'usercredentials', ['userID'], ['userID'])
    op.create_foreign_key(None, 'sale', 'customer', ['customerID'], ['custID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'sale', 'receipt', ['receiptID'], ['receiptID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'service', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'service_sale_item', 'service', ['serviceID'], ['serviceID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'service_sale_item', 'user', ['userID'], ['userID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'stock', 'product', ['prodID'], ['prodID'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'usercredentials', 'user', ['userID'], ['userID'])
    op.create_foreign_key(None, 'usercredentials', 'business', ['busID'], ['busID'])
    op.create_foreign_key(None, 'websitedrag', 'websitedetails', ['section_detail'], ['section_detail'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'websitedrag', type_='foreignkey')
    op.drop_constraint(None, 'usercredentials', type_='foreignkey')
    op.drop_constraint(None, 'usercredentials', type_='foreignkey')
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.drop_constraint(None, 'service_sale_item', type_='foreignkey')
    op.drop_constraint(None, 'service_sale_item', type_='foreignkey')
    op.drop_constraint(None, 'service', type_='foreignkey')
    op.drop_constraint(None, 'sale', type_='foreignkey')
    op.drop_constraint(None, 'sale', type_='foreignkey')
    op.drop_constraint(None, 'role', type_='foreignkey')
    op.drop_constraint(None, 'receiptdetails', type_='foreignkey')
    op.drop_constraint(None, 'receiptdetails', type_='foreignkey')
    op.drop_constraint(None, 'receiptdetails', type_='foreignkey')
    op.drop_constraint(None, 'receiptdetails', type_='foreignkey')
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.drop_constraint(None, 'receipt', type_='foreignkey')
    op.drop_constraint(None, 'product_sale_item', type_='foreignkey')
    op.drop_constraint(None, 'product_sale_item', type_='foreignkey')
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'longest_lead')
    op.drop_column('product', 'avg_lead')
    op.drop_constraint(None, 'orderdetails', type_='foreignkey')
    op.drop_constraint(None, 'oprev', type_='foreignkey')
    op.drop_column('oprev', 'tag')
    op.drop_constraint(None, 'opex', type_='foreignkey')
    op.drop_column('opex', 'tag')
    op.drop_constraint(None, 'nonoprev', type_='foreignkey')
    op.drop_column('nonoprev', 'tag')
    op.drop_constraint(None, 'nonopex', type_='foreignkey')
    op.drop_column('nonopex', 'tag')
    op.drop_constraint(None, 'noncurrentasset', type_='foreignkey')
    op.drop_column('noncurrentasset', 'tag')
    op.drop_constraint(None, 'longtermliability', type_='foreignkey')
    op.drop_column('longtermliability', 'tag')
    op.drop_constraint(None, 'ledgerdetails', type_='foreignkey')
    op.drop_constraint(None, 'ledgerdetails', type_='foreignkey')
    op.drop_constraint(None, 'invoice', type_='foreignkey')
    op.drop_constraint(None, 'invoice', type_='foreignkey')
    op.drop_constraint(None, 'genledger', type_='foreignkey')
    op.drop_constraint(None, 'financialstmtlineseq', type_='foreignkey')
    op.drop_constraint(None, 'financialstmtlineseq', type_='foreignkey')
    op.drop_constraint(None, 'financialstmtlinealias', type_='foreignkey')
    op.add_column('financialstmtline', sa.Column('fstmtID', mysql.VARCHAR(length=10), nullable=False))
    op.add_column('financialstmtline', sa.Column('lineDesc', mysql.VARCHAR(length=50), nullable=True))
    op.create_index('fstmtID', 'financialstmtline', ['fstmtID'], unique=True)
    op.drop_constraint(None, 'financialstmtdesc', type_='foreignkey')
    op.drop_constraint(None, 'financialstmtdesc', type_='foreignkey')
    op.drop_constraint(None, 'financialstmt', type_='unique')
    op.alter_column('financialstmt', 'fs_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint(None, 'equity', type_='foreignkey')
    op.drop_column('equity', 'tag')
    op.drop_constraint(None, 'custorder', type_='foreignkey')
    op.drop_constraint(None, 'custorder', type_='foreignkey')
    op.drop_constraint(None, 'custorder', type_='foreignkey')
    op.drop_constraint(None, 'currentliability', type_='foreignkey')
    op.drop_column('currentliability', 'tag')
    op.drop_constraint(None, 'currentasset', type_='foreignkey')
    op.drop_column('currentasset', 'tag')
    op.drop_constraint(None, 'con_service_sale_item', type_='foreignkey')
    op.drop_constraint(None, 'con_service', type_='foreignkey')
    op.drop_constraint(None, 'con_service', type_='foreignkey')
    # ### end Alembic commands ###
