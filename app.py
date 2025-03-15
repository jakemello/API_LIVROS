from flask import Flask  # Aqui estamos importando a classe Flask do módulo flask para criar nossa aplicação
import sqlite3  # Importamos o módulo sqlite3 para manipulação do banco de dados SQLite

# Criamos uma instância do Flask e armazenamos na variável "app"
# O parâmetro __name__ indica que este arquivo será reconhecido como o principal da aplicação
app = Flask(__name__)

# Aqui estamos criando uma rota para o endpoint "/"
# Ou seja, quando acessarmos http://127.0.0.1:5000/, a função abaixo será executada
@app.route("/")
def pagar_pessoas():
    # Retorna uma mensagem formatada em HTML para ser exibida na página principal
    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"

# Criamos uma rota para o endpoint "/pix"
# Quando acessarmos http://127.0.0.1:5000/pix, a função será chamada automaticamente
@app.route("/pix")
def mande_o_pix():
    # Retorna uma mensagem formatada em HTML para ser exibida na rota "/pix"
    return "<h3>Pagar as pessoas faz bem pras pessoas!!! =D</h3>"

# Criamos uma rota para o endpoint "/comidas"
# Quando acessarmos http://127.0.0.1:5000/comidas, essa função será executada
@app.route("/comidas")
def prato_do_dia():
    # Retorna uma mensagem formatada em HTML descrevendo o prato do dia
    return "<h1>O prato do dia é feijoada com farofinha com bacon e de sobremesa brownie com sorvete!!!</h1>"

# Função para inicializar o banco de dados SQLite
# Criamos uma conexão com o banco de dados chamado 'database.db'
# Se o banco de dados ainda não existir, ele será criado automaticamente

def init_db():
    # Conectamos ao banco de dados SQLite e usamos "with" para garantir que a conexão seja fechada corretamente após a execução
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  # Identificador único para cada livro, gerado automaticamente
                    titulo TEXT NOT NULL,  # O título do livro, armazenado como texto e obrigatório
                    categoria TEXT NOT NULL,  # A categoria do livro (exemplo: ficção, tecnologia), armazenada como texto e obrigatória
                    autor TEXT NOT NULL,  # O nome do autor do livro, armazenado como texto e obrigatório
                    imagem_url TEXT NOT NULL  # O URL da imagem da capa do livro, armazenado como texto e obrigatório
                )
            """
        )  # A execução desse comando cria a tabela caso ela ainda não exista, garantindo que nossa estrutura de banco esteja configurada

# Chamamos a função para inicializar o banco de dados quando o programa for executado
init_db()

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração (nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código)
    app.run(debug=True)