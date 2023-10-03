import requests

CLIENT_ID = '71fd59d0b4cb4f1dadbed88a02761217'
CLIENT_SECRET = '3e4dd1ac651040289f9d6048becef00b'

data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}

def generate_access_token():
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    return response