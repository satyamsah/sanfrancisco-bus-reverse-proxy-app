# sanfrancisco-bus-reverse-proxy-app

![alt text](https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app/blob/master/workflowdia.png)


I have a reverse proxy service that is a python file " proxy-net.py " which does all the heavy lifting tasks like taking request from custom uris and proxying the requests to either a cache db or to the remote sf-bus server. The docker-compose has been used to run the whole proxy service. You can use build.sh as an alternative approach to run the service. The test.sh is used to test the endpoints.

The technology used are :

python and related libraries: reverse-proxy service

sqlite db : cache

dockerfile and docker-compose : to start the reverse-proxy service

shell scripts : to start and test the service



#### clone the repo:

`git clone https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app.git`

`cd sanfrancisco-bus-reverse-proxy-app`

#### Build the project in two ways(use only one of the two steps at one time):

##### 1) using build.sh

`chmod 777 build.sh`

`./build.sh`

keep the terminal open to see the log 

##### 2) using docker-compose

`sudo docker-compose up`

keep the terminal open to see the log 


#### test the project (open a new terminal):

This is a test.sh file which calls different curl commands against server proxy endpoints.It shows  the state the endpoint queried (live or not live):

`chmod 777 test.sh`

`./test.sh`

The sample result of tag can be found in the file [test_result.txt](https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app/blob/master/test_result.txt)


### Sample testing using browser

#### Sample List the stats:

It will  have a response in json string in the browser.The last float number in the endpoint uri is the threshold value of https response-delay in terms of seconds. So, because of this, the result will only have those endpoints under "slow_requests:" key whose reponse time is greater than the threshold seconds:


http://localhost:5002/app/stats/thresholdtime/.2

http://localhost:5002/app/stats/thresholdtime/.0002


Sample result [stats_response.txt](https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app/blob/master/stats_response.txt)

#### Sample reponse of routeList where acency tag is 'actransit' :

http://localhost:5002/app/routeList/agencytag/actransit


### Http calls to server and concept of cache using SQLite DB:

As shown in the diagram ,for the first time after the reverse-proxy-service has started up, the request  won't be using the cache. But, after the first call, if the user hits exactly same uri with same values, within 40 secs, the response would be fetched from 'Local SQLite DB'. I set the time-out of the cache as 40 seconds. After 40 seconds, the http request will call the sf-bus-server over the wire. It is very obvious that the cache has made the retrival of information massively fast. It usually takes .20 to .5 seconds to get a response from http calls to enpoint sf-bus-server, but it averagely takes less than .0022 to .0045 seconds to fetch the saved response from the 'SQLite cache db'.













