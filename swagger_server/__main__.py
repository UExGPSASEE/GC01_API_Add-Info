#!/usr/bin/env python3

import connexion
from flask_cors import CORS  # Importa flask-cors
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Additional Info management API'}, pythonic_params=True)

    # Aplica CORS a la aplicación Flask subyacente
    CORS(app.app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Modifica origins según sea necesario

    app.run(port=8083)


if __name__ == '__main__':
    main()
