from flask import Flask, jsonify, request

import mysql.connector

# Conectando com o banco de dados 

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Luna@2020',
    database='cadastro'
)

# Condição para verificar a conexão
if mydb.is_connected():
    print('Conexão realizada com sucesso!')
    cursor = mydb.cursor()

# Criação do app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Rota para mostrar os carros existente
@app.route('/carros', methods=['GET'])  # Rota de exibição da lista de carros
def get_carro():
    '''Função para mostrar os carros cadastrados no BD, em formato JSON'''
    cursor.execute('select * from carros;')
    carros = cursor.fetchall()
    return jsonify(carros)


# Rota para adicionar um novo carro
@app.route('/carros', methods=['POST'])  # Rota para adicionar um novo carro
def criar_carro():
    ''' Função para criar um novo perfil de carro, usando os parâmetros 
    específicados em formato JSON'''
    carro = request.json

    # Recupera os dados do carro do JSON enviado na requisição
    modelo = carro.get('modelo')
    marca = carro.get('marca')
    ano = carro.get('ano')

    # Inserir os dados no banco de dados
    cursor.execute(
        'INSERT INTO carros (modelo, marca, ano) VALUES (%s, %s, %s)',
        (modelo, marca, ano)
    )
    mydb.commit()  # Confirma a transação

    # Retorna uma mensagem de cadastro realizado
    return jsonify({
        'mensagem': 'Carro cadastrado com sucesso!',
        'carro': {'modelo': modelo, 'marca': marca, 'ano': ano}
    })


# Função para editar algum carro existente 
@app.route('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    '''Função para editar algum carro existente, 
    usando o atributo id como parâmetro'''
    data = request.get_json()
    marca = data['marca']
    modelo = data['modelo']
    ano = data['ano']

    # Executa o comando SQL para editar 
    cursor.execute(
        'UPDATE carros SET marca = %s, modelo = %s, ano = %s WHERE id = %s',
        (marca, modelo, ano, id)
    )
    mydb.commit()
    # Comdição para ver se o veículo existe e executar o comando 'ATUALIZAR'
    if cursor.rowcount > 0:
        return jsonify({'message': 'Carro atualizado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Carro não encontrado'}), 404


# Rota para excluir o perfil de um carro
@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    '''Função para deletar algum carro existente
    , usando o parâmetro id para busca'''
    cursor.execute('DELETE FROM carros WHERE id = %s', (id,))
    mydb.commit()

    # Condição para ver se o carro existe, se encontrado é deletado
    if cursor.rowcount > 0:
        return jsonify({'message': 'Carro excluído com sucesso!'}), 200
    else:
        return jsonify({'message': 'Carro não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)
