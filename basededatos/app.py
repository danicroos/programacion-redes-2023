import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crudr1.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para la tabla Libros
@app.route('/', methods=['GET'])
def query_records():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Libros')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

# Método PUT para la tabla Libros
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Libros(titulo, autor, genero, publicacion_year, editorial, paginas, disponible) VALUES(?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, [record['titulo'], record['autor'], record['genero'], record['publicacion_year'], record['editorial'], record['paginas'], record['disponible']])
    conn.commit()
    return jsonify(record)

# Método DELETE para la tabla Libros
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Libros WHERE id = ?'
    cursor.execute(delete, [record['id']])
    conn.commit()
    return jsonify(record)

# Método POST para la tabla Libros
@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Libros SET titulo = ? WHERE id = ?'
    cursor.execute(update, [record['titulo'], record['id']])
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)
