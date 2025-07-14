import sys
import requests

if len(sys.argv) != 4:
    print("Uso: python make_move.py <playerId> <x> <y>")
    sys.exit(1)

# Tu match ID actual
match_id = "your-match-id"
player = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

url = "http://127.0.0.1:5000/api/move"
payload = {
    "matchId": match_id,
    "playerId": player,
    "square": {"x": x, "y": y}
}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Movimiento realizado correctamente:")
        for row in data["board"]:
            print(" | ".join(cell if cell else " " for cell in row))
        print(f"\nTurno de: {data['currentPlayer']}")
        if data["over"]:
            print("Partida finalizada.")
            if data["winner"]:
                print(f"Ganador: {data['winner']}")
            else:
                print("Empate.")
    else:
        print("Error:", response.status_code, response.text)
except Exception as e:
    print("Error en la petición:", e)
