from flask_script import Command, Option


class Create(Command):

    option_list = (
        Option('--name', '-n', dest='name'),
    )

    def run(self, name):
        print("Hello World {}".format(name))
