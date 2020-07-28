import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Dish


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    @app.route('/dishes', methods=['GET'])
    def retrieve_dishes():
        try:
            dishes = [ dish.format() for dish in Dish.query.all()]
            return jsonify({
                'success': True,
                'dishes': dishes
            })
        except:
            abort(422)


    # Error handlers
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Not Processable'
        }), 422

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
