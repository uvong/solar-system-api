from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Mercury", "named for the messenger of Roman gods"),
    Planet(2, "Venus", "named for the Roman goddess of love and beauty"),
    Planet(3, "Neptune", "named for the Roman god of water")
]

planets_bp = Blueprint("planets", __name__)
@planets_bp.route("/planets", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description
        })
    return jsonify(response)
    