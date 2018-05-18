#A short program that fetches data from the Estimote cloud and exports it into a csv file.
#HUBBS Labs
#By: Siman Shrestha

import requests
import csv
import ast


#---Get visit duration for BLUEBERRY BEACON ---

url_1 = 'https://cloud.estimote.com/v2/analytics/devices/cc95d1d6b8587f69bb2d353a599fcd00/duration?from=1520812800&to=1523232000&granularity=hourly'
response_1 = requests.get(url_1,auth = ('hubbs-beacon-1g4','9dd89caad492d2a7d4b4c023d591cc17'))

url_1 = 'https://cloud.estimote.com/v2/analytics/devices/cc95d1d6b8587f69bb2d353a599fcd00/duration?from=1520812800&to=1523232000&granularity=hourly'
response_1 = requests.get(url_1,auth = ('hubbs-beacon-1g4','9dd89caad492d2a7d4b4c023d591cc17'))

#	print(response_3.text) #Prints data to terminal
# 	print("\n")

#	Converts the dictionary string output of response.text into an actual dictionary
allData = ast.literal_eval(response_1.text)
data = allData['data']
print("-------------------------------------------------------------")
print("EXPORTING CSV: Get Visit Duration for Blueberry Beacon: \n")
print("-------------------------------------------------------------")

try:
	keys = data[0].keys() #keys #['date','count']
	with open('BlueberryProximityData.csv','wb') as output_file:
		thewriter = csv.DictWriter(output_file,['date','count'])
		thewriter.writeheader()
		
		for row in data: 
			thewriter.writerow(row)
		
		print("Success! :]")

except IOError:
   		print "Could not open file! Please close Excel!"



#---Get visit duration for Mint BEACON---

url_2 = 'https://cloud.estimote.com/v2/analytics/devices/193fde558e5f12386ab392df7761900a/duration?from=1520812800&to=1523232000&granularity=hourly'
response_1 = requests.get(url_2,auth = ('hubbs-beacon-1g4','9dd89caad492d2a7d4b4c023d591cc17'))

#	print(response_3.text) #Prints data to terminal
# 	print("\n")

#	Converts the dictionary string output of response.text into an actual dictionary
allData = ast.literal_eval(response_1.text)
data = allData['data']
print("-------------------------------------------------------------")
print("EXPORTING CSV: Get Visit Duration for Mint Beacon: \n")
print("-------------------------------------------------------------")

try:
	keys = data[0].keys() #keys #['date','count']
	with open('MintProximityData.csv','wb') as output_file:
		thewriter = csv.DictWriter(output_file,['date','count'])
		thewriter.writeheader()
		
		for row in data: 
			thewriter.writerow(row)
		
		print("Success! :]")

except IOError:
   		print "Could not open file! Please close Excel!"

