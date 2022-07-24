import requests
import datetime


class Pixela:
    def __init__(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.TODAY = datetime.datetime.now()

    def create_pixela_user(self, username, token):
        user_params = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        # Creating a user
        response = requests.post(url=self.pixela_endpoint, json=user_params)
        response.raise_for_status()
        print(response.text)

    def create_pixela_graph(self, username, token, graph_id):
        graph_endpoint = f"{self.pixela_endpoint}/{username}/graphs"

        graph_config = {
            "id": graph_id,
            "name": "Swimming Graph",
            "unit": "meters",
            "type": "float",
            "color": "ajisai"
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        response.raise_for_status()
        print(response.text)

    def create_pixela_pixel(self, username, graph_id, token, qty):
        pixel_endpoint = f"{self.pixela_endpoint}/{username}/graphs/{graph_id}"

        headers = {
            "X-USER-TOKEN": token
        }

        pixel_params = {
            "date": self.TODAY.strftime("%Y%m%d"),
            "quantity": qty,
        }

        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
        print(response.text)

    def update_pixela_pixel(self, username, graph_id, token, date, qty):
        pixel_endpoint = f"{self.pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
        print(pixel_endpoint)
        headers = {
            "X-USER-TOKEN": token
        }

        pixel_params = {
            "quantity": qty
        }

        response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
        print(response.text)

    def delete_pixela_pixel(self, username, graph_id, token, date):
        pixel_endpoint = f"{self.pixela_endpoint}/{username}/graphs/{graph_id}/{date}"

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.delete(url=pixel_endpoint, headers=headers)
        print(response.text)
