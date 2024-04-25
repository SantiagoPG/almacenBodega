from flask import Flask, request, render_template, jsonify
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Conexión a la base de datos MySQL
Conexion = 'mysql://root:@localhost/prueba' 
engine = create_engine(Conexion)

# Ruta para cargar el archivo y guardar los datos en la base de datos
@app.route('/subirArchivo', methods=['POST'])
def subir_archivo():
    archivo = request.files['archivo']
    print('Archivo recibido:', archivo.filename)
    if archivo.filename != '':
        # Leer el archivo Excel y cargar los datos en la base de datos
        df = pd.read_excel(archivo)
        print('Datos del archivo:', df.head())
        # Rellenar los valores nulos con un valor específico
        df.fillna('N/A', inplace=True)
        # Insertar datos en la tabla
        df.to_sql('datos', engine, if_exists='replace', index=False)
        # Devolver los datos en formato JSON
        return jsonify(df.to_dict(orient='records'))
    return 'No se ha seleccionado ningún archivo.'


# Ruta para obtener los datos de la tabla más reciente
@app.route('/archivoGuardado', methods=['GET'])
def obtener_ultima_tabla():
    # Realizar una consulta SQL para obtener los datos de la tabla más reciente
    query = "SELECT * FROM datos"
    df = pd.read_sql(query, engine)
    # Convertir los datos a un formato JSON y devolverlos
    return jsonify(df.to_dict(orient='records'))

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
