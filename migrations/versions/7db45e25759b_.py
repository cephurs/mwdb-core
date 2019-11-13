"""empty message

Revision ID: 7db45e25759b
Revises: c30396dd416a
Create Date: 2019-04-12 18:14:04.169081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7db45e25759b'
down_revision = 'c30396dd416a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('static_config', sa.Column('config_type', sa.String(length=32), server_default='static', nullable=False))
    op.create_index(op.f('ix_static_config_config_type'), 'static_config', ['config_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_static_config_config_type'), table_name='static_config')
    op.drop_column('static_config', 'config_type')
    # ### end Alembic commands ###
