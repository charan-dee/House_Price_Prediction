
from flask import Flask, render_template, request
from house import predict_price

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    price = None

    if request.method == 'POST':

        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        age = int(request.form['age'])
        location = request.form['location']
        parking = int(request.form['parking'])

        price = predict_price(
            area, bedrooms, bathrooms, age, location, parking
        )

    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)