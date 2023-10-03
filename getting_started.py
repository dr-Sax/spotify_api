from core.access_token import generate_access_token

token = generate_access_token()
print(token.json())