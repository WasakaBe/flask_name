from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
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
                justify-content: center;
                align-items: center;
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
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Perfil Estudiantil</h1>
            <p id="fixed-text">Soy</p>
            <p id="changing-text"></p>
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

if __name__ == '__main__':
    app.run(debug=True)
