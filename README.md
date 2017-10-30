# sanfrancisco-bus-reverse-proxy-app"

![alt text](https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app/blob/master/workflowdiagram.PNG)

clone the repo:

`git clone https://github.com/satyamsah/sanfrancisco-bus-reverse-proxy-app.git`

`cd sanfrancisco-bus-reverse-proxy-app`

#### Build the project in two ways(use  one the the two steps at one time):

##### 1) using build.sh

`chmod 777 build.sh`
`./build.sh`

keep the terminal open to see the log 


##### 2) using docker-compose

`sudo docker-compose up`

keep the terminal open to see the log 

#### test the project (open a new terminal):

This is a test.sh file which calls different differnt curl command against server proxy endpoints :

`chmod 777 test.sh`
`./test.sh`

The sample result of tag can be found in the file `test_result.txt` 


#### Sample testing using browser

###### Sample List the stats:(threshold time is 0.002 seconds)

It will  have a response in json string in the browser:

http://localhost:5002/app/stats/thresholdtime/.0002

http://localhost:5002/app/stats/thresholdtime/.2


###### Sample List of routeList:
http://localhost:5002/app/routeList/agencytag/actransit


##### Http calls to server (Not a part of execution) and concept of cache:

As shown in the digram ,for the first time just after the app is booted up, http call wont be using the cache. After that, if the user hits exactly same uri with same values, within 40 secs, the reponse would be fetched from 'Local SQLLite DB'. It is very obvious that the cache has made the retrival of information massively fast. The time out of the cache is 40 seconds.













