
import requests
import json
import hashlib


def get_notification_data():
    r = requests.get(
        url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=446&date=01-06-2021')
    json_data = r.json()

    for jsonobj in json_data['sessions']:

        for key, value in jsonobj.items():
            if jsonobj['min_age_limit'] < 45 and jsonobj['available_capacity_dose1'] >= 0:
                print(jsonobj)
                print(key, value)
    return r


def get_sha_256_encode(otpstring):
    return hashlib.sha256(otpstring.encode()).hexdigest()


# print(get_sha_256_encode('621579'))
get_notification_data()
