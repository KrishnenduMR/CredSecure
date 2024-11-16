from flask import Flask, render_template, request, url_for, session, redirect
import pickle
import numpy as np
import csv
from flask_socketio import SocketIO

# # Load the Random Forest Classifier model
# filename = 'credit-card-model.pkl'
# model = pickle.load(open('credit-card-model.pkl', 'rb'))

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'C16'

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# About page route
@app.route('/about')
def about():
    if 'loggedin' in session:
        return render_template('about.html')
    return redirect(url_for('home'))

# Overview page route
@app.route('/overview')
def overview():
    if 'loggedin' in session:
        return render_template('overview.html')
    return redirect(url_for('home'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        v1 = float(request.form['v1'])
        v2 = float(request.form['v2'])
        v3 = float(request.form['v3'])
        # More variables...
        data = np.array([[v1, v2, v3]])  # Add the rest of the variables
        # my_prediction = model.predict(data)
        # return render_template('result.html', prediction=my_prediction[0])
        return render_template('result.html', prediction='0')
    if 'loggedin' in session:
        return render_template('detection.html')
    return redirect(url_for('home'))

# Result page route
@app.route('/result/<prediction>')
def result(prediction):
    return render_template('result.html', prediction=prediction)

# Contact page route
@app.route('/contact')
def contact():
    if 'loggedin' in session:
        return render_template('contact.html')
    return redirect(url_for('home'))

# Signup page route
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        
        if password != confirmpassword:
            return "Passwords do not match. Please try again."
        
        # Save user data to CSV
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([fullname, email, username, password])
        
        return redirect(url_for('home'))
    return render_template('signup.html')

# Login page route with simple validation
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate login with CSV file
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == username and row[3] == password:
                session['loggedin'] = True  # Set login status
                return redirect(url_for('overview'))
    
    return render_template('home.html', error='Invalid username or password.')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)  # Remove the loggedin session variable
    return redirect(url_for('home'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
