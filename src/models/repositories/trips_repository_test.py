#Testes de Integração
import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


## IMPEDE QUE O TESTE ACONTEÇA(para não popular o banco toda hora que executado): para o funcionamento normal retirar isso de cima das funções
@pytest.mark.skip(reason="interacao com o banco")
# A função deve começar com test_
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_info = {
        "id": trip_id,
        "destination": "Roma",
        "start_date": datetime.strptime("13-03-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("13-03-2024", "%d-%m-%Y") + timedelta(days=15),
        "owner_name": "Alice",
        "owner_email": "alice@gmail.com"
    }
    
    trips_repository.create_trip(trips_info)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    response = trips_repository.find_trip_by_id(trip_id)

    assert isinstance(response, tuple)


@pytest.mark.skip(reason="interacao com o banco")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)
