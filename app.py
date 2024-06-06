<<<<<<< HEAD
from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging
=======
from flask import Flask, request, send_from_directory
>>>>>>> 62294206eebfad6df56ab969ee1e4f132f66e63d

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modelo.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
<<<<<<< HEAD
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        abdomen = float(request.form['abdomen'])
        antena = float(request.form['antena'])
        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[abdomen, antena]], columns=['abdomen', 'antena'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'categoria': prediction[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400
=======
def index():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Perfil Futurista</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

            body {
                margin: 0;
                padding: 0;
                font-family: 'Orbitron', sans-serif;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                color: #e0e0e0;
                background: black;
            }

            .background {
                position: absolute;
                width: 100%;
                height: 100%;
                overflow: hidden;
                z-index: -1;
            }

            .background .circle {
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.2);
                animation: animate 10s linear infinite;
                bottom: -150px;
            }

            .background .circle:nth-child(1) {
                width: 60px;
                height: 60px;
                left: 25%;
                animation-duration: 18s;
                animation-delay: 0s;
            }

            .background .circle:nth-child(2) {
                width: 100px;
                height: 100px;
                left: 10%;
                animation-duration: 15s;
                animation-delay: 2s;
            }

            .background .circle:nth-child(3) {
                width: 80px;
                height: 80px;
                left: 70%;
                animation-duration: 12s;
                animation-delay: 4s;
            }

            .background .circle:nth-child(4) {
                width: 120px;
                height: 120px;
                left: 40%;
                animation-duration: 22s;
                animation-delay: 0s;
            }

            .background .circle:nth-child(5) {
                width: 150px;
                height: 150px;
                left: 65%;
                animation-duration: 20s;
                animation-delay: 2s;
            }

            @keyframes animate {
                0% {
                    transform: translateY(0) rotate(0deg);
                    opacity: 1;
                }
                100% {
                    transform: translateY(-1000px) rotate(720deg);
                    opacity: 0;
                }
            }

            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.5), 0 0 25px rgba(0, 255, 255, 0.3), 0 0 35px rgba(0, 255, 255, 0.2);
                animation: glow 2s infinite alternate;
                margin-bottom: 2rem;
                position: relative;
                z-index: 1;
            }

            @keyframes glow {
                from {
                    box-shadow: 0 0 15px rgba(0, 255, 255, 0.5), 0 0 25px rgba(0, 255, 255, 0.3), 0 0 35px rgba(0, 255, 255, 0.2);
                }
                to {
                    box-shadow: 0 0 25px rgba(0, 255, 255, 0.7), 0 0 35px rgba(0, 255, 255, 0.5), 0 0 45px rgba(0, 255, 255, 0.4);
                }
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                color: #00e6e6;
            }

            p {
                font-size: 1.5rem;
                margin: 0.5rem 0;
                animation: fadeIn 1s ease-in-out infinite alternate;
            }

            @keyframes fadeIn {
                from {
                    opacity: 0.5;
                }
                to {
                    opacity: 1;
                }
            }

            .form-container {
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.5), 0 0 25px rgba(0, 255, 255, 0.3), 0 0 35px rgba(0, 255, 255, 0.2);
                width: 300px;
                text-align: left;
                position: relative;
                z-index: 1;
            }

            .form-container input, .form-container button {
                width: 100%;
                padding: 0.5rem;
                margin: 0.5rem 0;
                border: none;
                border-radius: 5px;
                font-family: 'Orbitron', sans-serif;
            }

            .form-container input {
                background: rgba(255, 255, 255, 0.2);
                color: #e0e0e0;
            }

            .form-container button {
                background: #00e6e6;
                color: #121212;
                cursor: pointer;
            }

            .form-container button:hover {
                background: #00cccc;
            }

            .image-container img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
                object-fit: cover;
            }
        </style>
    </head>
    <body>
        <div class="background">
            <div class="circle"></div>
            <div class="circle"></div>
            <div class="circle"></div>
            <div class="circle"></div>
            <div class="circle"></div>
        </div>
        <div class="container">
            <h1>Perfil Estudiantil</h1>
            <div class="image-container">
                <img src="/static/imagen.jpg" alt="Profile Image">
            </div>
            <p id="fixed-text">Soy</p>
            <p id="changing-text"></p>
        </div>
        <div class="form-container">
            <form action="/submit" method="post">
                <label for="name">Nombre:</label>
                <input type="text" id="name" name="name">
                <label for="grade">Grado:</label>
                <input type="text" id="grade" name="grade">
                <label for="career">Carrera:</label>
                <input type="text" id="career" name="career">
                <button type="submit">Enviar</button>
            </form>
        </div>
        <script>
            const texts = [
                'Alan de Jesus Martinez Hernandez',
                'de 9ºA',
                'de la carrera Ingenieria en DyG de Software'
            ];
            let currentIndex = 0;

            function updateText() {
                document.getElementById('changing-text').innerText = texts[currentIndex];
                currentIndex = (currentIndex + 1) % texts.length;
            }

            setInterval(updateText, 2000); // Cambiar texto cada 2 segundos
            window.onload = updateText; // Mostrar el primer texto inmediatamente
        </script>
    </body>
    </html>
    '''
>>>>>>> 62294206eebfad6df56ab969ee1e4f132f66e63d

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    grade = request.form.get('grade')
    career = request.form.get('career')
    return f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Datos Enviados</title>
        <style>
            body {{
                background: black;
                color: #e0e0e0;
                font-family: 'Orbitron', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>Datos Enviados</h1>
        <p>Nombre: {name}</p>
        <p>Grado: {grade}</p>
        <p>Carrera: {career}</p>
        <a href="/">Volver</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
