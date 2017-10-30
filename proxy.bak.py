from flask import Flask, jsonify, make_response, request
import requests
import json
import time
import xmltodict
import sqlite3
import requests_cache


app = Flask(__name__)

requests_cache.install_cache('proxy_cache', backend='sqlite', expire_after=40)


def convertToJSON(response):
    """Convert responses to json data."""
    to_dict = dict()
    to_dict = xmltodict.parse(response)

    response = json.dumps(to_dict, sort_keys=True,
                          indent=4, separators=(",", ":"))
    return response


hitsCollection={};
hitsCollection["/app/agencyList/"]=0;
hitsCollection["/app/routeList/"]=0;
hitsCollection["/app/routeConfig/"]=0;
hitsCollection["/app/predictionByStopId/"]=0;
hitsCollection["/app/predictionByStopTag/"]=0;
hitsCollection["/app/predictionsForMultiStops/"]=0;
hitsCollection["/app/schedule/"]=0;
hitsCollection["/app/messages"]=0;
hitsCollection["/app/vehicleLocation/"]=0;


requestime={};
requestime["/app/agencyList/"]=0;
requestime["/app/routeList/"]=0;
requestime["/app/routeConfig/"]=0;
requestime["/app/predictionByStopId/"]=0;
requestime["/app/predictionByStopTag/"]=0;
requestime["/app/predictionsForMultiStops/"]=0;
requestime["/app/schedule/"]=0;
requestime["/app/messages"]=0;
requestime["/app/vehicleLocation/"]=0;



#Command "agencyList"
@app.route('/app/agencyList/', methods=['GET'])
def getAllAgencies():
    url='http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList'

    print("inside AGENCYLIST")
    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/agencyList/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")
    #print(requestime.get("/app/agencyList/"))

    val=hitsCollection.get("/app/agencyList/");
    hitsCollection["/app/agencyList/"]=val+1;


    result=convertToJSON(response.text)
    return result

    # print(type(response))
    # print(type(response.text))
    # print(response.text)

    # http = urllib3.PoolManager()
    # r = http.request('GET', 'http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList')
    # r.content_type="text/xml"
    # print(r.xml)
    # print(type(r.data))
    # return r.data


    # req = urllib.request.Request('http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList')
    # with urllib.request.urlopen(req) as response:
    #     the_page = response.read()
    #     return  the_page


#Command "routeList"
@app.route('/app/routeList/agencytag/<agency_tag>', methods=['GET'])
def getRouteList(agency_tag):

    url="http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a="+agency_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/routeList/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")
	
    val=hitsCollection.get("/app/routeList/");
    hitsCollection["/app/routeList/"]=val+1;

    result=convertToJSON(response.text)
    return result

