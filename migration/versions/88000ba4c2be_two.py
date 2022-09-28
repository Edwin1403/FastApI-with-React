"""two

Revision ID: 88000ba4c2be
Revises: a4eab9a92595
Create Date: 2022-09-27 14:54:41.971018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88000ba4c2be'
down_revision = 'a4eab9a92595'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("sample",
    sa.Column("Age", sa.String, nullable=True)
    )
    pass


def downgrade() -> None:
    op.drop_column("sample", "Age")
    pass
