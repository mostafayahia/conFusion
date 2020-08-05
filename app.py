import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Dish, setup_db, rollback, close_connection, Promotion
import sys


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # ======= Dishes ============
    @app.route('/dishes', methods=['GET'])
    def retrieve_dishes():
        try:
            dishes = [ dish.format() for dish in Dish.query.all()]
            return jsonify({
                'success': True,
                'dishes': dishes
            })
        except:
            print(sys.exc_info())
            abort(422)


    @app.route('/dishes', methods=['POST'])
    def create_dish():
        body = request.get_json()

        # if body not exist, will be considered bad request
        if not body:
            abort(400)

        # if any of not null args not exist in the body it will be considered a bad request
        for arg in ['name', 'image', 'category', 'price']:
            if arg not in body:
                abort(400)
        
        # extract args
        name = body.get('name', None)
        image = body.get('image', None)
        category = body.get('category', None)
        price = body.get('price', None)

        try:
            dish = Dish(name=name, image=image, category=category, price=price)
            dish.insert()
            dish_id = dish.id
            dishes = [dish.format() for dish in Dish.query.all()]
            return jsonify({
                'success': True,
                'created': dish_id,
                'dishes': dishes
            })

        except:
            print(sys.exc_info())
            rollback()
            abort(422)
        finally:
            close_connection()

    @app.route('/dishes/<int:dish_id>', methods=['PATCH'])
    def update_dish_price(dish_id):
        dish = Dish.query.filter(Dish.id == dish_id).one_or_none()

        # if there is no dish exist for dish_id, Will be consider 404 error
        if not dish: abort(404)

        body = request.get_json()

        # if body not exist or not containg price, Will be considered bad request
        if not body or 'price' not in body:
            abort(400)

        # extract args
        price = body.get('price', None)

        try:
            dish.price = price
            dish.update()
            formatted_dish = dish.format()
            return jsonify({
                'success': True,
                'dish': formatted_dish
            })
        except:
            print(sys.exc_info)
            rollback()
            abort(422)
        finally:
            close_connection()

    @app.route('/dishes/<int:dish_id>', methods=['DELETE'])
    def remove_dish(dish_id):
        dish = Dish.query.filter(Dish.id == dish_id).one_or_none()

        # if dish with the given dish_id, Will be consider unprocessable request
        if not dish: abort(422)

        try:
            dish.delete()
            dish_id = dish.id
            return jsonify({
                'success': True,
                'deleted': dish_id,
                'dishes': [dish.format() for dish in Dish.query.all()]
            })
        except:
            print(sys.exc_info())
            rollback()
            abort(422)
        finally:
            close_connection()

    ##### Promotions ############
    @app.route('/promotions', methods=['GET'])
    def retrieve_promotions():
        return jsonify({
            'success': True,
            'promotions': [ promotion.format() for promotion in Promotion.query.all()]
        })

    @app.route('/promotions', methods=['POST'])
    def create_promotion():
        body = request.get_json()

        # if body not exist, will be considered bad request
        if not body:
            abort(400)

        # if any of not null args not exist in the body it will be considered a bad request
        for arg in ['name', 'image', 'price', 'description']:
            if arg not in body:
                abort(400)
        
        # extract args
        name = body.get('name', None)
        image = body.get('image', None)
        price = body.get('price', None)
        description = body.get('description', None)

        try:
            promotion = Promotion(name=name, image=image, price=price, description=description)
            promotion.insert()
            promotion_id = promotion.id
            promotions = [promotion.format() for promotion in Promotion.query.all()]
            return jsonify({
                'success': True,
                'created': promotion_id,
                'promotions': promotions
            })

        except:
            print(sys.exc_info())
            rollback()
            abort(422)
        finally:
            close_connection()

    @app.route('/promotions/<int:promotion_id>', methods=['DELETE'])
    def remove_promotion(promotion_id):
        promotion = Promotion.query.filter(Promotion.id == promotion_id).one_or_none()

        # if promotion with the given promotion_id, Will be consider unprocessable request
        if not promotion: abort(422)

        try:
            promotion.delete()
            promotion_id = promotion.id
            return jsonify({
                'success': True,
                'deleted': promotion_id,
                'promotions': [promotion.format() for promotion in Promotion.query.all()]
            })
        except:
            print(sys.exc_info())
            rollback()
            abort(422)
        finally:
            close_connection()

    # ======Error handlers==========
    
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

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
