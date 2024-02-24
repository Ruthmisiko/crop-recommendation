from flask import Flask, render_template
from flask import Flask, jsonify, request
from service import predict_recommendation, weather_predictions
from service import crop_model as model 
app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all books
@app.route('/weather', methods=['GET'])
def get_books():
    return jsonify({'books': books})


# Route to update a book by ID
@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    county = request.form.get('countySelect')
    month = request.form.get('monthSelect')
    recommendations = predict_recommendation(weather_predictions,model)

    print(recommendations)

    formatted = jsonify ({'Crops Recommended': recommendations.tolist()})
    
    return render_template('index.html', recommended= formatted)

if __name__ == '__main__':
    app.run(debug=True)

