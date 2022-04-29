from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)

# class Planet:
#     def __init__(self, id, name, description, moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moons = moons
#     def get_planet_info(self):
#         return {
#                 'id': self.id,
#                 'name': self.name,
#                 'description': self.description,
#                 'moons': self.moons
#             }

# planets = [
#     Planet(1, "Mercury", "named for the messenger of Roman gods", 0),
#     Planet(2, "Venus", "named for the Roman goddess of love and beauty", 0),
#     Planet(3, "Neptune", "named for the Roman god of water", 14)
# ]