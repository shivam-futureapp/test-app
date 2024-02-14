from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load pricing data 
pricing = pd.read_csv('./data.csv', index_col=0)  # Set the first column as index

@app.route('/', methods=['GET', 'POST'])  
def estimate_cost():
    data_transfer = None 
    source = None
    destination = None
    monthly_cost = None

    if request.method == 'POST': 
        data_transfer = float(request.form['data_transfer'])
        source = request.form['source']
        destination = request.form['destination']
  
        rate = pricing.loc[source, destination]
    
        dt_premium = float(rate.split('/')[0][1:].strip()) * data_transfer  
        fixed_fee = 18

        monthly_cost = fixed_fee + dt_premium

    return render_template('index.html', data_transfer=data_transfer, source=source, 
                           destination=destination, monthly_cost=monthly_cost)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
