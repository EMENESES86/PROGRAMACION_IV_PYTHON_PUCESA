from flask import Flask, send_file, render_template, request
from grafo_utils import grafo_a_imagen, camino_optimo_con_costera, obtener_ciudades

app = Flask(__name__)

@app.route('/grafo')
def ver_grafo():
    img = grafo_a_imagen()
    return send_file(img, mimetype='image/png')

@app.route('/camino')
def ver_camino():
    resultado = camino_optimo_con_costera()
    return render_template("camino.html", resultado=resultado)

@app.route('/camino_formulario', methods=['GET', 'POST'])
def camino_formulario():
    ciudades = obtener_ciudades()
    resultado = None

    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        if origen and destino and origen != destino:
            resultado = camino_optimo_con_costera(origen, destino)

    return render_template("formulario.html", ciudades=ciudades, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
