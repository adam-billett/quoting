import bcrypt


class UserAuthentication:

    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.salt = bcrypt.gensalt(rounds=14)

    def login(self, username, password):
        if not username or not password:
            return False
        else:
            stored_password = self.db_manager.get_password(username)

            if stored_password:
                try:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        self.current_user = username
                        return True
                    else:
                        return False
                except ValueError as e:
                    print(f'Error: {e}')
                    return False
            else:
                return False

    def create(self, username, password, confirm):
        if not username or not password or not confirm:
            return False
        elif password != confirm:
            return False
        else:
            hashed_pass = bcrypt.hashpw(password.encode('utf-8'), self.salt)
            success = self.db_manager.create(username, hashed_pass, self.salt)
            return success
