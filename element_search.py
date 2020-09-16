
def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5)) # prints False
import requests
from bs4 import BeautifulSoup
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
filename = input("File to save to: ")

with open(filename, 'w') as f:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            f.write(story_heading.a.text.replace("\n", " ")).strip()
        else:
            f.write(story_heading.contents[0].strip())
print(filename)
