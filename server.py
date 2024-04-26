'''
    Contains the server to run our application.
'''
from flask_failsafe import failsafe

from Code.app import server
server = server

@failsafe
def create_app():
    '''
        Gets the underlying Flask server from our Dash app.

        Returns:
            The server to be run
    '''
    # l'importation est intentionnellement à l'intérieur pour fonctionner avec le serveur failsafe
    from Code.app import app  # pylint: disable=import-outside-toplevel
    return app.server

if __name__ == "__main__":
    
    create_app().run(port="8050", debug=True)