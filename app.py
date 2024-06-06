from flask import Flask, request

app = Flask(__name__)

@app.route('/')
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
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                color: #e0e0e0;
                font-family: 'Orbitron', sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }

            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.5), 0 0 25px rgba(0, 255, 255, 0.3), 0 0 35px rgba(0, 255, 255, 0.2);
                animation: glow 2s infinite alternate;
                margin-bottom: 2rem;
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
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Perfil Estudiantil</h1>
            <div class="image-container">
                <img src="https://via.placeholder.com/100" alt="Profile Image">
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
                background: linear-gradient(135deg, #1f1c2c, #928dab);
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
