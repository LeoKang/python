import requests

url = 'http://apis.data.go.kr/1360000/RoadWthrInfoService/getCctvStnRoadWthr'
params ={'serviceKey' : '', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'eqmtId' : '0500C00001', 'hhCode' : '00' }

response = requests.get(url, params=params)
print(response.content)
