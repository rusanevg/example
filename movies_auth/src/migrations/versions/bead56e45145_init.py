"""empty message

Revision ID: 6e0edd24f487
Revises: 74f7291bc3d9
Create Date: 2022-12-11 13:57:52.883554

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bead56e45145'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('create schema auth')
    op.create_table('permission',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('name'),
    schema='auth'
    )
    op.create_table('role',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('name'),
    schema='auth'
    )
    op.create_table('user',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('salt', sa.String(length=32), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    schema='auth'
    )
    op.create_table('role_permission',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('permission_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth.permission.uuid'], ),
    sa.ForeignKeyConstraint(['role_id'], ['auth.role.uuid'], ),
    sa.PrimaryKeyConstraint('uuid', 'role_id', 'permission_id'),
    sa.UniqueConstraint('role_id', 'permission_id'),
    schema='auth'
    )
    op.create_table('social_account',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('social_id', sa.String(length=64), nullable=True),
    sa.Column('social_name', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid', 'user_id'),
    sa.UniqueConstraint('social_id', 'social_name'),
    schema='auth'
    )
    op.create_table('user_agent',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid', 'user_id'),
    sa.UniqueConstraint('user_id', 'name'),
    sa.UniqueConstraint('uuid'),
    schema='auth'
    )
    op.create_table('user_role',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['auth.role.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid', 'user_id', 'role_id'),
    sa.UniqueConstraint('user_id', 'role_id'),
    schema='auth'
    )
    op.create_table('auth_history',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_agent_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('auth_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_agent_id'], ['auth.user_agent.uuid'], ),
    sa.PrimaryKeyConstraint('uuid', 'user_agent_id'),
    sa.UniqueConstraint('user_agent_id', 'auth_date'),
    schema='auth',
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_history', schema='auth')
    op.drop_table('user_role', schema='auth')
    op.drop_table('user_agent', schema='auth')
    op.drop_table('social_account', schema='auth')
    op.drop_table('role_permission', schema='auth')
    op.drop_table('user', schema='auth')
    op.drop_table('role', schema='auth')
    op.drop_table('permission', schema='auth')
    op.execute('drop schema auth')
    # ### end Alembic commands ###
