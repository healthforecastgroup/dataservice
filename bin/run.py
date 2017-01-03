from eve import Eve
from eve.auth import BasicAuth
import bcrypt
from flask import current_app as app
from werkzeug.security import check_password_hash
import random
import string
    
class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # allow anyone to create a new account.
        print('checkauth')
        if resource == 'app_users' and method == 'POST':
            print('bypass auth')
            return True
        if resource == 'lib_drugs' and method == 'GET':
            print('bypass auth')
            return True
        print('checkauth False')
        accounts = app.data.driver.db['app_users']
        account = accounts.find_one({'username': username})
        if account and 'username' in account:
            self.set_request_auth_value(account['username'])
        print('hola')
        print(account)
        return account and bcrypt.hashpw(password.encode('utf-8'),account['salt'].encode('utf-8')) == account['password']


def create_user(documents):
    print('hello')
    for document in documents:
        document['salt'] = bcrypt.gensalt().encode('utf-8')
        password = document['password'].encode('utf-8')
        document['password'] = bcrypt.hashpw(password, document['salt'])
        # Don't use this in production:
        # You should at least make sure that the token is unique.
        """For the purpose of this example the implementation is as simple as
            possible. A 'real' token should probably contain a hash of the
            username/password combo, which sould then validated against the account
            data stored on the DB.
        """
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                  for x in range(10)))


if __name__ == '__main__':

    app = Eve(auth=RolesAuth)

    @app.route('/hola')
    def hola():
        return 'hello world'

    app.on_insert_app_users += create_user
    app.run()