from flask_script import Manager
from flask import Flask
from commands.create import Create

app = Flask(__name__)

manager = Manager(app)


manager.add_command('hello', Create())


if __name__ == "__main__":
    manager.run()
