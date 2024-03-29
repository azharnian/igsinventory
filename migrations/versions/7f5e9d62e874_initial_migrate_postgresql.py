"""Initial Migrate PostgreSQL

Revision ID: 7f5e9d62e874
Revises: 
Create Date: 2023-10-25 03:33:07.464831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5e9d62e874'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('phone', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('full_name', sa.String(length=256), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('profile_picture', sa.String(length=256), nullable=True),
    sa.Column('is_login', sa.Boolean(), nullable=True),
    sa.Column('is_email_verified', sa.Boolean(), nullable=True),
    sa.Column('is_suspended', sa.Boolean(), nullable=True),
    sa.Column('is_phone_verifed', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('last_ip', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('buildings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('rt', sa.String(length=3), nullable=True),
    sa.Column('rw', sa.String(length=3), nullable=True),
    sa.Column('kelurahan', sa.String(length=256), nullable=False),
    sa.Column('kecamatan', sa.String(length=256), nullable=False),
    sa.Column('city', sa.String(length=256), nullable=False),
    sa.Column('province', sa.String(length=256), nullable=False),
    sa.Column('zip_code', sa.String(length=6), nullable=True),
    sa.Column('photo_location', sa.String(length=256), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('component_name', sa.String(length=256), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('component_name')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('event_name', sa.String(length=256), nullable=False),
    sa.Column('note', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_name')
    )
    op.create_table('item_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_type', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('photo_location', sa.String(length=256), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('floors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('building_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('photo_location', sa.String(length=256), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['building_id'], ['buildings.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('affected_user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('component_id', sa.Integer(), nullable=False),
    sa.Column('ip_address', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['affected_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['component_id'], ['components.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=256), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('room_code', sa.String(length=256), nullable=False),
    sa.Column('room_name', sa.String(length=256), nullable=False),
    sa.Column('floor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('room_code')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('color', sa.String(length=128), nullable=True),
    sa.Column('photo_item', sa.String(length=256), nullable=True),
    sa.Column('is_electronic', sa.Boolean(), nullable=True),
    sa.Column('is_waterresistant', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('make', sa.String(length=256), nullable=True),
    sa.Column('model', sa.String(length=256), nullable=True),
    sa.Column('store', sa.String(length=256), nullable=True),
    sa.Column('volume_cc', sa.Float(), nullable=True),
    sa.Column('material', sa.String(length=256), nullable=True),
    sa.Column('machine_number', sa.String(length=256), nullable=True),
    sa.Column('police_state_number', sa.String(length=256), nullable=True),
    sa.Column('serial_number', sa.String(length=256), nullable=True),
    sa.Column('date_purchased', sa.DateTime(), nullable=True),
    sa.Column('budget_type', sa.String(length=256), nullable=True),
    sa.Column('origin_country', sa.String(length=256), nullable=True),
    sa.Column('percent_depreciation_per_year', sa.Float(), nullable=True),
    sa.Column('percent_demage', sa.Float(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('is_broken', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('photo_location', sa.String(length=256), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('item_type_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['item_type_id'], ['item_types.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('transfers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('origin_id', sa.Integer(), nullable=False),
    sa.Column('destination_id', sa.Integer(), nullable=False),
    sa.Column('date_transfered', sa.DateTime(), nullable=True),
    sa.Column('transfered_by', sa.Integer(), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['destination_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['origin_id'], ['rooms.id'], ),
    sa.ForeignKeyConstraint(['transfered_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('updates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('update_detail', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('updates')
    op.drop_table('transfers')
    op.drop_table('items')
    op.drop_table('rooms')
    op.drop_table('logs')
    op.drop_table('floors')
    op.drop_table('locations')
    op.drop_table('item_types')
    op.drop_table('events')
    op.drop_table('components')
    op.drop_table('buildings')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
