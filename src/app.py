from flask import Flask, jsonify

from controllers.controller import YoutubeController
from security.security import token_required

app = Flask(__name__)

app.config["DEBUG"] = True

controller = YoutubeController()
decorator = token_required

@app.route('/')
def index():
    return(" Hi! This's My Project! ")

@app.route('/get_info', methods=["GET"])
@decorator
def getInfo():
    info = controller.get_data()
    return jsonify({'Infomation': info})

@app.route('/info/<int:id>', methods=["GET"])
@decorator
def getInfoId(id):  
    info = controller.get_data()
    return jsonify({'Infomation': info[id]})

@app.route('/process', methods=["GET"])
@decorator
def process():
    data = controller.process_data()
    return jsonify({'data': data})

@app.route('/write_info', methods=["GET"])
@decorator
def writeInfo():
    worksheet = controller.write_data_to_db()
    if worksheet:
        return jsonify({"message": "connected"})
    else:
        return jsonify({"message": "failed"})

@app.route('/sync_data', methods=["GET"])
@decorator
def syncData():    
    controller.syncdata()
    return jsonify({'message': 'sync complete.'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)


