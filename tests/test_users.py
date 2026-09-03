# using the requests package that was downloaded
import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"


def test_get_users():
    # communicating with the api
    response = requests.get(base_url + "/users")

    users = response.json()

    # test if we get a 200 response
    assert response.status_code == 200

    # verifying users is a list
    assert isinstance(users, list)

    # verifying the api returned at least one user
    assert len(users) > 0

    # going through each user returned by the api
    for user in users:
        # print(user)

        # verifying each user has the following
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user


@pytest.mark.parametrize("user_id, expected_name, expected_username, expected_email", [
    (1, "Leanne Graham", "Bret", "Sincere@april.biz"),
    (2, "Ervin Howell", "Antonette", "Shanna@melissa.tv"),
    (3, "Clementine Bauch", "Samantha", "Nathan@yesenia.net")
])

def test_get_specific_user(user_id, expected_name, expected_username, expected_email):
    url = base_url + "/users/" + str(user_id)
    response = requests.get(url)

    user = response.json()

    assert response.status_code == 200
    assert user["id"] == user_id
    assert user["name"] == expected_name

    # this one should fail
    # assert user["name"] == "Kaylee Miller"

    assert user["username"] == expected_username
    assert user["email"] == expected_email


def test_get_nonexistent_user():
    url = base_url + "/users/999"
    response = requests.get(url)

    # will print an empty dictionary {}
    # print(response.json())

    # test if we get a 404 response because user 999 does not exist
    assert response.status_code == 404
    assert response.json() == {}