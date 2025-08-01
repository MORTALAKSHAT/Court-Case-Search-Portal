import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas as pd

def generate_dummy_data():
    data = [
        {"Case No": "CIV-2023-0001", "Filing Date": "2023-06-01", "Case Type": "Civil", "Court Name": "District Court A", "Status": "Pending"},
        {"Case No": "CRL-2023-0002", "Filing Date": "2023-06-05", "Case Type": "Criminal", "Court Name": "District Court B", "Status": "Closed"},
        {"Case No": "LAB-2023-0003", "Filing Date": "2023-06-12", "Case Type": "Labour", "Court Name": "Labour Court", "Status": "Ongoing"},
        {"Case No": "FAM-2023-0004", "Filing Date": "2023-06-20", "Case Type": "Family", "Court Name": "Family Court", "Status": "Pending"},
        {"Case No": "CIV-2023-0005", "Filing Date": "2023-06-23", "Case Type": "Civil", "Court Name": "District Court A", "Status": "Judgment Reserved"},
        {"Case No": "CRL-2023-0006", "Filing Date": "2023-06-28", "Case Type": "Criminal", "Court Name": "Sessions Court", "Status": "Adjourned"},
        {"Case No": "LAB-2023-0007", "Filing Date": "2023-07-01", "Case Type": "Labour", "Court Name": "Labour Court", "Status": "Pending"},
        {"Case No": "FAM-2023-0008", "Filing Date": "2023-07-04", "Case Type": "Family", "Court Name": "Family Court", "Status": "Hearing Scheduled"},
        {"Case No": "CIV-2023-0009", "Filing Date": "2023-07-06", "Case Type": "Civil", "Court Name": "District Court C", "Status": "Closed"},
        {"Case No": "CRL-2023-0010", "Filing Date": "2023-07-10", "Case Type": "Criminal", "Court Name": "Sessions Court", "Status": "Under Trial"},
    ]

    df = pd.DataFrame(data)
    df.to_csv("court_cases.csv", index=False)
    print("✅ Dummy court_cases.csv created successfully.")

if __name__ == "__main__":
    generate_dummy_data()
def scrape_faridabad_ecourts():
    url = "https://districts.ecourts.gov.in/faridabad/daily-case-status"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers,timeout=10)

    soup = BeautifulSoup(response.content, "html.parser")

    # This section may need adjustment if they change the page layout
    tables = soup.find_all("table")

    if not tables:
        print("❌ No tables found on the page.")
        return

    table = tables[0]  # usually the first table is the correct one
    rows = table.find_all("tr")

    data = []
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 5:
            data.append({
                "Case No": cols[0].get_text(strip=True),
                "Filing Date": cols[1].get_text(strip=True),
                "Case Type": cols[2].get_text(strip=True),
                "Court Name": cols[3].get_text(strip=True),
                "Status": cols[4].get_text(strip=True),
            })

    if data:
        df = pd.DataFrame(data)
        df.to_csv("court_cases.csv", index=False)
        print("✅ Scraped and saved court_cases.csv")
    else:
        print("⚠️ No data extracted.")

if __name__ == "__main__":
    scrape_faridabad_ecourts()
