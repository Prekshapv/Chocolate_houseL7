from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
import models  # Ensure your models.py file has the necessary functions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_flavor', methods=['GET'])
def add_flavor_page():
    return render_template('add_flavor.html')

@app.route('/add_ingredient', methods=['GET'])
def add_ingredient_page():
    return render_template('add_ingredient.html')

@app.route('/add_suggestion', methods=['GET'])
def add_suggestion_page():
    flavors = models.get_all_flavors()  # Fetch available flavors from the database
    return render_template('add_suggestion.html', flavors=flavors)

@app.route('/flavors', methods=['GET'])
def get_flavors():
    try:
        flavors = models.get_all_flavors()  # Fetch flavors from your database
        return render_template('flavors.html', flavors=flavors), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    try:
        ingredients = models.get_all_ingredients()  # Fetch ingredients from your database
        return render_template('ingredients.html', ingredients=ingredients), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    try:
        suggestions = models.get_all_suggestions()  # Fetch suggestions from your database
        return render_template('suggestions.html', suggestions=suggestions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flavor', methods=['POST'])
def add_flavor():
    data = request.form
    name = data.get('name')
    availability = data.get('availability')

    if not name or not availability:
        abort(400, description="Name and availability are required.")

    try:
        flavor_id = models.add_seasonal_flavor(name, availability)  # Add flavor to your database
        return redirect(url_for('get_flavors'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ingredient', methods=['POST'])
def add_ingredient():
    data = request.form
    name = data.get('name')
    quantity = data.get('quantity')

    if not name or not quantity:
        abort(400, description="Name and quantity are required.")

    try:
        models.add_ingredient(name, int(quantity))  # Add ingredient to your database
        return redirect(url_for('get_ingredients'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/suggestion', methods=['POST'])
def add_suggestion():
    data = request.form
    flavor_id = data.get('flavor')
    allergy_concern = data.get('allergy_concern')

    if not flavor_id or not allergy_concern:
        abort(400, description="Flavor and allergy concern are required.")

    try:
        models.add_customer_suggestion(int(flavor_id), allergy_concern)  # Add suggestion to your database
        return redirect(url_for('get_suggestions'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_flavor/<int:flavor_id>', methods=['POST'])
def delete_flavor(flavor_id):
    try:
        models.delete_flavor_by_id(flavor_id)  # Delete flavor from your database
        return redirect(url_for('get_flavors'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_ingredient/<int:ingredient_id>', methods=['POST'])
def delete_ingredient(ingredient_id):
    try:
        models.delete_ingredient_by_id(ingredient_id)  # Delete ingredient from your database
        return redirect(url_for('get_ingredients'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_suggestion/<int:suggestion_id>', methods=['POST'])
def delete_suggestion(suggestion_id):
    try:
        models.delete_suggestion(suggestion_id)  # Delete suggestion from your database
        return redirect(url_for('get_suggestions'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)