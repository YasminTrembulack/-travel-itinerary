import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = LinksRepository(conn)

    links_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "http://olaMundo.com.br",
        "title": "Hello World Link"
    }
    emails_to_invite_repository.registry_link(links_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = LinksRepository(conn)

    links = emails_to_invite_repository.find_links_from_trip(trip_id)
    print()
    print(links)