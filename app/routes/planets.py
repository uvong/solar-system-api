from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "named for the messenger of Roman gods", 0),
    Planet(2, "Venus", "named for the Roman goddess of love and beauty", 0),
    Planet(3, "Neptune", "named for the Roman god of water", 14)
]

planets_bp = Blueprint("planets", __name__)
@planets_bp.route("/planets", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'moons': planet.moons
        })
    return jsonify(response)
    