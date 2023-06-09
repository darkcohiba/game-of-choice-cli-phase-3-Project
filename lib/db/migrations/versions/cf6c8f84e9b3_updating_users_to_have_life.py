"""updating users to have life

Revision ID: cf6c8f84e9b3
Revises: ae89705d6385
Create Date: 2023-03-25 18:12:44.097693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf6c8f84e9b3'
down_revision = 'ae89705d6385'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('life', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'life')
    # ### end Alembic commands ###
