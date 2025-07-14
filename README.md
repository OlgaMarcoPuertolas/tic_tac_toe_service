# Tic Tac Toe Web Service

Servicio web en Flask para el juego Tic-Tac-Toe.

## Endpoints

- `POST /api/create` – Crea una partida
- `GET /api/status?matchId=` – Devuelve estado de la partida
- `POST /api/move` – Realiza una jugada

## HOW TO START

```bash
pip install -r requirements.txt
python run.py

## Get your matchId

curl -X POST http://127.0.0.1:5000/api/create

## Use make_move.py to make moves easily from the command line (You need to change matchId first)

Example: python make_move.py X 1 1 to send move as player X to position (1, 1)