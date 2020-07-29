"""empty message

Revision ID: e95d0e5c0bad
Revises: 
Create Date: 2020-07-29 13:06:18.484656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e95d0e5c0bad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('featured', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dishes')
    # ### end Alembic commands ###
