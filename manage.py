from gaia import create_app

from flask.ext.script import (Manager, Shell, Server, prompt, prompt_pass,prompt_bool)

app = create_app()



manager = Manager(app)
manager.add_command("runserver", Server("localhost", port=5000))





if __name__ == "__main__":
    manager.run()
    