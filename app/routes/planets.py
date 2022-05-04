from flask import Blueprint, jsonify, request, make_response, abort
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
        params = request.args
        if "name" in params and "moons" in params:
            planet_name = params["name"]
            planet_moons = params["moons"]
            planets = Planet.query.filter_by(name=planet_name, moons=planet_moons)
        elif "name" in params:
            planet_name = params["name"]
            planets = Planet.query.filter_by(name=planet_name)
        elif "moons" in params:
            planet_moons = params["moons"]
            planets = Planet.query.filter_by(moons=planet_moons)
        else:
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

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify({
        'id': planet.id,
        'name': planet.name,
        'description': planet.description,
        'moons': planet.moons
    })

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    request_body = request.get_json()

    planet = validate_planet(planet_id)

    if "name" not in request_body or\
        "description" not in request_body or\
        "moons" not in request_body:
        return jsonify({"msg": f"Request must include name, description, and moons"}), 400

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()

    return make_response(f"Planet #{planet_id} successfully updated. =D")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet_id} has been successfully deleted. D=<")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"Invalid id: '{planet_id}'. ID must be an integer."}, 400))
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"msg": f"Planet {planet_id} not found"}, 404))
    
    return planet

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
