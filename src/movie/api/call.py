import requests
import os
import pandas as pd

def list2df():
	l = req2list()
	df = pd.DataFrame(l)

	return df

def req2list():
	_, data = req()
	# data.get('').get('')
	l = data['boxOfficeResult']['dailyBoxOfficeList']
	l = [
		{'rnum' : '1', 'rank' : '1'},
		{'rnum' : '2', 'rank' : '2'},
		{'rnum' : '3', 'rank' : '3'},
	]
	
	return l

def gen_url(dt="20120101"):
	base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
	key = get_key()

	url = f"{base_url}?key={key}&targetDt={dt}"
	
	return url

def req(dt="20120101"):
	url = gen_url(dt)
	r = requests.get(url)

	data = r.json()
	code = r.status_code
	print(code, data)
	return code, data

def get_key():
	key = os.getenv("MOVIE_API_KEY")
	return key
