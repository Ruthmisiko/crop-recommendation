# from flask import Flask, render_template
# from flask import Flask, jsonify, request
# from service import serve_recomm_requests
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to update a book by ID
# @app.route('/recommendation', methods=['POST'])
# def get_recommendation():
#     county = request.form.get('countySelect')
#     month = request.form.get('monthSelect')
#     predictions_and_recomm = serve_recomm_requests(month, county)

#     # Extracting the values
#     weather = predictions_and_recomm['weather']
#     recommendations = predictions_and_recomm['recommendations']
#     predicted_rainfall = round(weather[0][-1], 2)  # Extracting the last value which represents rainfall
    
#     context = {'recommendations': recommendations, 'predicted_rainfall': predicted_rainfall}

#     return render_template('index.html', county=county, month=month, recommendations=recommendations,predicted_rainfall=predicted_rainfall)

# if __name__== '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, session
from service import serve_recomm_requests

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Change this to a random secret key

# Dummy user data (for demonstration purposes)
users = {'username': 'password'}  # Replace with actual user data from your database

@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    county = request.form.get('countySelect')
    month = request.form.get('monthSelect')
    predictions_and_recomm = serve_recomm_requests(month, county)

    # Extracting the values
    weather = predictions_and_recomm['weather']
    recommendations = predictions_and_recomm['recommendations']
    predicted_rainfall = weather[0][-1]  # Extracting the last value which represents rainfall
    
    return render_template('index.html', county=county, month=month, recommendations=recommendations, predicted_rainfall=predicted_rainfall)

# Login form route
@app.route('/login')
def login_form():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        session['username'] = username
        # Render index.html after successful login
        return render_template('index.html')
    else:
        return 'Invalid username or password'

# Sign-up route
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    
    # Add the user to the database or any other storage mechanism
    users[username] = password
    
    # Redirect to login page after successful sign-up
    return redirect('/login')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
     