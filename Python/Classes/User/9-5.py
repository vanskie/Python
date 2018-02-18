from user import *

user_0 = User('Ivan', 'Vasilev', 'kopenga')
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()

print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)

