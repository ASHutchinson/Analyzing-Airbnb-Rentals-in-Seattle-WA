## Overview:
This project analyzed Seattle Airbnb listing data to try to find if there were patterns amongst successful properties. I tested whether the cleanliness rating for Entire Homes was higher than that for Private Rooms and compared the test results to Portland, OR and Vancouver, BC.

## Data:
This data was found on [insideairbnb.com](http://insideairbnb.com/get-the-data.html)
The id, listing url, scrape id, last scraped date, property name, description, and neighborhood overview can be seen on the table below. 

![Seattle Listings Overview](https://user-images.githubusercontent.com/79812486/121740651-407f3500-cab2-11eb-88b4-43bc570f10ed.png)

Dataframe contains:
4213 rows (listings)
74 columns

## Exploratory Data Analysis:
I explored the differences between Private Rooms and Entire Home listings. 81.3% of the listings in Seattle are for entire homes, 17.3% for private rooms, and 1.4% are for shared rooms and hotel rooms combined. 


![Room Types](https://user-images.githubusercontent.com/79812486/121745513-3e6ca480-cab9-11eb-8f32-f60e0fb367b4.png)
![Number of Listings per Review Scores Ratings](https://user-images.githubusercontent.com/79812486/121745526-44628580-cab9-11eb-893c-7b4ff1b859ba.png)
![Entire Home Neighborhoods](https://user-images.githubusercontent.com/79812486/121745537-47f60c80-cab9-11eb-926a-6712525892b4.png)
![Private Room Neighborhoods](https://user-images.githubusercontent.com/79812486/121745543-49bfd000-cab9-11eb-843d-94c12ae6be4a.png)



## Hypothesis Testing
**Scientific Question:** Hypothesis testing was conducted to determine whether the cleanliness rating for Entire Homes was higher than that for Private Rooms. 
**Null Hypothesis:** The cleanliness rating for Private Rooms is higher than the cleanliness rating for Entire Homes
**Alpha Level:** The significance level used was α=0.05
**Assumptions:** Reviewers were non-biased
**Two Samples:** Entire Home listings and Privatet Room Listings

## Conclusion 
Private Rooms are more likely to be cleaner than Entire Homes

## Technologies Used
* Numpy
* Matplotlib
* Pandas

## Next Steps
Find whether hosts that own multiple properties have higher ratings and scape website for overall stars rating, not just n/10 ratings. 
