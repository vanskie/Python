class User():
    """User creation"""

    def __init__(self, f_name, l_name, password):
        self.f_name = f_name
        self.l_name = l_name
        self.username = l_name.lower() + f_name.lower() 
        self.password = password
        self.login_attempts = 0


    def describe_user(self):
        """Describes the user vaguely"""

        user_info = {
            'first name': self.f_name,
            'last_name': self.l_name,
            'user_name': self.username,
            'password': '*' * len(self.password),
            }   
        
        print(user_info)


    def greet_user(self):
        """
        Prints a personalized greeting message to the user.
        """

        print('Hello there {}!'.format(self.username))


    def increment_login_attempts(self):
        """Increments self.login_attempts by 1"""

        self.login_attempts += 1


    def reset_login_attempts(self):
        """Resets the login attempts to 0"""

        self.login_attempts = 0


class Privileges():
    """Creates a number of privileges"""

    def __init__(self):
        
        self.privileges = [] 


    def set_privileges(self):
        """Gives a number of privileges"""

        self.privileges.append('bans')
        self.privileges.append('unbans')
        self.privileges.append('administrates')


    def show_privileges(self):
       """Shows the given privileges if any"""
       
       print('The user has the current privileges: ')
       
       for privilege in self.privileges:
           print('\t- ' + privilege)


class Admin(User):
    """A special kind of User ... and Admin User ... yea """

    def __init__(self, f_name, l_name, password):
        super().__init__(f_name, l_name, password)
        self.privileges = Privileges()

