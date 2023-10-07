from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint



import repository_com_bd

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

#api - Api(app)

#Criar um novo aluno no banco
#nome, idade, nota_1_semestre, nota_2_semestre, nome_professor, numero_da_sala
@app.route('/aluno', methods=['POST'])
def criar_aluno():
    try:
        aluno = repository_com_bd.criando_aluno()
        
        return jsonify(aluno), 201
    except Exception as ex:
        print(ex)
        return jsonify({'Mensagem': "Não consegui criar o resumo do aluno."}), 404
    
#Retorna todos os alunos
@app.route('/', methods=['GET'])
def retornar_alunos():
    try:
        resultado = repository_com_bd.retornando_alunos()
        return resultado, 200
    except:
        return jsonify({'Mensagem': "Resumo de aluno não encontrado"}), 404 
    
#Retorna um único aluno
@app.route('/aluno/<int:id>', methods=['GET'])
def retornar_produto(id:int):
    try:
        aluno = repository_com_bd.retornando_aluno(id)
        return aluno, 200
    except:
        return jsonify({'Mensagem': "Resumo de aluno não encontrado"}), 404
    
#Atualiza os dados de um aluno por id
@app.route('/aluno/<int:id>', methods=['PUT'])
def atualizar_aluno_id(id):
    try:
        aluno = repository_com_bd.retornando_aluno(id)
        if aluno['id'] == id:
            dados_atualizados = request.json
            dados_atualizados["id"]=id
            repository_com_bd.atualizar_aluno(**dados_atualizados)
            return jsonify(dados_atualizados), 200
    except Exception:
        return jsonify({'Mensagem': "Resumo de aluno não encontrado"}), 404

#Deletando um aluno por id
@app.route('/aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        aluno = repository_com_bd.retornando_aluno(id)
        if aluno:
            repository_com_bd.remover_aluno(id)
            return jsonify({"Mensagem": "Resumo de aluno deletado com sucesso"}, aluno)
    except Exception:
        return jsonify({"Mensagem": "Resumo de aluno não encontrado"}), 404

@app.route('/api-docs')
def documentacao():
    print('documentação')

app.run(debug=True)