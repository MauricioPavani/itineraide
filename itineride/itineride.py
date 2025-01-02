from datetime import datetime

import ride_optimization
import ride_request
from InquirerPy import inquirer


def cli():
    parks = ride_request.list_parks.keys()
    selected_park = inquirer.select(
        message='Pick a park:', choices=parks
    ).execute()

    rides = ride_request.list_rides(ride_request.list_parks[selected_park])

    rated_rides = dict()
    print('Type directional key and rate the ride:')
    for ride in rides:
        rate = inquirer.number(
            message=ride + ':', min_allowed=1, max_allowed=10
        ).execute()

        rated_rides[ride] = {'wait_time': rides[ride], 'will_index': int(rate)}

    start_park = inquirer.text('Type start park (hh:mm): ').execute()
    end_park = inquirer.text('Type end park (hh:mm): ').execute()

    try:
        format_time = '%H:%M'
        start_park = datetime.strptime(start_park, format_time)
        end_park = datetime.strptime(end_park, format_time)

        diff = end_park - start_park
        park_time = diff.total_seconds() / 60
    except ():
        park_time = 300

    selected_rides = ride_optimization.ride_allocation(rated_rides, park_time)
    print('Selected rides:')
    for ride in selected_rides:
        print(ride)


if __name__ == '__main__':
    cli()
