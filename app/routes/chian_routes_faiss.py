from flask import Blueprint, jsonify, request
from app.service.chian_service_faiss import analyze_chian

chian_bp = Blueprint('chian', __name__)

@chian_bp.route('/api/chian', methods=['POST'])
def analyze_chian_route():
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "차량에 대한 질문을 해주세요."}), 400

    try:
        answer = analyze_chian(query)
        return jsonify({"answer": answer}), 200
    except Exception as e:
        print(f"Error in analyze_chian_route: {str(e)}")  # 에러 로깅
        return jsonify({"error": f"응답 생성 중 오류가 발생했습니다: {str(e)}"}), 500
