import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from parser import parse_data

# Set up the browser driver
driver = webdriver.Chrome()

# Navigate to naver.com
driver.get("https://naver.com")

# Wait for the page to fully load
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.ID, "footer")))

# Find the search box and enter a search term
search_box = driver.find_element("id", "query")
search_box.send_keys("비건 레스토랑")

# Find the search button and click it
search_button = driver.find_element("id", "search_btn")
search_button.click()

# Wait for the search results page to load
driver.implicitly_wait(10)

# Define the sections to extract
sections = [
    ('Advertisement', 'brand_search section brand_new_ui'),
    ('Power Link', 'ad_section section _pl_section bg_type_v2'),
    ('English Dictionary', 'api_subject_bx'),
    ('Related Search', 'sc_new cs_same_different _kgs_same_different'),
    ('Stock Information', 'api_subject_bx'),
    ('Related Stocks', 'api_subject_bx'),
    ('Business Sites', 'ad_section section _bz_section bg_type_v2'),
    ('Namu Wiki', 'total_wrap api_ani_send')
]

parsed_results = []

# Iterate through the sections and extract them
for title, css_class in sections:
    try:
        section = driver.find_element(By.CSS_SELECTOR, f".{css_class.replace(' ', '.')}")
        parsed_section = parse_data(section)  # Pass the section element
        parsed_results.append(f"{title}:\n{parsed_section}\n")
    except Exception as e:
        parsed_results.append(f"{title} not found.\n")

# Save the parsed results to a file with a dynamic name based on a counter
counter = 0
while os.path.exists(f"results_{counter}.txt"):
    counter += 1

with open(f"results_{counter}.txt", "w") as output_file:
    output_file.writelines(parsed_results)

# Close the browser
driver.quit()
