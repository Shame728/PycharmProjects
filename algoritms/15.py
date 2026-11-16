import string

alf = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_'

def IsIdent(s):
    if (s == '') or ('_' not in s):
        return False
    for i in s:
        if i not in alf:
            return False
    return True
print(IsIdent('asdfsdfs_'))