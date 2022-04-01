"""init

Revision ID: 55ff7236a566
Revises:
Create Date: 2022-04-01 22:08:55.040862

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "55ff7236a566"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "vehicle_count",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("started", sa.DateTime, default=datetime.utcnow),
        sa.Column("ended", sa.DateTime),
        sa.Column("status", sa.String),
        sa.Column("number_of_vehicles", sa.Integer),
    )


def downgrade():
    op.drop_table("vehicle_count")
