from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'
filename = "graphic cards.csv"
f = open(filename, "w")
headers = "Brand, Title, Shipping\n"
f.write(headers)


#print(my_url)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#print(page_soup.prettify())
#print(page_soup.h1)
#page_soup.p
#page_soup.find_all()
#print(page_soup.body.span)

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

#print(len(containers))
#print(containers[0])
#container = containers[0]
#print(container.find("div", {"class": "item-info"}))
for container in containers:
    brand = container.find("div", {"class": "item-info"}).div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    title = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("Brand: " + str(brand))
    print("Title " + str(title))
    print("Shipping: " + str(shipping) + "\n")

    f.write(brand + "," + title.replace(",", "|") + "," + shipping + "\n")

f.close()

