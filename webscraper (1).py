import requests
from bs4 import BeautifulSoup
import csv
import sys 

SHADOWFOX_URL = "https://shadowfox.in/index.html" 
INTERNSHIP_TITLES = [
    'Data Science', 
    'Python Development', 
    'Web Development', 
    'UI/UX Design', 
    'AI/ML', 
    'Cyber Security', 
    'Android App Development', 
    'Java Development'
]
CSV_FILE_PATH = 'shadowfox_internships.csv'
FIELDNAMES = ['Domain', 'Description']

scraped_data = []

try:
    print(f"Attempting to fetch data from: {SHADOWFOX_URL}...")
    
    response = requests.get(SHADOWFOX_URL)
    response.raise_for_status() 
    
    soup = BeautifulSoup(response.text, 'html.parser')

    for title_text in INTERNSHIP_TITLES:
        title_element = soup.find(
            lambda tag: tag.name in ['h3', 'h4'] and tag.text.strip() == title_text
        )
        
        if title_element:
            card_container = title_element.find_parent().find_parent()
            
            title = title_element.get_text(strip=True)

            description_tag = card_container.find('p') 
            description = description_tag.get_text(strip=True) if description_tag else "Description Not Found"
            
            scraped_data.append({
                'Domain': title,
                'Description': description
            })

    if scraped_data:
        print("-" * 60)
        print("✅ Successfully Extracted Internship Data from ShadowFox:")
        print("-" * 60)
        
        for item in scraped_data:
            print(f"DOMAIN: {item['Domain']}")
            print(f"SUMMARY: {item['Description']}\n")
            
        try:
            with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
                
                writer.writeheader()
                
                writer.writerows(scraped_data)
            
            print("-" * 60)
            print(f"💾 Data successfully saved to {CSV_FILE_PATH}")
            
        except Exception as file_error:
            print("❌ Error saving CSV file:",file_error)
            
    else:
        print("❌ Could not extract any internship data. Check the target URL or HTML structure.")
        
except requests.exceptions.HTTPError as errh:
    print("-" * 60)
    print(f"❌ HTTP Error (Status Code {errh.response.status_code}): Ensure the URL is valid.")
except requests.exceptions.ConnectionError as errc:
    print("-" * 60)
    print(f"❌ Connection Error: Check your network connection.")
except requests.exceptions.Timeout as errt:
    print("-" * 60)
    print("❌ Timeout Error: Request took too long to respond.")
except requests.exceptions.RequestException as e:
    print("-" * 60)
    print(f"❌ A critical error occurred during the request: {e}")
    sys.exit(1)