"""empty message

Revision ID: 0762c359a972
Revises: 94ef98ced171
Create Date: 2021-04-22 13:58:56.726191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0762c359a972'
down_revision = '94ef98ced171'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('prodID', sa.Integer(), nullable=False),
    sa.Column('busID', sa.String(length=100), nullable=True),
    sa.Column('prodName', sa.String(length=100), nullable=True),
    sa.Column('unit_price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('Unit', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('limitedTime', sa.DateTime(), nullable=True),
    sa.Column('taxPercent', sa.DECIMAL(precision=3, scale=2), nullable=True),
    sa.Column('grade', sa.String(length=5), nullable=True),
    sa.Column('prodStatus', sa.String(length=25), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['busID'], ['business.busID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('prodID')
    )
    op.create_index(op.f('ix_product_busID'), 'product', ['busID'], unique=False)
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
    op.create_table('stock',
    sa.Column('prodID', sa.Integer(), nullable=False),
    sa.Column('inStock', sa.String(length=10), nullable=True),
    sa.Column('lastUpdateTime', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('threshold', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prodID'], ['product.prodID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('prodID')
    )
    op.create_table('receiptdetails',
    sa.Column('receiptID', sa.Integer(), nullable=False),
    sa.Column('rdetailsID', sa.Integer(), nullable=False),
    sa.Column('orderID', sa.Integer(), nullable=True),
    sa.Column('prodID', sa.Integer(), nullable=True),
    sa.Column('serviceID', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_tot', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['orderID'], ['order.orderID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['prodID'], ['product.prodID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['receiptID'], ['receipt.receiptID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['serviceID'], ['service.serviceID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('rdetailsID'),
    sa.UniqueConstraint('receiptID')
    )
    op.create_index(op.f('ix_receiptdetails_orderID'), 'receiptdetails', ['orderID'], unique=False)
    op.create_index(op.f('ix_receiptdetails_prodID'), 'receiptdetails', ['prodID'], unique=False)
    op.create_index(op.f('ix_receiptdetails_serviceID'), 'receiptdetails', ['serviceID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_receiptdetails_serviceID'), table_name='receiptdetails')
    op.drop_index(op.f('ix_receiptdetails_prodID'), table_name='receiptdetails')
    op.drop_index(op.f('ix_receiptdetails_orderID'), table_name='receiptdetails')
    op.drop_table('receiptdetails')
    op.drop_table('stock')
    op.drop_index(op.f('ix_product_sale_item_prodID'), table_name='product_sale_item')
    op.drop_index(op.f('ix_product_sale_item_customerID'), table_name='product_sale_item')
    op.drop_table('product_sale_item')
    op.drop_index(op.f('ix_product_busID'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
