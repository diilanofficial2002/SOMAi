from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/test_gen_content", methods=["POST"])
def receive_post():
    # Get JSON data from POST request
    data = request.get_json()

    # Log received data (for debugging)
    print("Received data:", data)

    # Prepare response
    response = {
        "status": "success",
        "message": "POST received"
    }

    # Send JSON response
    return jsonify(response), 200


if __name__ == "__main__":
    # Run server on all interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)
