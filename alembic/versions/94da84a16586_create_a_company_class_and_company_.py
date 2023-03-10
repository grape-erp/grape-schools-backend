"""Create a company class and company relationship with users.

Revision ID: 94da84a16586
Revises: 2dcc912a7a35
Create Date: 2023-03-12 16:37:18.910696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94da84a16586'
down_revision = '2dcc912a7a35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('legal_name', sa.String(), nullable=True),
    sa.Column('cnpj', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_cnpj'), 'company', ['cnpj'], unique=False)
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_index(op.f('ix_company_legal_name'), 'company', ['legal_name'], unique=False)
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=False)
    op.add_column('user', sa.Column('company_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'company_id')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_index(op.f('ix_company_legal_name'), table_name='company')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_index(op.f('ix_company_cnpj'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
