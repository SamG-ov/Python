from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify()) #all the html in pretty format
print(soup.a) #first anchor tag
print(soup.p) #first paragraph tag

#find all the anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


for tag in all_anchor_tags:
    print(tag.getText()) #all anchor tag text
    print(tag.get("href")) #all anchor tag link

heading = soup.find(name="h1", id="name")
print(heading) #.string / getText()

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

comapny_url = soup.select_one(selector="p a") #first matching item / select() gives all matching item in a list
print(comapny_url)

name = soup.select_one(selector="#name")
print(name)

head = soup.select(".heading")
print(head)

#<form method="get" action="/search/">
# <input type="text" name="q" maxlength="255" value=""></input>
#</form> 

#form_tag = soup.find("input")
#max_length = form_tag.get("maxlength")