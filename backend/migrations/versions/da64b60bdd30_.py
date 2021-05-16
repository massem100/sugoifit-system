"""empty message

Revision ID: da64b60bdd30
Revises: 52ee97e8dcf2
Create Date: 2021-04-23 00:21:48.391592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da64b60bdd30'
down_revision = '52ee97e8dcf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('busID', sa.String(length=100), nullable=False),
    sa.Column('busName', sa.String(length=100), nullable=True),
    sa.Column('busemail', sa.String(length=255), nullable=True),
    sa.Column('busaddress', sa.String(length=100), nullable=True),
    sa.Column('telephone', sa.String(length=100), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('busID'),
    sa.UniqueConstraint('busID')
    )
    op.create_table('customer',
    sa.Column('custID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fname', sa.String(length=100), nullable=True),
    sa.Column('lname', sa.String(length=100), nullable=True),
    sa.Column('trn', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('custID')
    )
    op.create_table('financialstmt',
    sa.Column('stmtID', sa.String(length=10), nullable=False),
    sa.Column('fs_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('stmtID'),
    sa.UniqueConstraint('stmtID')
    )
    op.create_table('user',
    sa.Column('userID', sa.String(length=100), nullable=False),
    sa.Column('fname', sa.String(length=25), nullable=True),
    sa.Column('lname', sa.String(length=25), nullable=True),
    sa.Column('user_address', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('userID'),
    sa.UniqueConstraint('userID')
    )
    op.create_table('websitedetails',
    sa.Column('section_detail', sa.String(length=10), nullable=False),
    sa.Column('sec_header', sa.String(length=50), nullable=True),
    sa.Column('sec_message', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('section_detail'),
    sa.UniqueConstraint('section_detail')
    )
    op.create_table('currentasset',
    sa.Column('caID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('assetName', sa.String(length=100), nullable=True),
    sa.Column('acquisDATE', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('caID')
    )
    op.create_index(op.f('ix_currentasset_busID'), 'currentasset', ['busID'], unique=False)
    op.create_table('currentliability',
    sa.Column('cliabID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('liabName', sa.String(length=100), nullable=True),
    sa.Column('borwDATE', sa.Date(), nullable=True),
    sa.Column('dueDATE', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('cliabID'),
    sa.UniqueConstraint('cliabID')
    )
    op.create_index(op.f('ix_currentliability_busID'), 'currentliability', ['busID'], unique=False)
    op.create_table('equity',
    sa.Column('equityID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('equityName', sa.String(length=100), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('equityID'),
    sa.UniqueConstraint('equityID')
    )
    op.create_index(op.f('ix_equity_busID'), 'equity', ['busID'], unique=False)
    op.create_table('financialstmtline',
    sa.Column('lineID', sa.Integer(), nullable=False),
    sa.Column('fstmtID', sa.String(length=10), nullable=False),
    sa.Column('line_name', sa.String(length=250), nullable=True),
    sa.Column('lineDesc', sa.String(length=50), nullable=True),
    sa.Column('tag', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['fstmtID'], ['financialstmt.stmtID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('lineID'),
    sa.UniqueConstraint('fstmtID'),
    sa.UniqueConstraint('lineID')
    )
    op.create_table('genledger',
    sa.Column('ledgerID', sa.String(length=80), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('Year', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ledgerID')
    )
    op.create_index(op.f('ix_genledger_busID'), 'genledger', ['busID'], unique=False)
    op.create_table('invoice',
    sa.Column('invoiceID', sa.String(length=10), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('custID', sa.Integer(), nullable=True),
    sa.Column('invoice_DATE', sa.Date(), nullable=True),
    sa.Column('tax_tot', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['custID'], ['customer.custID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('invoiceID')
    )
    op.create_index(op.f('ix_invoice_busID'), 'invoice', ['busID'], unique=False)
    op.create_index(op.f('ix_invoice_custID'), 'invoice', ['custID'], unique=False)
    op.create_table('longtermliability',
    sa.Column('LtliabID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('liabName', sa.String(length=100), nullable=True),
    sa.Column('borwDATE', sa.Date(), nullable=True),
    sa.Column('dueDATE', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('LtliabID'),
    sa.UniqueConstraint('LtliabID')
    )
    op.create_index(op.f('ix_longtermliability_busID'), 'longtermliability', ['busID'], unique=False)
    op.create_table('noncurrentasset',
    sa.Column('ncaID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('assetName', sa.String(length=100), nullable=True),
    sa.Column('lifeSpan', sa.Integer(), nullable=True),
    sa.Column('accumDep', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('disposalAmt', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('depType', sa.String(length=100), nullable=True),
    sa.Column('acquisDATE', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ncaID')
    )
    op.create_index(op.f('ix_noncurrentasset_busID'), 'noncurrentasset', ['busID'], unique=False)
    op.create_table('nonopex',
    sa.Column('nOpexID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('nOpexName', sa.String(length=100), nullable=True),
    sa.Column('dateIncurred', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nOpexID'),
    sa.UniqueConstraint('nOpexID')
    )
    op.create_index(op.f('ix_nonopex_busID'), 'nonopex', ['busID'], unique=False)
    op.create_table('nonoprev',
    sa.Column('nopRevenueID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('nOprevName', sa.String(length=100), nullable=True),
    sa.Column('dateEarned', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nopRevenueID'),
    sa.UniqueConstraint('nopRevenueID')
    )
    op.create_index(op.f('ix_nonoprev_busID'), 'nonoprev', ['busID'], unique=False)
    op.create_table('opex',
    sa.Column('opexID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('opexName', sa.String(length=100), nullable=True),
    sa.Column('dateIncurred', sa.Date(), nullable=True),
    sa.Column('expenseCategory', sa.String(length=80), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('opexID'),
    sa.UniqueConstraint('opexID')
    )
    op.create_index(op.f('ix_opex_busID'), 'opex', ['busID'], unique=False)
    op.create_table('oprev',
    sa.Column('opRevenueID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('oprevName', sa.String(length=100), nullable=True),
    sa.Column('dateEarned', sa.Date(), nullable=True),
    sa.Column('related_entry', sa.String(length=50), nullable=True),
    sa.Column('debitBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('creditBalance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Balance', sa.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('BalanceDC', sa.Enum('Debit', 'Credit'), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('opRevenueID'),
    sa.UniqueConstraint('opRevenueID')
    )
    op.create_index(op.f('ix_oprev_busID'), 'oprev', ['busID'], unique=False)
    op.create_table('product',
    sa.Column('prodID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('prodName', sa.String(length=100), nullable=True),
    sa.Column('unit_price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('Unit', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('limitedTime', sa.DateTime(), nullable=True),
    sa.Column('taxPercent', sa.DECIMAL(precision=3, scale=2), nullable=True),
    sa.Column('prodStatus', sa.String(length=25), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('prodID')
    )
    op.create_index(op.f('ix_product_busID'), 'product', ['busID'], unique=False)
    op.create_table('service',
    sa.Column('serviceID', sa.String(length=11), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('serv_name', sa.String(length=11), nullable=True),
    sa.Column('serv_cost', sa.Integer(), nullable=True),
    sa.Column('taxPercent', sa.DECIMAL(precision=3, scale=2), nullable=True),
    sa.Column('in_season', sa.String(length=11), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('serviceID')
    )
    op.create_index(op.f('ix_service_busID'), 'service', ['busID'], unique=False)
    op.create_table('usercredentials',
    sa.Column('cid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userID', sa.String(length=100), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('user_email', sa.String(length=50), nullable=True),
    sa.Column('user_password', sa.String(length=255), nullable=True),
    sa.Column('busID', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('cid'),
    sa.UniqueConstraint('userID'),
    sa.UniqueConstraint('user_email')
    )
    op.create_table('websitedrag',
    sa.Column('sectionID', sa.Integer(), nullable=False),
    sa.Column('positionID', sa.String(length=50), nullable=True),
    sa.Column('sectionName', sa.String(length=50), nullable=True),
    sa.Column('section_detail', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['section_detail'], ['websitedetails.section_detail'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('sectionID'),
    sa.UniqueConstraint('sectionID')
    )
    op.create_table('con_service_sale_item',
    sa.Column('cssiID', sa.String(length=11), nullable=False),
    sa.Column('quantitySold', sa.Integer(), nullable=True),
    sa.Column('unit_price', sa.Integer(), nullable=True),
    sa.Column('serv_price', sa.Integer(), nullable=True),
    sa.Column('taxAmt', sa.Integer(), nullable=True),
    sa.Column('serviceID', sa.String(length=11), nullable=True),
    sa.Column('starttime', sa.DateTime(), nullable=True),
    sa.Column('endtime', sa.DateTime(), nullable=True),
    sa.Column('prolong_period', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['serviceID'], ['service.serviceID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('cssiID')
    )
    op.create_index(op.f('ix_con_service_sale_item_serviceID'), 'con_service_sale_item', ['serviceID'], unique=False)
    op.create_table('custorder',
    sa.Column('orderID', sa.String(length=10), nullable=False),
    sa.Column('order_tot', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('order_DATE', sa.Date(), nullable=True),
    sa.Column('custID', sa.Integer(), nullable=True),
    sa.Column('invoiceID', sa.Integer(), nullable=True),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['custID'], ['customer.custID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['invoiceID'], ['invoice.custID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('orderID')
    )
    op.create_index(op.f('ix_custorder_busID'), 'custorder', ['busID'], unique=False)
    op.create_index(op.f('ix_custorder_custID'), 'custorder', ['custID'], unique=False)
    op.create_index(op.f('ix_custorder_invoiceID'), 'custorder', ['invoiceID'], unique=False)
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
    sa.Column('fsStmtID', sa.String(length=10), nullable=False),
    sa.Column('fsStmtLineID', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fsStmtID'], ['financialstmt.stmtID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['fsStmtLineID'], ['financialstmtline.lineID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('lineSeqID'),
    sa.UniqueConstraint('fsStmtID', 'fsStmtLineID')
    )
    op.create_index(op.f('ix_financialstmtlineseq_fsStmtID'), 'financialstmtlineseq', ['fsStmtID'], unique=False)
    op.create_index(op.f('ix_financialstmtlineseq_fsStmtLineID'), 'financialstmtlineseq', ['fsStmtLineID'], unique=False)
    op.create_table('ledgerdetails',
    sa.Column('ledgerDetailsID', sa.Integer(), nullable=False),
    sa.Column('ledgerID', sa.String(length=80), nullable=True),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('accountName', sa.String(length=250), nullable=True),
    sa.Column('accountBalance', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ledgerID'], ['genledger.ledgerID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ledgerDetailsID')
    )
    op.create_index(op.f('ix_ledgerdetails_busID'), 'ledgerdetails', ['busID'], unique=False)
    op.create_index(op.f('ix_ledgerdetails_ledgerID'), 'ledgerdetails', ['ledgerID'], unique=False)
    op.create_table('product_sale_item',
    sa.Column('psiID', sa.Integer(), nullable=False),
    sa.Column('customerID', sa.Integer(), nullable=True),
    sa.Column('timePaid', sa.DateTime(), nullable=True),
    sa.Column('timeCreated', sa.DateTime(), nullable=True),
    sa.Column('saleAmt', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('saleAmtPaid', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('SaleStatus', sa.String(length=25), nullable=True),
    sa.Column('quantitySold', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('unit_price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('prodID', sa.Integer(), nullable=True),
    sa.Column('taxAmt', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['customerID'], ['customer.custID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['prodID'], ['product.prodID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('psiID')
    )
    op.create_index(op.f('ix_product_sale_item_customerID'), 'product_sale_item', ['customerID'], unique=False)
    op.create_index(op.f('ix_product_sale_item_prodID'), 'product_sale_item', ['prodID'], unique=False)
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userID', sa.String(length=100), nullable=True),
    sa.Column('role_name', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['userID'], ['usercredentials.userID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_sale_item',
    sa.Column('ssiID', sa.String(length=11), nullable=False),
    sa.Column('serv_price', sa.Integer(), nullable=True),
    sa.Column('taxAmt', sa.Integer(), nullable=True),
    sa.Column('serviceID', sa.String(length=11), nullable=True),
    sa.Column('userID', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['serviceID'], ['service.serviceID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ssiID')
    )
    op.create_index(op.f('ix_service_sale_item_serviceID'), 'service_sale_item', ['serviceID'], unique=False)
    op.create_index(op.f('ix_service_sale_item_userID'), 'service_sale_item', ['userID'], unique=False)
    op.create_table('stock',
    sa.Column('prodID', sa.Integer(), nullable=False),
    sa.Column('inStock', sa.String(length=10), nullable=True),
    sa.Column('lastUpdateTime', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('threshold', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prodID'], ['product.prodID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('prodID')
    )
    op.create_table('con_service',
    sa.Column('serviceID', sa.String(length=11), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('serv_name', sa.String(length=11), nullable=True),
    sa.Column('serv_uprice', sa.Integer(), nullable=True),
    sa.Column('basic_unit', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('d_prolongperiod', sa.DateTime(), nullable=True),
    sa.Column('taxPercent', sa.DECIMAL(precision=3, scale=2), nullable=True),
    sa.Column('in_season', sa.String(length=11), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.Column('cssiID', sa.String(length=11), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['cssiID'], ['con_service_sale_item.cssiID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('serviceID')
    )
    op.create_index(op.f('ix_con_service_busID'), 'con_service', ['busID'], unique=False)
    op.create_index(op.f('ix_con_service_cssiID'), 'con_service', ['cssiID'], unique=False)
    op.create_table('orderdetails',
    sa.Column('orderID', sa.String(length=10), nullable=False),
    sa.Column('detailsID', sa.String(length=10), nullable=False),
    sa.Column('prodID', sa.String(length=10), nullable=True),
    sa.Column('serviceID', sa.String(length=10), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_tot', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['orderID'], ['custorder.orderID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('orderID', 'detailsID')
    )
    op.create_table('receipt',
    sa.Column('receiptID', sa.String(length=10), nullable=False),
    sa.Column('orderID', sa.String(length=10), nullable=True),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('DATE_issued', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['orderID'], ['custorder.orderID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('receiptID')
    )
    op.create_index(op.f('ix_receipt_busID'), 'receipt', ['busID'], unique=False)
    op.create_index(op.f('ix_receipt_orderID'), 'receipt', ['orderID'], unique=False)
    op.create_table('receiptdetails',
    sa.Column('receiptID', sa.String(length=10), nullable=False),
    sa.Column('rdetailsID', sa.String(length=10), nullable=False),
    sa.Column('orderID', sa.String(length=10), nullable=True),
    sa.Column('prodID', sa.Integer(), nullable=True),
    sa.Column('serviceID', sa.String(length=11), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_tot', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['orderID'], ['custorder.orderID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['prodID'], ['product.prodID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['receiptID'], ['receipt.receiptID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['serviceID'], ['service.serviceID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('rdetailsID'),
    sa.UniqueConstraint('receiptID')
    )
    op.create_index(op.f('ix_receiptdetails_orderID'), 'receiptdetails', ['orderID'], unique=False)
    op.create_index(op.f('ix_receiptdetails_prodID'), 'receiptdetails', ['prodID'], unique=False)
    op.create_index(op.f('ix_receiptdetails_serviceID'), 'receiptdetails', ['serviceID'], unique=False)
    op.create_table('sale',
    sa.Column('saleID', sa.String(length=11), nullable=False),
    sa.Column('customerID', sa.Integer(), nullable=True),
    sa.Column('timePaid', sa.DateTime(), nullable=True),
    sa.Column('timeCreated', sa.DateTime(), nullable=True),
    sa.Column('saleAmt', sa.Integer(), nullable=True),
    sa.Column('saleAmtPaid', sa.Integer(), nullable=True),
    sa.Column('SaleStatus', sa.String(length=11), nullable=True),
    sa.Column('receiptID', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['customerID'], ['customer.custID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['receiptID'], ['receipt.receiptID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('saleID')
    )
    op.create_index(op.f('ix_sale_customerID'), 'sale', ['customerID'], unique=False)
    op.create_index(op.f('ix_sale_receiptID'), 'sale', ['receiptID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sale_receiptID'), table_name='sale')
    op.drop_index(op.f('ix_sale_customerID'), table_name='sale')
    op.drop_table('sale')
    op.drop_index(op.f('ix_receiptdetails_serviceID'), table_name='receiptdetails')
    op.drop_index(op.f('ix_receiptdetails_prodID'), table_name='receiptdetails')
    op.drop_index(op.f('ix_receiptdetails_orderID'), table_name='receiptdetails')
    op.drop_table('receiptdetails')
    op.drop_index(op.f('ix_receipt_orderID'), table_name='receipt')
    op.drop_index(op.f('ix_receipt_busID'), table_name='receipt')
    op.drop_table('receipt')
    op.drop_table('orderdetails')
    op.drop_index(op.f('ix_con_service_cssiID'), table_name='con_service')
    op.drop_index(op.f('ix_con_service_busID'), table_name='con_service')
    op.drop_table('con_service')
    op.drop_table('stock')
    op.drop_index(op.f('ix_service_sale_item_userID'), table_name='service_sale_item')
    op.drop_index(op.f('ix_service_sale_item_serviceID'), table_name='service_sale_item')
    op.drop_table('service_sale_item')
    op.drop_table('role')
    op.drop_index(op.f('ix_product_sale_item_prodID'), table_name='product_sale_item')
    op.drop_index(op.f('ix_product_sale_item_customerID'), table_name='product_sale_item')
    op.drop_table('product_sale_item')
    op.drop_index(op.f('ix_ledgerdetails_ledgerID'), table_name='ledgerdetails')
    op.drop_index(op.f('ix_ledgerdetails_busID'), table_name='ledgerdetails')
    op.drop_table('ledgerdetails')
    op.drop_index(op.f('ix_financialstmtlineseq_fsStmtLineID'), table_name='financialstmtlineseq')
    op.drop_index(op.f('ix_financialstmtlineseq_fsStmtID'), table_name='financialstmtlineseq')
    op.drop_table('financialstmtlineseq')
    op.drop_table('financialstmtlinealias')
    op.drop_table('financialstmtdesc')
    op.drop_index(op.f('ix_custorder_invoiceID'), table_name='custorder')
    op.drop_index(op.f('ix_custorder_custID'), table_name='custorder')
    op.drop_index(op.f('ix_custorder_busID'), table_name='custorder')
    op.drop_table('custorder')
    op.drop_index(op.f('ix_con_service_sale_item_serviceID'), table_name='con_service_sale_item')
    op.drop_table('con_service_sale_item')
    op.drop_table('websitedrag')
    op.drop_table('usercredentials')
    op.drop_index(op.f('ix_service_busID'), table_name='service')
    op.drop_table('service')
    op.drop_index(op.f('ix_product_busID'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_oprev_busID'), table_name='oprev')
    op.drop_table('oprev')
    op.drop_index(op.f('ix_opex_busID'), table_name='opex')
    op.drop_table('opex')
    op.drop_index(op.f('ix_nonoprev_busID'), table_name='nonoprev')
    op.drop_table('nonoprev')
    op.drop_index(op.f('ix_nonopex_busID'), table_name='nonopex')
    op.drop_table('nonopex')
    op.drop_index(op.f('ix_noncurrentasset_busID'), table_name='noncurrentasset')
    op.drop_table('noncurrentasset')
    op.drop_index(op.f('ix_longtermliability_busID'), table_name='longtermliability')
    op.drop_table('longtermliability')
    op.drop_index(op.f('ix_invoice_custID'), table_name='invoice')
    op.drop_index(op.f('ix_invoice_busID'), table_name='invoice')
    op.drop_table('invoice')
    op.drop_index(op.f('ix_genledger_busID'), table_name='genledger')
    op.drop_table('genledger')
    op.drop_table('financialstmtline')
    op.drop_index(op.f('ix_equity_busID'), table_name='equity')
    op.drop_table('equity')
    op.drop_index(op.f('ix_currentliability_busID'), table_name='currentliability')
    op.drop_table('currentliability')
    op.drop_index(op.f('ix_currentasset_busID'), table_name='currentasset')
    op.drop_table('currentasset')
    op.drop_table('websitedetails')
    op.drop_table('user')
    op.drop_table('financialstmt')
    op.drop_table('customer')
    op.drop_table('business')
    # ### end Alembic commands ###
