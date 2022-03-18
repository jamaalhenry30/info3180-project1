"""empty message

Revision ID: 86bd2ffe825c
Revises: fc00efd5467c
Create Date: 2022-03-17 20:17:38.075321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86bd2ffe825c'
down_revision = 'fc00efd5467c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('propertylistings', sa.Column('photo', sa.String(length=255), nullable=True))
    op.drop_column('propertylistings', 'filename')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('propertylistings', sa.Column('filename', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('propertylistings', 'photo')
    # ### end Alembic commands ###