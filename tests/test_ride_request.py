import respx
from httpx import Response

from itineride import ride_request


def test_list_parks_in_ride_request():
    assert hasattr(ride_request, 'list_parks')


def test_list_parks_is_dict():
    list_parks = getattr(ride_request, 'list_parks')
    assert isinstance(list_parks, dict)


@respx.mock
def test_status_code_200_ride_request():
    mocked_responce = Response(
        200,
        json={
            'lands': [
                {
                    'rides': [
                        {
                            'name': "A Pirate's Adventure ~ Treasures of the Seven Seas",
                            'wait_time': 0,
                            'is_open': True,
                        }
                    ]
                }
            ]
        },
    )

    respx.get(ride_request.URL.format(6)).mock(mocked_responce)
    response = ride_request.list_rides()
    assert response == {
        "A Pirate's Adventure ~ Treasures of the Seven Seas": 0
    }
    # assert isinstance(ride_request.list_rides(), dict)


@respx.mock
def test_status_code_error_ride_request():
    mocked_responce = Response(408)  # Timeout status code

    respx.get(ride_request.URL.format(6)).mock(mocked_responce)
    response = ride_request.list_rides()
    assert response == {}


@respx.mock
def test_status_is_open_ride_request():
    mocked_responce = Response(
        200,
        json={
            'lands': [
                {
                    'rides': [
                        {
                            'name': "A Pirate's Adventure ~ Treasures of the Seven Seas",
                            'wait_time': 0,
                            'is_open': False,
                        }
                    ]
                }
            ]
        },
    )

    respx.get(ride_request.URL.format(6)).mock(mocked_responce)
    response = ride_request.list_rides()
    assert response == {}
