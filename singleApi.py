from flask import Flask, send_file

# Flask application setup
app = Flask(__name__)

# Flask route to serve firmware file
@app.route('/ota/call_Api', methods=['GET'])
def call_Api():

    data = "file_path/fila_name.bin"
    return send_file(data, mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run()