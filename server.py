from flask import Flask, render_template, redirect, url_for
from cupcakes import get_cupcakes, find_cupcake, add_cupcake
app = Flask(__name__)

# Home endpoint renders all cupcakes in cupcakes.csv
@app.route('/')
def home():
    return render_template('/index.html', cupcakes = get_cupcakes('cupcakes.csv'))

# Individual Cupcake renders information about a specific cupcake once the name is clicked.
@app.route('/cupcake_individual/<name>')
def individual_cupcake(name):
    cupcake = find_cupcake('cupcakes.csv', name)

    if cupcake:
        return render_template('/cupcake-individual.html', cupcake=cupcake)
    else:
        "Sorry, cupcake not found."

# Add cupcake to order.csv by clicking the Add to Cart button. Displayed on Home and Individual Cupcake views.
@app.route('/add_cupcake/<name>')
def add_cupcake_to_order(name):
    cupcake = find_cupcake('cupcakes.csv', name)

    if cupcake:
            add_cupcake('order.csv', cupcake=cupcake)
            return redirect(url_for('home'))
    else:
        return "Sorry, cupcake not found."

# Order view displays all current cupcakes that have been added to the cart.
@app.route('/order')
def order():
    return render_template('/order.html', cupcakes = get_cupcakes('order.csv'))

if __name__ == '__main__':
    app.debug = "development"
    app.run(debug = True, port = 8000)