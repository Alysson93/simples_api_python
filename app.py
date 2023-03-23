from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
	{
		'id': 1,
		'titulo': 'A revolução dos bichos',
		'autor': 'George Owell'
	},
	{
		'id': 2,
		'titulo': 'O Leviatã',
		'autor': 'Thomas Hobbes'
	},
	{
		'id': 3,
		'titulo': 'O Príncipe',
		'autor': 'Maquiavel'
	},
]

@app.route('/', methods=['GET'])
def ola():
	return 'Olá mundo'

@app.route('/livros', methods=['GET'])
def get():
	return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def get_by_id(id):
	for livro in livros:
		if livro.get('id') == id:
			return jsonify(livro)
	return 'Não há um livro com esse identificador'


@app.route('/livros', methods=['POST'])
def create():
	novo_livro = request.get_json()
	livros.append(novo_livro)
	return jsonify(livros)


@app.route('/livros/<int:id>', methods=['PUT'])
def edit_by_id(id):
	livro_alterado = request.get_json()
	for indice, livro in enumerate(livros):
		if livro.get('id') == id:
			livros[indice].update(livro_alterado)
			return jsonify(livros[indice])


@app.route('/livros/<int:id>', methods=['DELETE'])
def delete(id):
	for indice, livro in enumerate(livros):
		if livro.get('id') == int(id):
			del livros[indice]

	return jsonify(livros)

app.run(port=8080, host='localhost', debug=True)