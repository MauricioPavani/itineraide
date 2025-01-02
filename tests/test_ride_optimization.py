from itineride import ride_optimization


def test_ratio_index_calc_OK_input():
    rides = {
        'ride_1': {'wait_time': 50, 'will_index': 10},
        'ride_2': {'wait_time': 30, 'will_index': 5},
        'ride_1': {'wait_time': 20, 'will_index': 1},
    }

    result = ride_optimization.ratio_index_calc(rides)

    assert (
        isinstance(result, dict) and 'ratio_index' in result['ride_1'].keys()
    )


def test_ratio_index_calc_wait_time_0_input():
    rides = {'ride_1': {'wait_time': 0, 'will_index': 10}}
    result = ride_optimization.ratio_index_calc(rides)

    assert (
        isinstance(result, dict) and 'ratio_index' in result['ride_1'].keys()
    )


def test_ratio_index_calc_key_errors():
    rides = {'ride_1': {'wait_time': 0, 'will': 10}}
    result = ride_optimization.ratio_index_calc(rides)
    assert result == 'Bad format rides'


def test_ratio_index_calc_bad_format():
    rides = ['ride_1', 'ride_2']
    result = ride_optimization.ratio_index_calc(rides)
    assert result == 'Bad format rides'
