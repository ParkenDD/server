from contextlib import contextmanager
from urllib.parse import urlparse

import psycopg2
import psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool

POOL = None


def setup(url):
    global POOL
    u = urlparse(url)
    POOL = ThreadedConnectionPool(1, 20,
                                  database=u.path[1:],
                                  user=u.username,
                                  password=u.password,
                                  host=u.hostname,
                                  port=u.port)
    # initialize DB schema
    with open('./db/schema.sql', 'r') as f:
        schema = f.read()
    with cursor(True) as cur:
        cur.execute(schema)


@contextmanager
def cursor(commit=False):
    global POOL
    assert POOL is not None, 'use db.setup() before calling db.cursor()'
    connection = None
    try:
        connection = POOL.getconn()
        cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield cur
            if commit:
                connection.commit()
        finally:
            cur.close()
    finally:
        POOL.putconn(connection)
