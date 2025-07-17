from flask import Flask, request

app = Flask(__name__)

# Dummy prediction function (replace with ML model)
def predict_price(area, bedrooms, bathrooms):
    # Simple formula (replace with ML model.predict)
    price = (area * 300) + (bedrooms * 50000) + (bathrooms * 30000)
    return round(price, 2)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            bathrooms = int(request.form['bathrooms'])
            prediction = predict_price(area, bedrooms, bathrooms)
        except ValueError:
            prediction = "Invalid input"

    return '''
    <html>
        <head>
            <title>House Price Prediction</title>
        </head>
        <body style="font-family: Arial; background-color: #f5f5f5; text-align: center; padding: 50px;">
            <h2 style="color: #333;">House Price Prediction</h2>
            <form method="POST" style="display: inline-block; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <label>Area (in sqft):</label><br>
                <input type="text" name="area" style="padding: 5px; width: 200px;"><br><br>

                <label>Bedrooms:</label><br>
                <input type="text" name="bedrooms" style="padding: 5px; width: 200px;"><br><br>

                <label>Bathrooms:</label><br>
                <input type="text" name="bathrooms" style="padding: 5px; width: 200px;"><br><br>

                <input type="submit" value="Predict Price" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
            </form>
            <br><br>
            <div style="font-size: 20px; color: #333;">
                {}
            </div>
        </body>
    </html>
    '''.format(f"Predicted Price: ${prediction}" if prediction is not None else "")

if __name__ == '__main__':
    app.run(debug=True)