import jwt


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')

def verify_signature(token):
    try:
        data = jwt.decode(token, 'acelera', algorithms='HS256')
    ######## FALTA ISSO AQUI ##########
    except jwt.exceptions.InvalidSignatureError:
        return {'error': 2}
    else:
        return data



'''
# Aprendendo a usar a biblioteca jwt 

def main():
    # Codificando os dados e gerando um token
    data = {
        'language': 'Python'
        }

    secret = 'acelera'

    token = jwt.encode(data, secret, algorithm='HS256')
    # exemplo de token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEyMywiZXhwIjoxNTE4NzQ5OTg1fQ.-uUCFwVFhpg57Jig9VwWh86f85Uip4lPvF4iL6nxjbA
    print(token)
    print()

    # Decodificando os dados pelo token
    data = jwt.decode(token, 'acelera', algorithms='HS256')

    print(data)

    print(verify_signature(token))
    print(verify_signature('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEyMywiZXhwIjoxNTE4NzQ5OTg1fQ.-uUCFwVFhpg57Jig9VwWh86f85Uip4lPvF4iL6nxjbA'))
    return 0

if __name__ == "__main__":
    main()
'''
