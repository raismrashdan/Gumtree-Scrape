# This script gets individual listing URLs

import time, csv
from selenium import webdriver

browser = webdriver.Chrome()

# Get all URLs of a listing, and output to CSV
with open("gumtree_url.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Set starting page number
    pg_num = 49
    # *MANUALLY SET MAX PAGES!*. Can implement auto check, but easier to just check last listing by eye
    while pg_num < 51:
        # Put your wanted url below in the correct format
        url = 'https://www.gumtree.com.au/s-flatshare-houseshare/rent/page-{}/k0c18294'.format(pg_num)
        browser.get(url)
        time.sleep(0.1)
        num_listings_on_pg = 1
        # Assume max 24 listings on a page
        while num_listings_on_pg < 25:
            listing_url = '/html/body/div/div/div[3]/div/div[3]/main/section/div/div/a[{}]'.format(num_listings_on_pg)
            print(listing_url)
            try:
                # Write thread URL in one cell
                writer.writerow([browser.find_element_by_xpath(listing_url).get_attribute("href")])
            except:
                break
            num_listings_on_pg += 1
        pg_num += 1
        if(num_listings_on_pg == 1):
            break