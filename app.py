from flask import Flask, render_template
import json
from decimal import Decimal

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
  data = load_data()
  transactions = data['transactions']
  budget = Decimal(data['monthlyBudget'])
  total_spend = Decimal(0)
  for x in transactions:
    if x['type'] == 'Debit':
      total_spend += Decimal(str(x['amount']))
    else:
      total_spend -= Decimal(str(x['amount']))
  remaining = budget - total_spend
  return render_template('index.html', budget=budget, remaining=remaining, total_spend=total_spend, transactions=transactions)

if __name__ == '__main__':
  app.run(debug=True, port=5001)

