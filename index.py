from flask import Flask, render_template
# llamar de la biblioteca flask - importar

app = Flask(__name__)
# objeto app a partir de inicialización

@app.route('/')
def home():
    return render_template('home.html')
# decorador @ metodo route - servidor creado

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
# validacion del main - app escuchando 