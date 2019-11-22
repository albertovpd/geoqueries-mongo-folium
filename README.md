# geoqueries-mongo-folium

Use Mongo, Scipy (Pandas), the Haversine equation and finding the middle points of geocoordinates to work with geoqueries and find the perfect location in the world for your new company, taking into account the preferences of workers.
![alt text](https://github.com/albertovpd/geoqueries-mongo-folium/blob/master/output/final%20with%20perfect%20spot.png "final result")

# Description of the task:

You recently created a new company in the `GAMING industry`. The main building needs to be close of:
- modern design companies which raised more than 1M€
- commuting facilities (airports, train station, etc)
- starbucks
- vegan restaurants
- kindergartens 
You are given a dataset with company names, number of offices, number of employees, founds, etc. Use mongo and pymongo to perform the right queries in first instance and be careful, mongo is not sql.

# My solution:
- Filter my dataset performing a huge query to get the geospatial coordinates of the filtered locations.
- Find great datasets of public transport facilities and starbucks with geospatial coordinates.
- Clean all datasets with pandas.
- I had troubles creating geoindexes in Mongo Compass, so I did the "math" way. First I tried with Scipy library, but finally I used haversine equation to get the closest distance between gps coordinates (taking into accout Earth surface is curved).
- Once the closest airport and starbucks to all my desired offices are found, create a weight function to decide what place is more suitable due to my preferences.

- Sort my dataset by the weight function.
- With folium, centre the map in the top place, and also draw the other 5 more suitable in the world (taking into accout my data).

![alt text](https://github.com/albertovpd/geoqueries-mongo-folium/blob/master/output/dataframe.png "dataframe")

![alt text](https://github.com/albertovpd/geoqueries-mongo-folium/blob/master/output/final%20without%20perfect%20spot.png "without perfect spot")

# Further improvements
- Use of APIs:
    - Obtain the real incomes of all companies in €.
    - Large-scale my problem.
        - Use several APIs to enrich my dataset with vegan restaurants and kindergartens.
        - Insert the new elements in my weight function.
        - Use the _init_ function to insert via terminal coordinates and get the closest place that accomplished all mentioned before.
