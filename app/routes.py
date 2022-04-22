from flask import Blueprint

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