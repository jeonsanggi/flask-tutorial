import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

#데이터 베이스 연결
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# 데이터베이서 연결 종료
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# 초기화
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# command에서 flask init-db 를 가능하게 해준다.
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
