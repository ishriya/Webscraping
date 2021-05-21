import requests
import bs4
import csv


one_star = []
two_star = []
three_star = []
four_star = []
five_star = []

url = 'https://books.toscrape.com/catalogue/page-{}.html'

for page_num in range(1, 51):
    scrape = url.format(page_num)
    res = requests.get(scrape)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for b in books:
        if 'star-rating One' in str(b):
            title_of_the_book = b.select("a")[1]['title']
            one_star.append(title_of_the_book)
        elif 'star-rating Two' in str(b):
            title_of_the_book = b.select("a")[1]['title']
            two_star.append(title_of_the_book)
        elif 'star-rating Three' in str(b):
            title_of_the_book = b.select("a")[1]['title']
            three_star.append(title_of_the_book)
        elif 'star-rating Four' in str(b):
            title_of_the_book = b.select("a")[1]['title']
            four_star.append(title_of_the_book)
        else:
            title_of_the_book = b.select("a")[1]['title']
            five_star.append(title_of_the_book)



print(one_star)


with open(r'C:\Users\ishri\Documents\python_practice\books.csv', "wt", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["One", "Two", "Three", "Four", "Five"])
    for row in zip(one_star,two_star,three_star,four_star,five_star):
         writer.writerow(row)