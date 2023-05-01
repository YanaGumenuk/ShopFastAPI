"""Added order and item models

Revision ID: 49c9a560808c
Revises: fcf441ca28d0
Create Date: 2023-05-01 08:47:17.288589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c9a560808c'
down_revision = 'fcf441ca28d0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('telephone', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_email'), 'order', ['email'], unique=False)
    op.create_index(op.f('ix_order_full_name'), 'order', ['full_name'], unique=False)
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('price', sa.Numeric(precision=8), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_index(op.f('ix_order_full_name'), table_name='order')
    op.drop_index(op.f('ix_order_email'), table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###