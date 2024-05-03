"""empty message

Revision ID: 6ad1b7758c76
Revises: d69eeb0ba728
Create Date: 2024-05-02 16:17:00.771342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ad1b7758c76'
down_revision: Union[str, None] = 'd69eeb0ba728'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('complite_tasks', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'complite_tasks')
    # ### end Alembic commands ###