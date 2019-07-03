### Flask Tutorial

- http://flask.pocoo.org/docs/1.0/tutorial/ 의 튜토리얼을 진행
- Window 10
- python 3.7.3

#### Python Version

- Python 2.7 or python 3.4 이상

#### Create an Environment

```bash
pip install virtualenv
cd flask-tutorial
virtualenv venv
venv\Script\activate
```

#### Install Flask

```bash
pip install Flask
```

#### Start

```bash
# 설정(window cmd)
# flask-tutorial\
set FLASK_APP=flaskr
set FLASK_ENV=development

# Database 초기화
flask init-db

# 실행
flask run
```

- 브라우저에서 http://127.0.0.1:5000/auth/register 접속