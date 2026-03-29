from flask import Flask, render_template
import json

app = Flask(__name__)

# Opens and loads the data held in the json file
def load_data():
  with open('data/transactions.json') as f:
    data = json.load(f)
  return data 

@app.route('/')
def index():
  return render_template('index.html')

#Pulls the data from the json file and then save the monthlyBudget amount to a variable to use in the html
@app.route('/dashboard')
def dashboard():
  budget = load_data()
  return render_template('index.html', budget=budget['monthlyBudget'])

if __name__ == '__main__':
  app.run(debug=True, port=5001)

