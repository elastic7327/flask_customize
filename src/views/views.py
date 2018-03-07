

from src.flaskr import app

@app.route('/protected', methods=['GET'])
@jwt_required()
def hello_jwt():
    return jsonify({
        'message': 'hello world!'
    })

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 'hello world!'
    })
