import requests, json

def contact():
    OPTION = input('[R] - Read server | [W] - Send a message | [D] - Delete all messages: ').lower()

    if OPTION == 'r':
        req = json.loads(requests.get(f'http://127.0.0.1:5000').text)

        if len(req) == 0:
            print('O servidor está vazio.')

        for msg in req:
            print(msg)

    elif OPTION == 'w':
        msg = input('Type the message: ')
        msg = json.dumps(msg)
        req = requests.post(f'http://127.0.0.1:5000/?msg={msg}')
        print('Message sent sucefully')

    elif OPTION == 'd':
        req = requests.post(f'http://127.0.0.1:5000/delete')
        
    else:
        print('Enter a valid option.')
        contact()
while True:
    contact()
