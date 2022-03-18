"""empty message

Revision ID: fc00efd5467c
Revises: 
Create Date: 2022-03-17 18:55:55.018999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc00efd5467c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('propertylistings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('numroom', sa.Integer(), nullable=True),
    sa.Column('numbath', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('property_type', sa.String(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('propertylistings')
    # ### end Alembic commands ###