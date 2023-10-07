import os

import click
from flask import current_app
from sqlalchemy import select

from backend.core.extensions import db

def register_commands(app):
    @app.cli.command()
    @click.option('--drop',is_flag=True,help='Crate after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm(
                'This operation will delete the database, do you want to continue?',
                abort=True
            )
            db.drop_all()
            click.echo('Dropped tables.')
        db.create_all()
        click.echo('Initialized the database.')