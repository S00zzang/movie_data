from src.movie.api.call import gen_url, req, get_key, req2dataframe

def test_sk():
	key = get_key()
	assert key


def test_gen_url():
	url = gen_url()
	assert url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=e1ac8e397edce73a571ba078b2d4db58&targetDt=20120101"

	assert True
	assert "http" in url

def test_req():
	code, data = req()
	assert code == 200

	code, data = req("20230101")
	assert code == 200


def test_req2df():
	l = req2dataframe()
	assert len(l) > 0
	v = l[0]
	assert 'rnum' in v.keys()
	assert v['rnum'] == '1'
	
