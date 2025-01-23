"""empty message

Revision ID: ac6b652e042d
Revises: 26c51a68ff6e
Create Date: 2025-01-17 21:05:02.077476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac6b652e042d'
down_revision: Union[str, None] = '26c51a68ff6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
