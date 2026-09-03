import requests


class APIClient:
    """
    Reusable client for communicating with the REST API.

    The goal of this class is to keep API communication separate
    from our actual test cases.
    """

    def __init__(self, base_url):
        # Store the base URL so we don't have to repeat it in every request
        self.base_url = base_url

    def get(self, endpoint):
        """
        Send a GET request to the specified API endpoint.

        Example:
            client.get("/users/1")

        This will send a request to:
            https://jsonplaceholder.typicode.com/users/1
        """

        # Combine the base URL and endpoint to create the full URL
        url = self.base_url + endpoint

        # Send the GET request and store the response
        response = requests.get(url)

        # Return the response so the test can validate it
        return response

    def post(self, endpoint, data=None):
        """
        Send a POST request to the specified API endpoint.

        'data' contains the information we want to send to the API.
        """

        # Combine the base URL and endpoint
        url = self.base_url + endpoint

        # Send the POST request with the provided data
        response = requests.post(url, json=data)

        # Return the response so the test can validate it
        return response

    def put(self, endpoint, data=None):
        """
        Send a PUT request to update an existing resource.
        """

        # Combine the base URL and endpoint
        url = self.base_url + endpoint

        # Send the PUT request with the updated data
        response = requests.put(url, json=data)

        # Return the response to the test
        return response

    def delete(self, endpoint):
        """
        Send a DELETE request to remove a resource.
        """

        # Combine the base URL and endpoint
        url = self.base_url + endpoint

        # Send the DELETE request
        response = requests.delete(url)

        # Return the response to the test
        return response