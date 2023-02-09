from flask import Flask, jsonify

from controllers.controller import YoutubeController
from security.security import token_required

app = Flask(__name__)

app.config["DEBUG"] = True

controller = YoutubeController
decorator = token_required

@app.route('/')
def index():
    return(" Hi! This's My Project! ")

@app.route('/get_info',methods=["GET"])
@decorator
def getInfo():
    info = controller.get_data()
    return jsonify({'Infomation':info})

@app.route('/info/<int:id>',methods=["GET"])
@decorator
def getInfoId(id):  
    info = controller.get_data()
    return jsonify({'Infomation':info[id]})


@app.route('/process',methods=["GET"])
@decorator
def process():
    info = controller.get_data()
    data = controller.process_data(info)
    return jsonify({'data':data})


@app.route('/write_info', methods=["GET"])
@decorator
def writeInfo():
    info = controller.get_data()
    data = controller.process_data(info)
    worksheet = controller.write_data_to_db(data)
    try:
        if worksheet:
            return ("connected !")
    except:
        return ("failed !")


@app.route('/sync_data', methods=["GET"])
@decorator
def syncData():    
    works = controller.syncdata()
    try:
        if works:
            return ("sync data success !")
    except:
        return ("sync data failed !")


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)


