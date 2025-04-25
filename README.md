
# Stock Data Fetcher with Flask and SQLite3

This is a simple web application built using Python's Flask framework and SQLite3. The application allows users to retrieve historical stock data from Yahoo Finance, display it in a user-friendly format, and download the data in CSV format.

## Prerequisites

Before getting started, you need to have Python and SQLite3 installed. If they are not installed, please follow these steps:

1. **Install Python:**  
   Download and install Python from [python.org](https://www.python.org/downloads/).
   
2. **Install SQLite3 (if not already installed):**  
   SQLite3 is included with Python, but if you need to install it manually, you can follow the instructions [here](https://www.sqlite.org/download.html).

3. **Install required Python packages:**

   Create a virtual environment (optional but recommended) and install Flask and other dependencies:

   ```bash
   pip install flask sqlite3 yfinance pandas
   ```

## Project Structure

```plaintext
/stock-data-fetcher
    /templates
        - index.html
        - result.html
    app.py
    stock_data.db (SQLite3 Database)
    README.md
```

- `app.py`: The main Flask application file.
- `templates/`: Folder containing HTML templates (`index.html`, `result.html`).
- `stock_data.db`: SQLite3 database to store user queries and stock data.
- `README.md`: This file.

## How to Run the Application

1. **Clone the repository**:

   ```bash
   git clone <your-repository-url>
   cd stock-data-fetcher
   ```

2. **Start the Flask application**:

   ```bash
   python app.py
   ```

   The application will run locally at `http://127.0.0.1:5000/`.


3. **Access the Website**:  
   Open your browser and go to `http://127.0.0.1:5000/`. This will load the homepage where you can enter the stock ticker symbol and the date range.

## How It Works

### 1. Index Page (`index.html`)
The `index.html` page contains a simple form where users can enter the stock ticker symbol and the date range for which they want the historical stock data.

### 2. Fetching Data from Yahoo Finance

Upon submitting the form, the Flask app uses the `yfinance` library to fetch the historical stock data from Yahoo Finance. The data is stored in an SQLite3 database (`stock_data.db`) for future reference.

### 3. Displaying Results (`result.html`)

The `result.html` page displays the fetched stock data in a tabular format. The user can view the data directly on the page.

### 4. Download CSV

The user can download the displayed data as a CSV file by clicking the "Download CSV" button.

## Database (SQLite3)

The application uses SQLite3 to store stock data. The database will be created automatically when you run the app.

### Schema

The SQLite3 database contains a simple table called `stocks` with the following columns:

- `id`: Integer, Primary Key
- `ticker`: Text
- `start_date`: Date
- `end_date`: Date
- `data`: Text (JSON format containing the stock data)

## Code Explanation

### 1. `app.py`

- **Imports and Setup**: 
  - Flask is imported to create the web app.
  - SQLite3 is used to store historical stock data.
  - `yfinance` is used to fetch the stock data.

- **Routes**:
  - `/`: Displays the homepage (`index.html`) with the form.
  - `/result`: Handles form submission, fetches the stock data, stores it in SQLite3, and renders the results in `result.html`.
  - `/download/<id>`: Allows users to download the stock data in CSV format.

### 2. `index.html`

A form where users can enter the stock symbol and date range.

### 3. `result.html`

Displays the fetched stock data in a table format and provides a download button for the CSV file.

## Example Usage

1. Visit the homepage at `http://127.0.0.1:5000/`.
2. Enter the stock symbol (e.g., `AAPL` for Apple) and the date range (e.g., `2020-01-01` to `2021-01-01`).
3. Click "Submit" to retrieve the historical stock data.
4. View the stock data on the results page.
5. Click the "Download CSV" button to download the data in CSV format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
