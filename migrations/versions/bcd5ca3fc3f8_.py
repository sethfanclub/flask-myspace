"""empty message

Revision ID: bcd5ca3fc3f8
Revises: 0024852df905
Create Date: 2021-06-09 09:00:44.721327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd5ca3fc3f8'
down_revision = '0024852df905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('wall_ibfk_1', 'wall', type_='foreignkey')
    op.create_foreign_key(None, 'wall', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wall', type_='foreignkey')
    op.create_foreign_key('wall_ibfk_1', 'wall', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###