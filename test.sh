declare -a routes=( "agencyList"
        "routeList/agencytag/sf-muni"
	"routeConfig/agencytag/sf-muni/routetag/E"
	"predictionByStopId/agencytag/sf-muni/stopId/15184"
	"predictionByStopTag/agencytag/sf-muni/routeTag/E/stopTag/5184"
	"predictionByStopTag/agencytag/sf-muni/routeTag/E/stopTag/5184/shortTitle"
	"predictionsForMultiStops/agencytag/sf-muni/routeTag1/N/stopTag1/6997/routeTag2/N/stopTag2/3909"
	"schedule/agencytag/sf-muni/routeTag/N"
	"vehicleLocation/agencytag/sf-muni/routeTag/E/time/0"
        "stats/thresholdtime/0.2" )

    for i in "${routes[@]}"
	do
		if curl -s --head  --request GET http://127.0.0.1:5002/app/$i | grep "200\|301" > /dev/null; then
			sleep 0.1
			echo "Endpoint "$i "is Live"
		else
			echo "Endpoint "$i "is not correct"
		fi
        done

