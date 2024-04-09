"""Core module of Pass Pro."""

from passpro.database import connect


def read():
    """Reads data from db"""
    db = connect()
    for pk, data in db["user"].items():
        return pk, data
