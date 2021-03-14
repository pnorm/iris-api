# Iris API

### 1. Clone repository
```
$ git clone https://github.com/pnorm/iris-api.git
```

### 2. Create and activate virtual environment
```
~/iris-api$ python3 -m venv env
~/iris-api$ source env/bin/activate
```
### 3. Install requirements
```
(env):~/iris-api$ pip install -r requirements.txt
```

### 4. Start web-server on localhost
```
(env):~/iris-api$ uvicorn app/main:app --reload
```

### 5. Go to the 127.0.0.1:8000/docs address in your browser
