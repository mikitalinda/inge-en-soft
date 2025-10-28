from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return render_template('home.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    usuarios_validos = {
        "mica": "1234",
        "admin": "adminpass"
    }

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios_validos and usuarios_validos[usuario] == contraseña:
            return f"Bienvenida, {usuario}!"
        else:
            return "Usuario o contraseña incorrectos"

    return render_template('login.html')

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
