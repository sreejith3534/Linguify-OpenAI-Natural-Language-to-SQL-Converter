from flask import Flask, request, jsonify
from make_query_on_table_data import console_ops

app = Flask(__name__)


@app.route('/get_results_from_table', methods=['POST'])
def prediction():
    content = request.json
    file_path = content["file_path"]
    query = content["query"]
    print("file path is", type(file_path), type(query))
    result = console_ops(file_path, query)
    print("result is")
    return jsonify(result.to_json(orient='records'))


if __name__ == "__main__":
    app.run()
