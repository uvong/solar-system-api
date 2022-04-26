from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons
    def get_planet_info(self):
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'moons': self.moons
            }

planets = [
    Planet(1, "Mercury", "named for the messenger of Roman gods", 0),
    Planet(2, "Venus", "named for the Roman goddess of love and beauty", 0),
    Planet(3, "Neptune", "named for the Roman god of water", 14)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        response.append(planet.get_planet_info())
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({'msg': f"Planet ID '{planet_id}' is invalid. Please enter an Integer"}), 400


    chosen_planet = None
    for planet in planets:
        if planet.id == planet_id:
            chosen_planet = planet.get_planet_info()
    if chosen_planet is None:
        return jsonify({'msg': f"Planet {planet_id} not found."}), 404
    return jsonify(chosen_planet)
