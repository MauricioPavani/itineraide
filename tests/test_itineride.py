from itineride import itineride


def test_return_type_list_open_rides():
    result = itineride.list_open_rides()
    assert type(result) == type(list())
