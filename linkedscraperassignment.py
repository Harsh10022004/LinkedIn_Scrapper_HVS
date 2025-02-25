from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver with options
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-features=WebRTC")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-background-networking")
    driver = webdriver.Chrome(options=options)
    return driver

driver = web_driver()

import pandas as pd

df = pd.read_excel('Assignment.xlsx')

# Extract LinkedIn URLs
linkedin_urls = df['LinkedIn URLs'].tolist()
df

linkedin_username = "kraj28822@gmail.com"
linkedin_password = "Harsh@#2004"

def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    driver.find_element(By.ID, "username").send_keys(linkedin_username)
    driver.find_element(By.ID, "password").send_keys(linkedin_password)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

login_to_linkedin()

from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

def scrape_linkedin_profile(url):
    try:
        driver.get(url)
        time.sleep(7)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        try:
            name = driver.find_elements(By.CSS_SELECTOR, 'h1[class*="inline t-24 v-align-middle break-words"]')
            name = name[0].text.strip() if name else ''
        except (IndexError, NoSuchElementException):
            name = ''

        try:
            bio = soup.select('main section:has(#about) div:nth-of-type(3) span:nth-of-type(1)')
            bio = bio[0].get_text(strip=True) if bio else ''
        except (IndexError, AttributeError):
            bio = ''

        experience, education, socials, certifications, projects, volunteer_experience, skills = [], [], [], [], [], [], []

        try:
            job_titles = soup.select('main section:has(#experience) div.display-flex.align-items-center.mr1.t-bold span:nth-of-type(1)')
            companies = soup.select('main section:has(#experience) span.t-14.t-normal span:nth-of-type(1)')
            experience = {job_titles[i].get_text(strip=True): companies[i].get_text(strip=True) for i in range(min(len(job_titles), len(companies)))}
        except (IndexError, AttributeError):
            experience = {}

        try:
            schools = soup.select('main section:has(#education) div.display-flex.align-items-center.mr1.hoverable-link-text.t-bold span:nth-of-type(1)')
            degrees = soup.select('main section:has(#education) span.t-14.t-normal span:nth-of-type(1)')
            education = {schools[i].get_text(strip=True): degrees[i].get_text(strip=True) for i in range(min(len(schools), len(degrees)))}
        except (IndexError, AttributeError):
            education = {}

        try:
            certs = soup.select('main section:has(#licenses_and_certifications) div.display-flex.align-items-center.mr1.t-bold span:nth-of-type(1)')
            certifications = [cert.get_text(strip=True) for cert in certs]
        except (IndexError, AttributeError):
            certifications = []

        try:
            project_titles = soup.select('main section:has(#projects) div.display-flex.align-items-center.mr1.t-bold span:nth-of-type(1)')
            projects = [proj.get_text(strip=True) for proj in project_titles]
        except (IndexError, AttributeError):
            projects = []

        try:
            volunteer_roles = soup.select('main section:has(#volunteering_experience) div.display-flex.align-items-center.mr1.t-bold span:nth-of-type(1)')
            volunteer_experience = [role.get_text(strip=True) for role in volunteer_roles]
        except (IndexError, AttributeError):
            volunteer_experience = []

        try:
            skills_list = soup.select('main section:has(#skills) div.display-flex.align-items-center.mr1.hoverable-link-text.t-bold span:nth-of-type(1)')
            skills = [skill.get_text(strip=True) for skill in skills_list]
        except (IndexError, AttributeError):
            skills = []

        return {
            'LinkedIn URL': url,
            'Name': name,
            'Bio': bio,
            'Socials': socials,
            'Experience': experience,
            'Education': education,
            'Certifications': certifications,
            'Projects': projects,
            'Volunteer Experience': volunteer_experience,
            'Skills': skills
        }

    except (TimeoutException, WebDriverException) as e:
        print(f"Error loading page {url}: {e}")
        return {'LinkedIn URL': url, 'Error': str(e)}
    except Exception as e:
        print(f"Unexpected error scraping {url}: {e}")
        return {'LinkedIn URL': url, 'Error': 'Unexpected error'}

results = []
# first_six_urls = df['LinkedIn URLs'].head(6)
for url in df['LinkedIn URLs']:
    try:
        profile_data = scrape_linkedin_profile(url)
        results.append(profile_data)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Convert results to DataFrame and save to CSV
results_df = pd.DataFrame(results)
updated_results_df = results_df.to_csv('scraped_output.csv', index=True)
updated_results_df
