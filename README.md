# Pipeline-64

                   <img src="https://i.ytimg.com/vi/uMCCxuGIGtw/hqdefault.jpg">



## Description

This is a **web scraping** and **APIs** project for *Ironhack*. 
The purpose of the project is to enrich the data stored in a dataset with external data extracted from an API and webscraping. The data set I selected contains real estate data for the city of Kuala Lumpur, Malasya. The API provides real-time exchange rate data to allow the user of the program to choose in which currency they want to see the most expensive / average price for a house of type x and x number of rooms.


## Program Tasks

The program returns:

* The average price (in a currency of choice) for a house with x number of rooms
* The maximum price for a house with those attributes number of rooms


## How to execute the program

In order to execute the program, go on the Terminal and type <python3 main.py>.
You must add three flags for each of the parameters: -h "type of home", -r <number of rooms> and -c for "currency"

Example:
```bash
python3 main.py -h "Flat" -r 3 -c "USD"
```



## Authors 

Jaime Sanz


## Documentation

The data comes from Kaggle (more specifically it is data that has been collected through web scraping of various Real Estate webpages and platforms in Kuala Lumpur)
[Kaggle-Global Property Listings in Kuala Lumpur](https://www.kaggle.com/dragonduck/property-listings-in-kuala-lumpur)



