# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = [{"name": "Wayne", "interests": ["violin", "coding"]}]


@app.route("/")
def index():
    return "<h1>Hello Word</h1>"


@app.route("/users")
def get_user():
    return jsonify({"users": users})


@app.route("/users", methods=["POST"])
def create_user():
    request_data = request.get_json()
    new_user = {
        "name": request_data.get("name") or None,
        "interests": request_data.get("interests") or [],
    }
    users.append(new_user)
    return jsonify(new_user)


if __name__ == "__main__":
    app.run()
