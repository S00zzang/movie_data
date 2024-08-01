import requests
import os
import pandas as pd

def echo(yaho):
	return y/tmp/test_parquet/load_dt=20240725/multiMovieYn=Naho

def apply_type2df(load_dt = '20120101', path="~/tmp/test_parquet"):
	df = pd.read_parquet(f'{path}/load_dt={load_dt}')

	num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
	for col_names in num_cols:
		df[col_names] = pd.to_numeric(df[col_names])

	return df


def save2df(load_dt = '20120101', url_param={}):
	df = list2df(load_dt, url_param)

	df['load_dt'] = load_dt
	# df에 load_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식)

	for k,v in url_params.items():
		df[k] = v
		cols.append(k)

	df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])

	return df

def list2df(load_dt='20120101', url_param={}):
	l = req2list(load_dt, url_param)
	df = pd.DataFrame(l)

	return df

def req2list(load_dt='20120101', url_param={}) -> list:
	_, data = req(load_dt, url_param)
	l = data['boxOfficeResult']['dailyBoxOfficeList']
	
	return l

def gen_url(dt="20120101", url_param={}):
	base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
	key = get_key()
	
	url = f"{base_url}?key={key}&targetDt={dt}"
	
	for k, v in url_param.items():
		url = url + f"&{k}={v}"

	return url

def req(load_dt="20120101", url_param={}):
	url = gen_url(load_dt, url_param=url_param)
	r = requests.get(url)

	data = r.json()
	code = r.status_code
	print(code, data)
	return code, data

def get_key():
	key = os.getenv("MOVIE_API_KEY")
	return key
