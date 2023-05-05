"""Initial migration

Revision ID: ddc52dd5bbd6
Revises: 
Create Date: 2023-05-05 15:01:56.332040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddc52dd5bbd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pcb_specs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pcb_information', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pcb_specs_id'), 'pcb_specs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pcb_specs_id'), table_name='pcb_specs')
    op.drop_table('pcb_specs')
    # ### end Alembic commands ###