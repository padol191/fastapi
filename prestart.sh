#! /usr/bin/env bash

# Let the DB start
python3 backend_pre_start.py

# Run migrations
# alembic upgrade head

# Create initial data in DB
python3 initial_data.py
