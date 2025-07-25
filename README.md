# Tic Tac Toe Web Service

A Flask-based web service for the classic Tic-Tac-Toe game.

## Endpoints

- `POST /api/create` – Create a new game
- `GET /api/status?matchId=` – Get the current status of a game
- `POST /api/move` – Make a move in a game

## HOW TO START

```bash
docker compose up --build # This will install dependencies and expose the service at: http://localhost:5000

# Verify it's running and get your matchId

curl -X POST http://127.0.0.1:5000/api/create

# Use make_move.py to make moves easily from the command line (You need to change matchId first)
# Example: make a move as player X to position (1, 1)

python make_move.py X 1 1