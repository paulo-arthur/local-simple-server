import requests, json

URL = input('Ngrok code: ')
URL = 'http://' + URL + '.ngrok.io'
print(URL)

def contact(URL):
    OPTION = input('[R] - Read server | [W] - Send a message | [D] - Delete all messages: ').lower()

    if OPTION == 'r':
        req = json.loads(requests.get(f'{URL}').text)

        if len(req) == 0:
            print('O servidor está vazio.')

        for msg in req:
            print(msg)

    elif OPTION == 'w':
        msg = input('Type the message: ')
        msg = json.dumps(msg)
        req = requests.post(f'{URL}?msg={msg}')
        print('Message sent sucefully')

    elif OPTION == 'd':
        req = requests.post(f'{URL}/delete')

    else:
        print('Enter a valid option.')
        contact(URL)
while True:
    contact(URL)
