"""Add quantity field to Basket table

Revision ID: 1c6a54939ced
Revises: 856a4522268e
Create Date: 2024-11-08 16:11:11.399639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c6a54939ced'
down_revision: Union[str, None] = '856a4522268e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('basket', sa.Column('quantity', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('basket', 'quantity')
    # ### end Alembic commands ###
