from src.movie.api.call import gen_url, req, get_key, req2list, list2df, save2df, echo, apply_type2df
import pandas as pd


def test_echo():
	r = echo("hello")
	assert r =="hello"

def test_sk():
	key = get_key()
	assert key


def test_gen_url():
	url = gen_url()
	assert url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=e1ac8e397edce73a571ba078b2d4db58&targetDt=20240730"

	assert True
	assert "http" in url

def test_req():
	code, data = req()
	assert code == 200

	code, data = req("20230101")
	assert code == 200


def test_req2list():
	l = req2list()
	assert len(l) > 0
	v = l[0]
	assert 'rnum' in v.keys()
	assert v['rnum'] == '1'
	
def test_list2df():
	df = list2df()
	print(df)
	assert isinstance(df, pd.DataFrame)
	assert 'rnum' in df.columns
	assert 'openDt' in df.columns
	assert 'movieNm' in  df.columns
	assert 'audiAcc' in df.columns

def test_save2df():
	df = save2df()

	assert isinstance(df, pd.DataFrame)
	assert 'load_dt' in df.columns

def test_apply2df():
	df = apply_type2df()
	assert isinstance(df, pd.DataFrame)
	assert df['rnum'].dtype in ['int64']
	assert df['rank'].dtype in ['int64']


