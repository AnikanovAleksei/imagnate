"""change user_id column type to BigInteger

Revision ID: edb370706f09
Revises: 1c6a54939ced
Create Date: 2024-11-08 17:28:04.578304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'edb370706f09'
down_revision: Union[str, None] = '1c6a54939ced'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Удаление ограничения внешнего ключа
    op.drop_constraint('basket_ibfk_1', 'basket', type_='foreignkey')

    # Изменение типа данных столбца user_id в таблице basket
    op.alter_column('basket', 'user_id',
               existing_type=mysql.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False)

    # Изменение типа данных столбца id в таблице users
    op.alter_column('users', 'id',
               existing_type=mysql.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               autoincrement=True)

    # Добавление ограничения внешнего ключа обратно
    op.create_foreign_key('basket_ibfk_1', 'basket', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    # Удаление ограничения внешнего ключа
    op.drop_constraint('basket_ibfk_1', 'basket', type_='foreignkey')

    # Изменение типа данных столбца id в таблице users обратно
    op.alter_column('users', 'id',
               existing_type=sa.BigInteger(),
               type_=mysql.INTEGER(),
               existing_nullable=False,
               autoincrement=True)

    # Изменение типа данных столбца user_id в таблице basket обратно
    op.alter_column('basket', 'user_id',
               existing_type=sa.BigInteger(),
               type_=mysql.INTEGER(),
               existing_nullable=False)

    # Добавление ограничения внешнего ключа обратно
    op.create_foreign_key('basket_ibfk_1', 'basket', 'users', ['user_id'], ['id'])
