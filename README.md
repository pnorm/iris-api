# Iris API

### 1. Clone repository
```sh
$ git clone https://github.com/pnorm/iris-api.git
```

### 2. Create and activate virtual environment
```sh
~/iris-api$ python3 -m venv env
~/iris-api$ source env/bin/activate
```
### 3. Install requirements
```sh
(env):~/iris-api$ pip install -r requirements.txt
```

### 4. Start web-server on localhost
```sh
(env):~/iris-api& cd app
(env):~/iris-api/app$ uvicorn main:app --reload
```

### 5. Go to the 127.0.0.1:8000/docs address in your browser
