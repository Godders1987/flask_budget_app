from flask import Flask, render_template, redirect, url_for, request
import json
from decimal import Decimal
from datetime import date

app = Flask(__name__)

# Opens and loads the data held in the json file
def load_data():
  with open('data/transactions.json') as f:
    data = json.load(f)
  return data 

# Calculates when the next payday is and calculates how many days till then
def payday():
  # Get todays date
  today = date.today()
  # Payday
  this_month_payday = date(today.year, today.month, 25)
  if this_month_payday > today:
    return (this_month_payday - today).days
  elif today > this_month_payday and today.month < 12:
    return (date(today.year, today.month + 1, 25) - today).days
  else: 
    return (date(today.year + 1, 1, 25) - today).days
  

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
  days_until_payday = payday()
  for x in transactions:
    if x['type'] == 'Debit':
      total_spend += Decimal(str(x['amount']))
    else:
      total_spend -= Decimal(str(x['amount']))
  remaining = budget - total_spend
  return render_template('index.html', budget=budget, remaining=remaining, total_spend=total_spend, transactions=transactions, payday=days_until_payday)

@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method = 'POST':
    date = request.form['date']
    transaction_type = request.form['type']
    description = request.form['description']
    amount = request.form['amount']
    data = load_data()





if __name__ == '__main__':
  app.run(debug=True, port=5001)

