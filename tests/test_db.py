from services.db import get_connection

def test_get_connection_returns_something():
    # check that calling get_connection actually gives us a connection object back
    connection = get_connection()
    assert connection is not None
    connection.close()