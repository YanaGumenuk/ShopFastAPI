"""Added category model

Revision ID: 15e0d2b1ce30
Revises: 9051af2fb61e
Create Date: 2023-04-29 08:31:34.550268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e0d2b1ce30'
down_revision = '9051af2fb61e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
