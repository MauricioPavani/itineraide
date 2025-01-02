import httpx

list_parks = {
    'Disney Magic Kingdom': 6,
    'Disney Hollywood Studios': 7,
    'Epcot': 5,
    'Animal Kingdom': 8,
    'Universal Studios At Universal Orlando': 65,
    'Islands Of Adventure At Universal Orlando': 64,
}

URL = 'https://queue-times.com/parks/{}/queue_times.json'


def list_rides(park_id: int = 6) -> dict[str, int]:
    response = httpx.get(URL.format(park_id))

    rides = dict()

    if response.status_code == 200:
        for land in response.json()['lands']:
            for ride in land['rides']:
                rides[ride['name']] = ride['wait_time']

    return rides
