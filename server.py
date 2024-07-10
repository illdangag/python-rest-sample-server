from flask import Flask, jsonify, request

app = Flask(__name__)

data_list = [
  {
    "id": 1,
    "name": "A",
    "description": "A data"
  },
  {
    "id": 2,
    "name": "B",
    "description": "B data"
  },
  {
    "id": 3,
    "name": "C",
    "description": "C data"
  },
  {
    "id": 4,
    "name": "D",
    "description": "D data"
  },
]

# 목록 조회
@app.route("/v1.0/data", methods=["GET"])
def get_data_list():
  return jsonify(data_list)

# 요소 조회
@app.route("/v1.0/data/<int:id>", methods=["GET"])
def get_data(id):
  for data in data_list:
    if data["id"] == id:
      return jsonify(data)
  
  # 요소를 찾지 못한 경우
  return jsonify({
    "code": 1,
  }), 404

# 요소 생성
@app.route("/v1.0/data", methods=["POST"])
def create_data():
  data = request.get_json()
  data_list.append(data)
  return jsonify(data), 201 

# 요소 삭제
@app.route("/v1.0/data/<int:id>", methods=["DELETE"])
def delete_data(id):
  for i in range(len(data_list)):
    if data_list[i]["id"] == id:
      del data_list[i]
      return jsonify({
        "code": -1
      }), 200
    
  # 요소를 찾지 못한 경우
  return jsonify({
    "code": 1
  }, 404)

# 서버 실행
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
