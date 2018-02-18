from user import *

admin = Admin('Ivan', 'Vasilev', 'password')
admin.privileges.show_privileges()
print('\nNow lets give him some privileges by calling set_privileges\n')
admin.privileges.set_privileges()
admin.privileges.show_privileges()


