from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

def check_telegram_post(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, timeout=5, headers=headers)
        if resp.status_code == 200:
            return "Active"
        elif resp.status_code == 404:
            return "Removed or Inaccessible"
        else:
            return f"Status: {resp.status_code}"
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    urls = data.get('urls', [])
    results = {u: check_telegram_post(u) for u in urls}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
