"""Add is_registered column to users table

Revision ID: d263b9d0b167
Revises: 2e2e590a35a7
Create Date: 2024-11-09 18:07:53.918497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd263b9d0b167'
down_revision: Union[str, None] = '2e2e590a35a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_registered', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_registered')
    # ### end Alembic commands ###
