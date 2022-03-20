"""empty message

Revision ID: 0ee0cf25ca69
Revises: 
Create Date: 2022-03-19 20:52:22.442423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ee0cf25ca69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('propertylist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('numroom', sa.Integer(), nullable=False),
    sa.Column('numbath', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('property_type', sa.String(length=20), nullable=False),
    sa.Column('location', sa.Text(), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('propertylist')
    # ### end Alembic commands ###