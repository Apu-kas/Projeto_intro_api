from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello' , methods = ['GET'])
def hello_world():
    return jsonify({'message' : 'Olá, Mundo! Bem-vindo à API Flask'})

@app.route('/api/tarefas' , methods = ['GET'])
def get_tarefas():
    tarefas = [
        {id:1, 'titulo': 'Estudar Flask' , 'Concluída' : False},
        {id:2, 'titulo': 'Criar primeira API' , 'Concluída' : False},
        {id:2, 'titulo': 'Testar Endpoints' , 'Concluída' : False}
    ]
    return jsonify ({'tarefas' : tarefas})

if __name__ == '__main__':
    app.run(debug=True)

