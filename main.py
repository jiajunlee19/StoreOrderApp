from Frontend.server_flask import app

if __name__ == "__main__":
    print("Starting Python Flask Server For Store Order Management Application...")
    app.run(port=5000, debug=True)
