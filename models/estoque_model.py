import mysql.connector
from config.db_config import db_config

# Função para listar todos os produtos
def listar_estoque():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estoque")
        produtos = cursor.fetchall()
        return produtos
    except Exception as e:
        print(f"Erro ao listar estoque: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Função para cadastrar um novo produto
def cadastrar_produto(nome, quantidade, limite_minimo):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (nome, quantidade, limite_minimo) VALUES (%s, %s, %s)",
            (nome, quantidade, limite_minimo)
        )
        conn.commit()
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
    finally:
        cursor.close()
        conn.close()
