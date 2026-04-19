from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

@app.route('/')
def index():
    servicios = ["Consultoría", "Soporte Técnico", "Desarrollo Web"]
    return render_template('index.html', servicios=servicios)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mensaje = request.form.get('mensaje')
        # Aquí procesarías los datos
        flash(f"Gracias {nombre}, hemos recibido tu mensaje.")
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)