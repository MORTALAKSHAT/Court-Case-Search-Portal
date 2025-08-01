🏛️ Court Case Search Portal
A lightweight and functional web-based portal that simulates the court case search process using a beautiful Tailwind CSS form, a Flask backend, SQLite database logging, and CSV export functionality.

This project was built for Internship Task 1: Court Data Fetcher & Mini Dashboard.

💡 Functional Highlights
🌐 Web UI with Tailwind CSS

📬 Flask backend server

🧾 Simulated court case data with:

Party names

Filing date

Next hearing date

Judgment/order PDF link

💽 Query logging into SQLite

📥 CSV export of all queries via /export route

💬 JSON API endpoint for async use

🎯 Fully ready for demo or extension with live scraping

📸 Demo Preview
🧱 Project Structure
court-data-fetcher-dashboard/
├── app.py                  # Flask backend logic
├── queries.db              # SQLite DB (auto-created)
├── templates/
│   └── form.html           # Tailwind HTML form interface




🚀 How to Run
1. Clone the project
https://github.com/MORTALAKSHAT/Court-Case-Search-Portal.git



2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux




3. Install required libraries
pip install flask pandas




4. Run the Flask app
python app.py




Visit in browser:
👉 http://localhost:5000

💻 Usage
Fill in Case Type, Case Number, and Filing Year

Click Search

A simulated response will show:

Parties involved

Dates

Downloadable PDF

All queries are logged in queries.db

📁 CSV Export
Download all search logs:
👉 http://localhost:5000/export

This will return case_logs.csv with:

Case type

Case number

Filing year

Timestamp

Raw dummy response

📌 Notes
This project uses dummy case data for simulation purposes.

No actual court portals were scraped due to CAPTCHAs and legal restrictions.

You can plug in real scraping logic using requests + BeautifulSoup or Selenium.

📦 Features You Can Add
/history route to view queries in HTML

Real court portal integration

PDF viewer inside browser

Admin panel or log filters

Export to PDF

👨‍💻 Author
Made by Akshat digraskar

For Internship Task 1 - Court Data Fetcher & Dashboard

📃 License
MIT License – free to use, modify and share.
