from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

UPLOAD_FOLDER = "static"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Ensure 'static' folder exists

@app.route("/generate-logo", methods=["POST"])
def generate_logo():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Placeholder: Replace this with your actual logo generation logic
    logo_path = os.path.join(UPLOAD_FOLDER, "logo.png")
    
    # Simulate saving a generated logo (Replace this with actual logo generation code)
    with open(logo_path, "wb") as f:
        f.write(b"")  # Save an empty file for now (replace with actual image data)

    logo_url = f"http://localhost:5000/static/logo.png"
    return jsonify({"image": logo_url})  # Return the correct image URL

if __name__ == "__main__":
    app.run(debug=True)
