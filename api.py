from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<center>Welcome to the [VISHESH] API! <br> This project is made by: @vishesh_404<br>Official channel: @specialmodj</center>"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/execute', methods=['GET', 'POST'])
def execute_code():
    if request.method == 'POST':
        data = request.json
        file_name = data.get('file_name')
        ip = data.get('ip')
        port = data.get('port')
        ddosTime = data.get('ddosTime')
        ddosThreads = data.get('ddosThreads')
    else:
        file_name = request.args.get('file_name')
        ip = request.args.get('ip')
        port = request.args.get('port')
        ddosTime = request.args.get('ddosTime')
        ddosThreads = request.args.get('ddosThreads')

    if not all([file_name, ip, port, ddosTime, ddosThreads]):
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        if file_name == 'bgmi':
            command = f"./bgmi {ip} {port} {ddosTime} {ddosThreads}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
        elif file_name.endswith('.go'):
            command = f"go run {file_name} {ip} {port} {ddosTime} {ddosThreads}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        output = result.stdout + result.stderr
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
