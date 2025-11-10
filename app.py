from flask import Flask, render_template
import requests

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1437282453994602496/PLfb3QMAEHmIt2x-oF7y3Lr10W4SHeeYCjQ4W-8Fgm8pv72Rg8iyVD1C-lZ0yEwbf5r7"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerta', methods=['POST'])
def alerta():
    message = {
        "content": "⚠️ El usuario no ha interactuado. ¿Deseas reportar alguna novedad?"
    }
    requests.post(DISCORD_WEBHOOK, json=message)
    return "Mensaje enviado a Discord", 200

if __name__ == '__main__':
    app.run(debug=True)
