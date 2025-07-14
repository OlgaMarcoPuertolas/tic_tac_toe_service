from flask import Blueprint, request, jsonify
from app.services.game_service import create_match, get_match, make_move

api_bp = Blueprint("api", __name__)

@api_bp.route("/")
def index():
    return "Tic Tac Toe Service"

@api_bp.route("/create", methods=["POST"])
def create():
    match_id = create_match()
    return jsonify({"matchId": match_id}), 200

@api_bp.route("/status", methods=["GET"])
def status():
    match_id = request.args.get("matchId")
    match = get_match(match_id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    return jsonify(match.to_dict()), 200

@api_bp.route("/move", methods=["POST"])
def move():
    data = request.json
    match_id = data.get("matchId")
    player = data.get("playerId")
    square = data.get("square", {})
    x, y = square.get("x"), square.get("y")

    match_data = make_move(match_id, player, x, y)
    if not match_data:
        return jsonify({"error": "Invalid match"}), 400
    return jsonify(match_data), 200
