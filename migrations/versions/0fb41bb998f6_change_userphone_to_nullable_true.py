"""Change userphone to nullable=True

Revision ID: 0fb41bb998f6
Revises: edb370706f09
Create Date: 2024-11-09 14:24:41.420625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0fb41bb998f6'
down_revision: Union[str, None] = 'edb370706f09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'userphone',
               existing_type=mysql.VARCHAR(collation='utf8mb3_unicode_ci', length=15),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb3_unicode_ci', length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb3_unicode_ci', length=100),
               nullable=False)
    op.alter_column('users', 'userphone',
               existing_type=mysql.VARCHAR(collation='utf8mb3_unicode_ci', length=15),
               nullable=False)
    # ### end Alembic commands ###
