from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
import models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_flavor', methods=['GET'])
def add_flavor_page():
    return render_template('add_flavor.html')

@app.route('/flavors', methods=['GET'])
def get_flavors():
    try:
        flavors = models.get_all_flavors()
        return render_template('flavors.html', flavors=flavors), 200
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
        flavor_id = models.add_seasonal_flavor(name, availability)
        return redirect(url_for('get_flavors'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_flavor/<int:flavor_id>', methods=['POST'])
def delete_flavor(flavor_id):
    try:
        models.delete_flavor_by_id(flavor_id)
        return redirect(url_for('get_flavors'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
