# external packages
import requests


def upload_data(url, id, data, token):
    requests.post(f"{url}/api/updateGCdata/{id}", json={"token": token, "data": data.jsonify()})
