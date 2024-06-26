"""empty message

Revision ID: d69eeb0ba728
Revises: 912e5d895ed2
Create Date: 2024-05-02 12:45:53.691196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd69eeb0ba728'
down_revision: Union[str, None] = '912e5d895ed2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('referrals', sa.Integer(), nullable=True))
    op.drop_column('Users', 'referals')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('referals', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('Users', 'referrals')
    # ### end Alembic commands ###
