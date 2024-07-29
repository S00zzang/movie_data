# movie

### install
```bash
# main
$ pip install git+https://github.com/S00zzang/movie_data.git

# branch
$ pip install git+https://github.com/S00zzang/movie_data.git@<BRANCH_NAME>
```

### start dev
```bash
$ git clone <URL>

$ cd <DIR>

$ # option
$ pdm venv create

$ source .venv/bin/activate 
$ pytest
```

### setting env
``` 
cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<key>"
```
