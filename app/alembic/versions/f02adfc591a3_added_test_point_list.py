"""Added Test Point List

Revision ID: f02adfc591a3
Revises: ddc52dd5bbd6
Create Date: 2023-05-05 16:40:58.572154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f02adfc591a3'
down_revision = 'ddc52dd5bbd6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_point_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('net', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('x_coord', sa.String(), nullable=True),
    sa.Column('y_coord', sa.String(), nullable=True),
    sa.Column('side', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('hole_size', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_point_list_id'), 'test_point_list', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_point_list_id'), table_name='test_point_list')
    op.drop_table('test_point_list')
    # ### end Alembic commands ###
