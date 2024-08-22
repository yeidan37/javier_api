from flask import Flask, jsonify

javielmascrack = Flask(__name__)  

@javielmascrack.route('/personas', methods=['GET'])
def obtener_personas():
    # Lista de nombres de personas
    lista_personas = ["Laura", "Xavier", "Daniel", "Samuel", "Acebedo", "Cancerbero", "messi"]
    # Convertir la lista a JSON y devolverla
    return jsonify(lista_personas)

if __name__ == '__main__':  #
    javielmascrack.run(debug=True)
