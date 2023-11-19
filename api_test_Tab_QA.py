import requests
import json
import pandas as pd
from speech_to_text_module import get_text_from_speech


def get_response(url, json_payload):
    response = requests.post(url, json=json_payload)
    if response.status_code == 200:
        result = json.loads(response.json())
        result_df = pd.DataFrame(result)
        return result_df


def mode_of_query(way_to_query, query=None):
    if way_to_query == "speech":
        text = get_text_from_speech()
    else:
        text = query
    return text


if __name__ == "__main__":
    query_text = mode_of_query("speech")
    payload = {
        "file_path": "test.csv",
        "query": query_text
    }
    url_link = ' http://localhost:5000/get_results_from_table'
    res = get_response(url_link, payload)
    print(res)
