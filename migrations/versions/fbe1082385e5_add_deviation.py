"""add deviation

Revision ID: fbe1082385e5
Revises: 2f385a39f5d4
Create Date: 2024-11-09 01:49:13.526970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe1082385e5'
down_revision = '2f385a39f5d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jurnal_umum', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deviation', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jurnal_umum', schema=None) as batch_op:
        batch_op.drop_column('deviation')

    # ### end Alembic commands ###