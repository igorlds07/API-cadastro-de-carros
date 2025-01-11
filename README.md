
Documentação da API de Cadastro de Carros. 🚗

Esta é uma API simples para gerenciar carros cadastrados. Ela permite consultar todos os carros cadastrados e adicionar novos carros ao sistema. 
A API foi construída com Flask e MySQL.

Base URL
A URL base da API é:
http://127.0.0.1:5001/

1. Listar Todos os Carros:

Endpoint: GET /carros
Descrição: Esse endpoint retorna uma lista de todos os carros cadastrados no sistema.
Método HTTP: GET

Parâmetros:
Não há parâmetros necessários.

Exemplo de Requisição:

GET http://127.0.0.1:5001/carros

Exemplo de Resposta (código HTTP 200 - OK):
json
Copiar código
{
  "mensagem": "Lista de carros",
  "dados": [
    {
      "id": 1,
      "modelo": "Gol",
      "marca": "Volkswagen",
      "ano": 2015
    },
    {
      "id": 2,
      "modelo": "Fusca",
      "marca": "Volkswagen",
      "ano": 1978
    }
  ]
}
Descrição da Resposta:
mensagem: Uma mensagem descritiva sobre o que está sendo retornado.

dados: Uma lista de carros cadastrados. 

Cada carro contém:

id: Identificador único do carro.
modelo: O modelo do carro.
marca: A marca do carro.
ano: O ano de fabricação do carro.

Notas:
Caso não existam carros cadastrados, a resposta será uma lista vazia.

2. Adicionar um Novo Carro:

Endpoint: POST /carros
Descrição: Este endpoint permite cadastrar um novo carro no sistema.

Método HTTP: POST

Parâmetros:
A requisição deve conter um corpo JSON com os seguintes parâmetros:

modelo (string): O modelo do carro.
marca (string): A marca do carro.
ano (inteiro): O ano de fabricação do carro.

Exemplo de Requisição:

POST http://127.0.0.1:5001/carros
Content-Type: application/json

{
    "modelo": "Civic",
    "marca": "Honda",
    "ano": 2020
}
Exemplo de Resposta (código HTTP 201 - Criado):

{
  "mensagem": "Carro cadastrado com sucesso!",
  "carro": {
    "modelo": "Civic",
    "marca": "Honda",
    "ano": 2020
  }
}
Descrição da Resposta:

mensagem: Uma mensagem confirmando que o carro foi cadastrado com sucesso.

carro: O objeto do carro que foi recém-cadastrado, contendo:

modelo: O modelo do carro.
marca: A marca do carro.
ano: O ano de fabricação do carro.

Notas:
Os dados devem ser enviados no corpo da requisição em formato JSON.
A resposta retornará o carro recém-cadastrado, com o mesmo formato dos dados que foram enviados.
Mensagens de Erro
Caso algo dê errado, a API retorna mensagens de erro com o código HTTP apropriado. Abaixo estão alguns exemplos de erros comuns:

Erro 400 - Bad Request (Requisição malformada):
Isso acontece quando os dados enviados para criar um carro não estão corretos ou faltando algum campo necessário.

Exemplo de Resposta:

{
  "mensagem": "Erro: Faltando parâmetros obrigatórios.",
  "erro": "O campo 'modelo' é obrigatório."
}
Erro 500 - Erro Interno do Servidor:
Este erro ocorre quando há um problema no servidor (por exemplo, falha na conexão com o banco de dados).

Exemplo de Resposta:

{
  "mensagem": "Erro ao acessar o banco de dados",
  "erro": "Erro desconhecido na conexão MySQL."
}

3. Atualizar um Carro Existente:
   
Endpoint:
PUT /carros/<int:id>

Descrição:
Este endpoint permite editar os dados de um carro existente. O carro é localizado pelo id, e os dados fornecidos são atualizados.

Método HTTP:
PUT

Parâmetros:
A requisição deve conter um corpo JSON com os seguintes dados para atualização:

modelo (string): O modelo do carro.
marca (string): A marca do carro.
ano (inteiro): O ano de fabricação do carro.
Exemplo de Requisição:

PUT http://127.0.0.1:5001/carros/1  
Tipo de conteúdo: application/json

{
  "modelo": "Civic",
  "marca": "Honda",
  "ano": 2021
}
Exemplo de Resposta (código HTTP 200 - OK):

{
  "message": "Carro atualizado com sucesso!"
}
Exemplo de Resposta (código HTTP 404 - Not Found):

{
  "message": "Carro não encontrado"
}
Notas:
Se o carro não for encontrado pelo id, a resposta será 404 - Not Found. Caso contrário, o carro será atualizado com os novos dados.

4. Excluir um Carro Existente:

Endpoint:
DELETE /carros/<int:id>

Descrição:
Este endpoint permite excluir um carro do sistema. O carro é localizado pelo id, e se encontrado, será removido do banco de dados.

Método HTTP:
DELETE

Exemplo de Requisição:

DELETE http://127.0.0.1:5001/carros/1
Exemplo de Resposta (código HTTP 200 - OK):


{
  "message": "Carro excluído com sucesso!"
}
Exemplo de Resposta (código HTTP 404 - Not Found):

{
  "message": "Carro não encontrado"
}
Notas:
Se o carro não for encontrado pelo id, a resposta será 404 - Not Found. Caso contrário, o carro será excluído do banco de dados.


Como Usar a API
Para usar esta API, você pode interagir com ela utilizando ferramentas como Postman, cURL ou diretamente do seu código (por exemplo, usando a biblioteca requests no Python).

Aqui estão alguns exemplos de como você pode testar a API usando o Postman:

Listar todos os carros:

Abra o Postman e crie uma nova requisição GET para http://127.0.0.1:5001/carros.

Cadastrar um novo carro:

Crie uma nova requisição POST para http://127.0.0.1:5001/carros.
No corpo (tab "Body"), adicione um JSON semelhante a este:

{
  "modelo": "Fusca",
  "marca": "Volkswagen",
  "ano": 1976
}

Conclusão
Essa API simples permite que você gerencie um pequeno cadastro de carros, com funcionalidades de listagem e inserção.
