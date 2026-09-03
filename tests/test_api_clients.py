from utils.api_client import APIClient


# the api we are using for our tests
base_url = "https://jsonplaceholder.typicode.com"


def test_api_client_get():
    # create an api client using our base url
    client = APIClient(base_url)

    # use our api client's get method
    response = client.get("/users/1")

    # verify that the request was successful
    assert response.status_code == 200

    # convert the response into a python dictionary
    user = response.json()

    # verify that we received the expected user
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"