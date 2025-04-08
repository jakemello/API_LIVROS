from flask import Flask, request, jsonify
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def mensagem():

    return "<h1>Incentivar a leitura é a forma mais eficaz de disseminar cultura e valores.</h1>"


def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
        """)
        #Estrutura adiciona para deixar os livros salvos no banco de dados
        # e não precisar ficar adicionando sempre que reiniciar o servidor da aplicação.
        quantidade = conn.execute("SELECT COUNT(*) FROM livros").fetchone()[0]

        if quantidade == 0:
            livros_padrao = [

                ("A Arte da Dívida", "Finanças", "Fernanda TZU", "https://i.imgur.com/Zj1iQoD.jpeg"),

                ("O Pequeno Príncipe", "Ficção", "Antoine de Saint-Exupéry","https://m.media-amazon.com/images/I/61ATa0Pc4AL._AC_UF1000,1000_QL80_.jpg"),

                 ("A Menina que Roubava Livros", "Ficção", "Markus Zusak", "https://m.media-amazon.com/images/I/61L+4OBhm-L._AC_UF1000,1000_QL80_.jpg"),

                 ("Game of Thrones", "Fantasia", "George R. R. Martin", "https://m.media-amazon.com/images/I/91+1SUO3vUL.jpg"),

                 ("O Retrato de Dorian Gray", "Clássico", "Oscar Wilde", "https://m.media-amazon.com/images/I/91ZEEdj0cCL._AC_UF1000,1000_QL80_.jpg"),

                 ("Harry Potter e as Relíquias da Morte", "Fantasia", "J.K. Rowling", "https://m.media-amazon.com/images/I/81rvO7xcJOL._AC_UF1000,1000_QL80_.jpg"),

                 ("Diario de um Banana", "Infantil", "Jeff Kinney", "https://m.media-amazon.com/images/I/71fWaI5myqL._AC_UF1000,1000_QL80_.jpg"),

                 ("League of Legends: Realms of Runeterra", "Universo de Ficção", "Evan Narcisse", "https://m.media-amazon.com/images/I/81gH-PXavoL._UF894,1000_QL80_.jpg"),
            ]

            for livro in livros_padrao:
                titulo, categoria, autor, image_url = livro
                conn.execute("""
                    INSERT INTO LIVROS (titulo, categoria, autor, image_url)
                    VALUES (?, ?, ?, ?)
                """, (titulo, categoria, autor, image_url))

            conn.commit()


init_db()

# --> São os endpoint da nossa API


@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    with sqlite3.connect("database.db") as conn:

        conn.execute(f"""
            INSERT INTO Livros (titulo, categoria, autor, image_url)
            VALUES (?, ?, ?, ?)
            """, (titulo, categoria, autor, image_url))

    conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201


@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros = {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)


# --> É o comando para rodar a nossa aplicação
# --> Se o arquivo app.py for igual(==) ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)
