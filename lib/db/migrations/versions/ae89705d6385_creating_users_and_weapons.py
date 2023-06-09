"""creating users and weapons

Revision ID: ae89705d6385
Revises: dc8ae8f65c96
Create Date: 2023-03-25 18:05:18.028719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae89705d6385'
down_revision = 'dc8ae8f65c96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weapons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('strength', sa.Integer(), nullable=True),
    sa.Column('wall_breaker', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('score', sa.String(), nullable=True),
    sa.Column('weapon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['weapon_id'], ['weapons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('weapons')
    # ### end Alembic commands ###
