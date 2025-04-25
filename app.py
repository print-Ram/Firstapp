import datetime as dt
import os
import sqlite3
import pandas as pd
import yfinance as yf
from flask import Flask, request, render_template, send_file

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Log current working directory and check if 'templates' folder exists
print("CWD:", os.getcwd())
print("Templates folder exists?", os.path.exists("templates"))
print("Files in templates:", os.listdir("templates") if os.path.exists("templates") else "Missing!")

# Function to fetch stock data using yfinance
def get_stock_data(stockdata, start_date, end_date, interval, events):
    # Get data from Yahoo Finance
    stock = yf.Ticker(stockdata)
    company_data = stock.history(start=start_date, end=end_date, interval=interval)
    
    # If no data is found, return None
    if company_data.empty:
        return None, None

    # Prepare the URL for reference
    stock_url = f"https://finance.yahoo.com/quote/{stockdata}/history?p={stockdata}"
    return company_data, stock_url

# Function to save the stock data to the SQLite database
def save_to_database(company_data, stockdata):
    # Connect to SQLite database
    conn = sqlite3.connect('stocks.db')
    
    # Save the data to a table with the stock symbol as the table name
    company_data.to_sql(stockdata, conn, if_exists='replace', index=False)
    
    # Close the connection
    conn.close()

# Function to load stock data from the SQLite database
def load_from_database(stockdata):
    conn = sqlite3.connect('stocks.db')
    query = f'SELECT * FROM {stockdata}'
    company_data = pd.read_sql_query(query, conn)
    conn.close()
    return company_data

# Define route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route to fetch and display stock data
@app.route('/get_stock_data', methods=['POST'])
def get_stock_data_route():
    stockdata = request.form['stockdata']
    start_date = dt.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    end_date = dt.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
    interval = request.form['interval']
    events = request.form['events']

    # Fetch stock data using yfinance
    company_data, stock_url = get_stock_data(stockdata, start_date, end_date, interval, events)

    # If data is None, return error
    if company_data is None:
        return "Failed to fetch stock data. Please try again later.", 500

    # Save the data to the database
    save_to_database(company_data, stockdata)
    # Build rows manually
    table_rows = ""
    for index, row in company_data.iterrows():
        table_rows += "<tr>"
        table_rows += f"<td>{index}</td>"  # Add date index manually
        for cell in row:
            table_rows += f"<td>{cell}</td>"
        table_rows += "</tr>"
    # Return the data in HTML table format and stock URL for reference
    return render_template('result.html', table=table_rows, stockdata=stockdata, stock_url=stock_url)

# Define route to download the CSV file
@app.route('/download_csv/<stockdata>')
def download_csv(stockdata):
    # Load stock data from the database
    company_data = load_from_database(stockdata)
    
    # Save the data to a CSV file
    csv_filename = f"{stockdata}_data.csv"
    company_data.to_csv(csv_filename, index=False)

    # Send the CSV file to the client
    return send_file(csv_filename, as_attachment=True)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
