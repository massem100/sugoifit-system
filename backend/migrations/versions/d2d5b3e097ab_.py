"""empty message

Revision ID: d2d5b3e097ab
Revises: d55dadab27eb
Create Date: 2021-05-17 23:40:37.097109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2d5b3e097ab'
down_revision = 'd55dadab27eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('sectionID', table_name='websitedrag')
    op.drop_table('websitedrag')
    op.add_column('con_service_sale_item', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_con_service_sale_item_busID'), 'con_service_sale_item', ['busID'], unique=False)
    op.create_foreign_key(None, 'con_service_sale_item', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('customerpayment', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_customerpayment_busID'), 'customerpayment', ['busID'], unique=False)
    op.create_foreign_key(None, 'customerpayment', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('product_sale_item', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_product_sale_item_busID'), 'product_sale_item', ['busID'], unique=False)
    op.create_foreign_key(None, 'product_sale_item', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('sale', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_sale_busID'), 'sale', ['busID'], unique=False)
    op.create_foreign_key(None, 'sale', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('service_sale_item', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_service_sale_item_busID'), 'service_sale_item', ['busID'], unique=False)
    op.create_foreign_key(None, 'service_sale_item', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('stock', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_stock_busID'), 'stock', ['busID'], unique=False)
    op.create_foreign_key(None, 'stock', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    op.add_column('websitedetails', sa.Column('busID', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_websitedetails_busID'), 'websitedetails', ['busID'], unique=False)
    op.create_foreign_key(None, 'websitedetails', 'business', ['busID'], ['busID'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'websitedetails', type_='foreignkey')
    op.drop_index(op.f('ix_websitedetails_busID'), table_name='websitedetails')
    op.drop_column('websitedetails', 'busID')
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.drop_index(op.f('ix_stock_busID'), table_name='stock')
    op.drop_column('stock', 'busID')
    op.drop_constraint(None, 'service_sale_item', type_='foreignkey')
    op.drop_index(op.f('ix_service_sale_item_busID'), table_name='service_sale_item')
    op.drop_column('service_sale_item', 'busID')
    op.drop_constraint(None, 'sale', type_='foreignkey')
    op.drop_index(op.f('ix_sale_busID'), table_name='sale')
    op.drop_column('sale', 'busID')
    op.drop_constraint(None, 'product_sale_item', type_='foreignkey')
    op.drop_index(op.f('ix_product_sale_item_busID'), table_name='product_sale_item')
    op.drop_column('product_sale_item', 'busID')
    op.drop_constraint(None, 'customerpayment', type_='foreignkey')
    op.drop_index(op.f('ix_customerpayment_busID'), table_name='customerpayment')
    op.drop_column('customerpayment', 'busID')
    op.drop_constraint(None, 'con_service_sale_item', type_='foreignkey')
    op.drop_index(op.f('ix_con_service_sale_item_busID'), table_name='con_service_sale_item')
    op.drop_column('con_service_sale_item', 'busID')
    op.create_table('websitedrag',
    sa.Column('sectionID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('positionID', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('sectionName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('section_detail', mysql.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['section_detail'], ['websitedetails.section_detail'], name='websitedrag_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('sectionID'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('sectionID', 'websitedrag', ['sectionID'], unique=True)
    # ### end Alembic commands ###