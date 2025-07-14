from app.services.game_service import create_match, make_move, get_match

def test_create_and_play():
    match_id = create_match()
    match = get_match(match_id)
    assert match.current_player == "X"

    state = make_move(match_id, "X", 1, 1)
    assert state["board"][0][0] == "X"
    assert state["currentPlayer"] == "O"
