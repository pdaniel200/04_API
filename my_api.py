# pachetul flask creaza api
from flask import Flask

server_port = 5000  # porturile cu 5000 sunt specifice serverului de comunicare prin api :D
app = Flask(__name__)
app.config['DEBUGG'] = True

users = [
    {
        'email': 'florin@.com',
        'name': 'florin',
        'password': '1234'
    },
    {
        'email': 'paul@.com',
        'name': 'paul',
        'password': '12345'
    }
]


@app.route('/')
def get_user():
    return users[0]


@app.route('/allusers')
def get_users():
    return users


# @app.route('/allusers', methods=['POST'])
# def post_users():
#     return users


if __name__ == '__main__':
    app.run('localhost', port=server_port)
