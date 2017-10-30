# sanfrancisco-bus-reverse-proxy-app

![alt text](https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app/blob/master/workflowdigram.png)

clone the repo:

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

This is a test.sh file which calls different curl command against server proxy endpoints.It shows whether thestate the endpoint queried :

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


### Http calls to server and concept of cache using SQLLite DB:

As shown in the diagram ,for the first time just after the service has started up, http call wont be using the cache. After that, if the user hits exactly same uri with same values, within 40 secs, the reponse would be fetched from 'Local SQLLite DB'.After 40 seconds, the http request will call the server over the wire. It is very obvious that the cache has made the retrival of information massively fast. It usually takes .20 to .5 seconds to get a response from http calls to enpoint server, but it averagely takes less than .0022 to .0045 seconds to fetch the saved response from the 'SQLLite cache db'. The time-out of the cache is 40 seconds and then the request would be sent to the nextbus server. 













