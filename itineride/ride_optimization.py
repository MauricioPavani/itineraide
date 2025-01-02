def ratio_index_calc(rides: dict[str]) -> dict[str] | str:
    for ride in rides:
        try:
            rides[ride]['ratio_index'] = (
                rides[ride]['will_index'] / rides[ride]['wait_time']
            )
        except ZeroDivisionError:
            rides[ride]['ratio_index'] = 100
        except KeyError:
            return 'Bad format rides'
        except TypeError:
            return 'Bad format rides'
    return rides


def ride_allocation(rides, max_time):
    rides = ratio_index_calc(rides)
    if isinstance(rides, dict):
        sorted_rides = dict(
            sorted(
                rides.items(),
                key=lambda item: item[1]['ratio_index'],
                reverse=True,
            )
        )

        allocated_ride = []
        current_time = 0

        for ride in sorted_rides:
            if current_time + sorted_rides[ride]['wait_time'] <= max_time:
                allocated_ride.append(ride)
                current_time += sorted_rides[ride]['wait_time']

        return allocated_ride
    else:
        return rides
