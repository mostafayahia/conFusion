"""empty message

Revision ID: cc7d23137bf2
Revises: 740472a87f5b
Create Date: 2020-08-04 19:57:55.960244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc7d23137bf2'
down_revision = '740472a87f5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
