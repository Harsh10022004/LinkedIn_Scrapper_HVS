# LinkedIn Profile Scraper

This project is a LinkedIn profile scraper that extracts key information such as Name, Bio, Experience, Education, Certifications, Projects, Volunteer Experience, and Skills from LinkedIn profiles listed in an Excel file. The scraped data is saved to a CSV file.

## Prerequisites
Ensure you have the following installed:
- Python
- Google Chrome
- ChromeDriver (installed automatically using `webdriver-manager`)

## Required Libraries
Install all dependencies using:
```bash
pip install selenium webdriver-manager pandas beautifulsoup4 openpyxl
```

## How to Use
1. Clone the repository:
```bash
git clone https://github.com/Harsh10022004/LinkedIn_Scrapper_HVS.git
cd LinkedIn_Scrapper_HVS
```

2. Update your LinkedIn credentials in the script:
```python
linkedin_username = "your-email@example.com"
linkedin_password = "your-password"
```

3. Run the scraper:
```bash
python linkedscraperassignment.py
```

4. The scraped data will be saved in `scraped_output.csv`.

## Output
The CSV file will contain the following columns:
- LinkedIn URL
- Name
- Bio
- Socials
- Experience
- Education
- Certifications
- Projects
- Volunteer Experience
- Skills

## Note
- Ensure your firewall or antivirus isn't blocking ChromeDriver.
- LinkedIn may have scraping protections, so use this tool responsibly and within LinkedIn's guidelines.

## Author
[Harsh Vardhan Singhania](https://github.com/Harsh10022004)

