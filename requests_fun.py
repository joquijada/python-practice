import requests

res = requests.post('https://9568a57sz5.execute-api.us-east-1.amazonaws.com/js/v1/token', data={'number': 4111111111111111,
                                                                 'month': '05',
                                                                 'year': 2023,
                                                                 'cvv': 123,
                                                                 'first_name': 'Test',
                                                                 'last_name': 'User',
                                                                 'address1': '123 Main St',
                                                                 'city': 'South Park',
                                                                 'state': 'CO',
                                                                 'postal_code': 12345,
                                                                 'country': 'US',
                                                                 'key': 'ewr1-jxTZCVWsb9A0ylzYNVSDoX'
                                                                 })

print(res.text)