#Command "routeConfig"
@app.route('/app/routeConfig/agencytag/<agency_tag>/routetag/<route_tag>', methods=['GET'])
def getRouteConfig(agency_tag,route_tag):

    url="http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a="+agency_tag+"&r="+route_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/routeConfig/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/routeConfig/");
    hitsCollection["/app/routeConfig/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictions" ByStopIdWithAgency
@app.route('/app/predictionByStopId/agencytag/<agency_tag>/stopId/<stop_Id>', methods=['GET'])
def getPredictionOfStopByStopIdWithAgency(agency_tag,stop_Id):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a="+agency_tag+"&stopId="+stop_Id

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionByStopId/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionByStopId/");
    hitsCollection["/app/predictionByStopId/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictions" ByStopIdWithAgencyWithRoute
@app.route('/app/predictionByStopId/agencytag/<agency_tag>/stopId/<stop_id>/routeTag/<route_tag>', methods=['GET'])
def getPredictionOfStopByStopIdWithAgencyWithRoute(agency_tag,stop_id,route_tag):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a="+agency_tag+"&stopId="+stop_id+"&routeTag="+route_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionByStopId/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionByStopId/");
    hitsCollection["/app/predictionByStopId/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictions" ByStopTagWithAgencyWithRoute
@app.route('/app/predictionByStopTag/agencytag/<agency_tag>/routeTag/<route_tag>/stopTag/<stop_tag>', methods=['GET'])
def getPredictionOfStopByStopTagWithAgencyWithRoute(agency_tag,route_tag,stop_tag):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a="+agency_tag+"&r="+route_tag+"&s="+stop_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionByStopTag/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionByStopTag/");
    hitsCollection["/app/predictionByStopTag/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictions" ByStopTagWithAgencyWithRouteAndShortTitle
@app.route('/app/predictionByStopTag/agencytag/<agency_tag>/routeTag/<route_tag>/stopTag/<stop_tag>/shortTitle', methods=['GET'])
def getPredictionOfStopByStopTagWithAgencyWithRouteAndShortTitle(agency_tag,route_tag,stop_tag):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a="+agency_tag+"&r="+route_tag+"&s="+stop_tag+"&useShortTitles=true"

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionByStopTag/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionByStopTag/");
    hitsCollection["/app/predictionByStopTag/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictionsForMultiStops"
#in this case only two routes
@app.route('/app/predictionsForMultiStops/agencytag/<agency_tag>/routeTag1/<route_tag1>/stopTag1/<stop_tag1>/routeTag2/<route_tag2>/stopTag2/<stop_tag2>', methods=['GET'])
def getPredictionsForMultiStops(agency_tag,route_tag1,stop_tag1,route_tag2,stop_tag2):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a="+agency_tag+"&stops="+route_tag1+"|"+stop_tag1+"&stops="+route_tag2+"|"+stop_tag2
    #sForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909

    print("two stops")

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionsForMultiStops/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionsForMultiStops/");
    hitsCollection["/app/predictionsForMultiStops/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "predictionsForMultiStops"
#in this case only one routes
@app.route('/app/predictionsForMultiStops/agencytag/<agency_tag>/routeTag/<route_tag>/stopTag/<stop_tag>', methods=['GET'])
def getPredictionsForMultiStopsForOneRoute(agency_tag,route_tag,stop_tag,):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a="+agency_tag+"&stops="+route_tag+"|"+stop_tag
    #sForMultiStops&a=sf-muni&stops=N|6997&stops=N|3909

    print("one stop")

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/predictionsForMultiStops/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/predictionsForMultiStops/");
    hitsCollection["/app/predictionsForMultiStops/"]=val+1;


    result=convertToJSON(response.text)
    return result


#Command "schedule"
@app.route('/app/schedule/agencytag/<agency_tag>/routeTag/<route_tag>', methods=['GET'])
def getSchedule(agency_tag,route_tag):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a="+agency_tag+"&r="+route_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/schedule/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/schedule/");
    hitsCollection["/app/schedule/"]=val+1;


    result=convertToJSON(response.text)
    return result


#Command "messages"
@app.route('/app/messages/agencytag/<agency_tag>/routeTag/<route_tag>', methods=['GET'])
def getMessages(agency_tag,route_tag):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=messages&a="+agency_tag+"&r="+route_tag

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/messages/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/messages/");
    hitsCollection["/app/messages/"]=val+1;


    result=convertToJSON(response.text)
    return result

#Command "vehicleLocations"
@app.route('/app/vehicleLocation/agencytag/<agency_tag>/routeTag/<route_tag>/time/<localtime>', methods=['GET'])
def getVehicleLocation(agency_tag,route_tag,localtime):
    url="http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a="+agency_tag+"&r="+route_tag+"&t="+localtime
    print(url)
    print("Inside Location")

    time1=time.time()
    response=requests.get(url)
    time2=time.time()
    requestime["/app/vehicleLocation/"]=float(time2-time1)
    print("Time Consumed for response: {0} / Used Cache: {1}".format(requestime["/app/routeList/"], response.from_cache))
    print("-----------------END-------------------------")
    print("")

    val=hitsCollection.get("/app/vehicleLocation/");
    hitsCollection["/app/vehicleLocation/"]=val+1;


    result=convertToJSON(response.text)
    return result


@app.route('/app/stats/thresholdtime/<threshold_time>', methods=['GET'])
def getStats(threshold_time):
    finalHitDict={}
    finalSlowReq={}
    for endpoint,hits in hitsCollection.items():
       if hits!=0:
           finalHitDict[endpoint]=hits
           if requestime.get(endpoint)>float(threshold_time):
               finalSlowReq[endpoint]=float(str(round(requestime.get(endpoint), 4)))

    strFinalHitDict=json.dumps(finalHitDict)
    strFinalSlowReq=json.dumps(finalSlowReq)
    finalStat='{"slow_requests":'+strFinalSlowReq+',"queries":'+strFinalHitDict+'}'
    print(finalStat)
    print("-----------------END-------------------------")
    print("")
    return finalStat

@app.route('/', methods=['GET'])
def hello():
    return "hello proxy service is up"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002, debug=True)

