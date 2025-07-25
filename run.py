from app import create_app

app = create_app()

if __name__ == '__main__':
    # Modified so that the title can be accessed from the browser (Although the game runs in terminal)
    app.run(debug=True, host="0.0.0.0", port=5000)
    