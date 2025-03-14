import subprocess
import json
from flask import Flask, request
from config import PASSWORD, HOST, PORT

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    if not data or "phone" not in data:
        return json.dumps({"error": "Номер телефона обязателен"}), 400

    phone_number = data["phone"]

    try:
        # Запуск поискового скрипта
        result = subprocess.run(
            ["python", "search_script.py", PASSWORD, phone_number], 
            capture_output=True, text=True
        )
        return json.dumps({"result": result.stdout.strip()}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)