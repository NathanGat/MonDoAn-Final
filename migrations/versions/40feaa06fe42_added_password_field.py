"""added password field

Revision ID: 40feaa06fe42
Revises: 
Create Date: 2021-12-20 06:18:30.520934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40feaa06fe42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
