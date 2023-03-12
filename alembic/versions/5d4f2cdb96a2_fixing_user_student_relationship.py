"""Fixing User Student Relationship

Revision ID: 5d4f2cdb96a2
Revises: d39af4278ae5
Create Date: 2023-03-12 16:24:57.866204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4f2cdb96a2'
down_revision = 'd39af4278ae5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_student_id', table_name='student')
    op.drop_index('ix_student_last_name', table_name='student')
    op.drop_index('ix_student_name', table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='student_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='student_pkey')
    )
    op.create_index('ix_student_name', 'student', ['name'], unique=False)
    op.create_index('ix_student_last_name', 'student', ['last_name'], unique=False)
    op.create_index('ix_student_id', 'student', ['id'], unique=False)
    # ### end Alembic commands ###
