from flask import jsonify, Blueprint

#jsonify: tranformas as respostas em json para o usuário
#Blueprint: ajuda a dar um nome bacana para a rotas para saber melhor a que ela se refere

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"Ola": "Mundo!"}), 200