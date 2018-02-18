from user import *

admin = Admin('Ivan', 'Vasilev', 'password')

admin.privileges.show_privileges()
print('\nNow lets give the admin some privileges by calling the\
give privilege method')

admin.privileges.set_privileges()
admin.privileges.show_privileges()


