# python rest sample server

## 서버 실행

### 환경

- python3

### 페키지 설치

```shell
pip install flask
```

### 서버 실행

```shell
python3 ./server.py
```

## API 목록

### 데이터 목록 조회

```shell
curl --location 'localhost:8000/v1.0/data'
```

### 데이터 조회

```shell
curl --location 'localhost:8000/v1.0/data/1'
```

### 데이터 생성

```shell
curl --location 'localhost:8000/v1.0/data' \
--header 'Content-Type: application/json' \
--data '  {
    "id": 5,
    "name": "F",
    "description": "F data"
  }'
```

### 데이터 삭제

```shell
curl --location --request DELETE 'localhost:8000/v1.0/data/1'
```