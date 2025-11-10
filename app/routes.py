from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to your Flask App!"})

@main.route('/about')
def about():
    return jsonify({"message": "This is a practice project for Docker deployment."})
