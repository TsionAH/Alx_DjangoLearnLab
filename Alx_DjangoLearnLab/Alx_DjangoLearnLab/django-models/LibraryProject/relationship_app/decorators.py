

def is_admin(user):
    return user.role == 'Admin'
    
def is_librarian(user):
    return user.role == 'Librarian'

def is_member(user):
    return user.role == 'Member'