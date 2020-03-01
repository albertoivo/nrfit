"""empty message

Revision ID: 77ad7fbc2eb7
Revises: 99358ba41a7e
Create Date: 2020-03-01 13:59:17.102526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77ad7fbc2eb7'
down_revision = '99358ba41a7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_fitness', sa.Column('distance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data_fitness', 'distance')
    # ### end Alembic commands ###
