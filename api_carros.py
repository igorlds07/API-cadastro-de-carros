from flask import Flask, make_response, jsonify, request

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


@app.route('/carros', methods=['GET'])  # Rota de exibição da lista de carros
def get_carro():
    '''Função para mostrar os carros cadastrados no BD, em formato JSON'''
    cursor.execute('select * from carros;')
    carros = cursor.fetchall()
    for auto in carros:
        return auto


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
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso!',  
            carro=carro
        )
    )


app.run(port=5001)
