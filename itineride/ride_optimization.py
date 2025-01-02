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
