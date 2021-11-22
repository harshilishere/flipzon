# Flipzon
Currently inventory and sales will be working. I regret not being able to exactly complete the assingment due to some issues. Its already been more than a week so
submitting it anyways today.

The sale will be made only if there is sufficient inventory. If the sale is made then the qty will be deducted from the inventory. In this project for the first time
I tried the django orm in such a depth. I normally use mongodb as a databse. I have tired to refer a lot of documentation and tutorials to write better code as possible
Here are some thoughts of how I would do in real world.
Assuming there are atleast a thousand deliveries to be done everyday, I would rather use something like Fast API with docker and run it in a seperate containers.
OR writing simple lambda functions thus saving a lot of cost. Using django for these kind of things today will be going through monolothic design and that would
probably not be a prefrable way to do it. Monolithic will only be relavant in case its an mvp or way too big project. 

There will be a seperate service that would run once every 24-hrs to make routes for the deliveries. Not taking map service from google that would be really costly,
instead taking from locationiq or mapmyindia or maybe setup OSM would be a better choice. Now when in the morning the teams are ready to start deliveries that time
the time of delivery with refrence to traffic of the area the time will be decided by the system. The micro-management of time per delivery is practically not feasible
until drones or something takes place. So there will always be an error of margin for time no matter what we do.

I am okay with choosing and designing MongoDb as my database. Please just let me know and i will draw the archicture of  mongodb if needed for this. I am sure that
wouldn't take time because its something i have to process it in my head. Can also wrote queries for that and reports, that might take a little time.

My approach is always to take time to write queries instead of writing efficient codes. As mongodb is a query rich database, we can get many things sorted right in the
query. And it will be faster then whatever or howsoever we code.

Hope this will be considered.
