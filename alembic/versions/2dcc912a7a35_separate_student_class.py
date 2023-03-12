"""Separate Student class.

Revision ID: 2dcc912a7a35
Revises: 5d4f2cdb96a2
Create Date: 2023-03-12 16:27:04.163744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dcc912a7a35'
down_revision = '5d4f2cdb96a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=False)
    op.create_index(op.f('ix_student_last_name'), 'student', ['last_name'], unique=False)
    op.create_index(op.f('ix_student_name'), 'student', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_name'), table_name='student')
    op.drop_index(op.f('ix_student_last_name'), table_name='student')
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###