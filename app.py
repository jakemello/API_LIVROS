from flask import Flask, request, jsonify

import sqlite3

app = Flask(__name__)

# --> São os endpoint da nossa API
@app.route("/pague")
def pagar_pessoas():

    return "<h1>começar a semana pagando suas dívidas, é bom demais</h1>"


def init_db():
    #Crie o nosso banco de dados com um arquivo 'databse.db' e conecte a variável conn(connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute(
           """"
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
               )
           """ 
        )

    init_db()  

    @app.route("/doar", methods=["POST"])
    def doar():

        dados = request.get_json()

        titulo = dados.get("titulo")
        categoria = dados.get("categoria")
        autor = dados.get("autor")
        image_url = dados.get("image_url")

        if not titulo or not categoria or not autor or not image_url:
            return jsonify({"erro":"Todos os campos são obrigatórios"}),400
        
        with sqlite3.connect("database.db") as conn:

            conn.execute(f"""
            INSERT INTO Livros (titulo, categoria, autor, imagem_url)
            VALUE ("{titulo}", "{categoria}", "{autor}", "{image_url}")
            """)

        conn.commit()

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# --> É o comando para rodar a nossa aplicação
# --> Se o arquivo app.py for igual(==) ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)

