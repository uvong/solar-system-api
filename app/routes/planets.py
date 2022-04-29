from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body['name'], description=request_body['description'],
                    moons=request_body['moons'])
        
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} has been successfully created :'D", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                'id': planet.id,
                'name': planet.name,
                'description': planet.description,
                'moons': planet.moons
            })
        return jsonify(planets_response)

# def get_all_planets():
    # response = []
    # for planet in planets:
    #     response.append(planet.get_planet_info())
    # return jsonify(response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return jsonify({'msg': f"Planet ID '{planet_id}' is invalid. Please enter an Integer"}), 400


#     chosen_planet = None
#     for planet in planets:
#         if planet.id == planet_id:
#             chosen_planet = planet.get_planet_info()
#     if chosen_planet is None:
#         return jsonify({'msg': f"Planet {planet_id} not found."}), 404
#     return jsonify(chosen_planet)
