import requests
from bs4 import BeautifulSoup

# The number of syllables in the words you want to scrape for.
num_syllables = 19

# Website URL.
url = f'https://en.wiktionary.org/wiki/Category:English_{num_syllables}-syllable_words'
# CSS tag.
css_tag = 'a'
# Link text to click on.
link_text = 'next page'


while True:
    # Initialize an empty array to store the elements.
    elements = []

    # Make a request to the website.
    response = requests.get(url)

    # Parse the HTML content with BeautifulSoup.
    soup = BeautifulSoup(response.text, 'html.parser')

    soup.prettify()
    # print(soup)

    # Find all elements with the specified CSS tag and add them to the array.
    elements += soup.select('li a[href][title]:not([class]):not([id]):not([rel]):not([accesskey]):not(:has(span))')

    next_link = soup.select_one('a[href][title]:not([class]):not([id]):-soup-contains("next page")')

    # Find the link with the specified content and click on it.
    with open(f'{num_syllables}_syllable_words.txt', mode='a', encoding="utf-8") as file:
        for i in elements:
            file.write(i.text + "\n")

    if next_link:
        url = "https://en.wiktionary.org" + next_link['href']
        print(next_link['href'])

    # Repeat until no more links are found.
    else:
        print("next link no")
        print(next_link)
        break

for i in elements:
    print(i.text)
    print()

