# Data analysis - Book store

This is a self-project to perform data analysis from scratch.
Collection of data is performed via web scraping from https://toscrape.com/ using BeautifulSoup. https://toscrape.com/ is a safe website to learn scraping.


#### Problem ####

The number of customers are declining and the stakeholders would like to know the reasons and how to improve their bookstore.

#### Steps ####

<li> I planned to web scrape the site to collect the list of books as per their star ratings. </li>

<li> Web scraped the dummy bookstore by creating a BeautifulSoup object </li>
   
```
   soup = bs4.BeautifulSoup(res.text, 'lxml')
   books = soup.select(".product_pod")
```    
<li> Maintained a list of books which falls under different star ratings </li>
<li> Converted list into csv file for data analysis </li>
<li> The collected data is converted into bubble chart for better illustrations using Tableau desktop. </li>

#### Observations ####
<ol>
<li> The bubble chart shown below represents that most of the books in the bookstore are 3 star rated </li>
  
  
<p align="center"><img src="https://github.com/ishriya/data_analysis_bookstore/blob/main/No.%20of%20books.png" width="400" /></p>

<li> The store has almost all collection of books ranging from 1 star to 5 star ratings. </li>
<li> However, the proportion of books that have less than equal to 3 star ratings are 70% which is a very high percenatge as compared to high rated books. </li>
</ol>


<p align="center"><img src="https://github.com/ishriya/data_analysis_bookstore/blob/main/percentage_of_ratings.png" width="500" /></p>

  
#### Action to be taken ####
  
1. Based on the observation, the store should work more towards imporving their 4 and 5 star rating books.
2. Improving their inventory based on customer preferences and buying patterns using more data analysis could be helpful.
3. There are many book recommendation platforms and publically available datasets which can be used in further stocking up their bookstore to increase number of customers.
4. The store can implement a sale/discount and analyse the impact of sales on customers.
 

###### Note ###### 
The data collected is from a dummy bookstore for my learning purposes, hence it may not represent real world data.
