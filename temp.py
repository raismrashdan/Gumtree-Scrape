import bs4, time, csv

from urllib.request import Request as uReq, urlopen
from bs4 import BeautifulSoup as soup

#sel_url = 'https://www.gumtree.com.au/s-real-estate/rent/k0c9296?'
my_url = 'https://www.gumtree.com.au/s-ad/west-melbourne/property-for-rent/1-bedroom-1-bathroom-carpark-apartment-near-southercorss-station/1257652438'
uClient = uReq(
    my_url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Grabs webpage
webpage = urlopen(uClient).read()

####################### SAVE HTML LOCALLY ########################################
# Saves html locally
# uRet(my_url, "test.txt")

############################ HTML PARSER ########################################
# Parses downloaded html file into an "html parsed" file
page_soup = soup(webpage, "html.parser")

# Class definitions
# Std
class_title = 'vip-ad-title__header'
class_price = 'user-ad-price__price'
class_nego = 'user-ad-price__price-negotiable user-ad-price__price-negotiable--with-price'
class_loc = 'vip-ad-title__location-address'
class_desc = 'vip-ad-description__content--wrapped'
# Attributes (var)
class_attr = 'vip-ad-attributes__item'
class_attr_desc = 'vip-ad-attributes__value'
class_attr_val = 'vip-ad-attributes__name'

# Get Data
# std
title = page_soup.find("h1",{"class":class_title})
price = page_soup.find("span",{"class":class_price})
nego = page_soup.find("span",{"class":class_nego})
loc = page_soup.find("span",{"class":class_loc})
desc = page_soup.find("span",{"class":class_desc})
# Attributes (var)
attr_container = page_soup.findAll("li",{"class":class_attr})
attributes = []
for attr in attr_container:
    attr_desc = attr.span.text
    attr_val = attr.span.nextSibling.text
    attribute = [attr_desc, attr_val]
    attributes.append(attribute)
# Check how many containers were found and grabbed
print(title.text)
print(price.text)
print(nego.text)
print(loc.text)
print(desc.text)
'''
# Define first container  
container = containers[0]

############################ READ PRODUCT DETAILS ########################################
print('test1')
for container in containers:
    # Read title
    class_title = 'user-ad-row-new-design__title-span'
    class_price = 'user-ad-price-new-design user-ad-row-new-design__price'
    class_loc = 'user-ad-row-new-design__location'
    class_

    title_container = container.findAll("span", {"class" : class_title})
    
    # Read brief
    class_brief = 'user-ad-row-new-design__description user-ad-row-new-design__description--regular'


    brand = container.
    
    prod_name = title_container[0].text

    action_container = container.findAll("div", {"class" : "item-action"})
    price_container = action_container[0].ul.findAll("li", {"class" : "price-current"})
    price1 = price_container[0].strong.text
    price2 = price_container[0].sup.text
    
    prod_price = float(price1.replace(",","")) + float(price2)

    print("########################################")
    print("Item Number",n, "n")
    
    print("brand: " + brand)
    print("prod_name: " + prod_name)
    print("prod_price: " + str(prod_price))
    print("\n")

    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'
########################################


# Get all thread links of a stock, and output to CSV
try:
    browser.find_element_by_class_name(class_normal).get_attribute("href")])


with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Print row to seperate each listing
    for stock in stock_code:
        # Write stock code
        writer.writerow(["NEW STOCK"])

        writer.writerow([stock])
        # Initialize vars
        pg_num = 1
        while pg_num < 150:
            url = 'https://hotcopper.com.au/asx/{}/discussion/page-{}?post_view=0'.format(stock, pg_num)
            browser.get(url)
            time.sleep(0.1)
            i = 1
            while i < 300:
                a = '//*[@id="hc-tab-content"]/div/div[2]/div[2]/table/tbody/tr[{}]/td[3]/strong/a'.format(i)
                try:
                    # Write thread URL in one cell
                    writer.writerow([browser.find_element_by_xpath(a).get_attribute("href")])
                except:
                    break
                i += 2
            pg_num += 1
            if(i == 1):
                break

# Takes a thread url as an input and scrapes all raw data

############ Data Structure ############
######## Stock data ########
# Mkt Cap
# Value
# Volume 

######## Comment data ########
### Meta Data ###
# Date
# Post ID
### Data ###
# Comment string
# Price at posting
# Sentiment
# Disclosure
# Likes
# Bulbs

######## User Data ########
# Username, Num of posts, Bulbs, Upvotes, Signature


######## Keyword Filter ########
Wanted, 

'''