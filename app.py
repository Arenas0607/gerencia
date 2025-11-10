from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1437289372054720594/2N-AMKnjk2bvP01TV0dD-d5H0OaLXxIWkTQk_mfDvT0KA5gxgHpVnSOWwVTYOgiRuWdX"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_discord', methods=['POST'])
def enviar_discord():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    mensaje = {
        "embeds": [
            {
                "title": "🆘 Reporte de usuario !varado",
                "description": f"📍 [Ver ubicación en Google Maps](https://www.google.com/maps?q={lat},{lon})",
                "color": 3447003  # Azul
            }
        ]
    }
    response = requests.post(DISCORD_WEBHOOK, json=mensaje)
    return jsonify({"status": "ok", "discord_response": response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
