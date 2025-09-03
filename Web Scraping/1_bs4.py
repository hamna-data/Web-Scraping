from bs4 import BeautifulSoup

with open("file.html", "r") as f:
    html = f.read()


soup = BeautifulSoup(html , 'html.parser')

# print(soup.prettify())

# print(soup.title)
print(soup.title.text)

# print(soup.find_all('a'))  # all the anchor tags
