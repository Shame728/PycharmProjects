import re
#a)
def validate_emails(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_regex, email):
        return True
    return False

print(validate_emails('test@example.com'))
print(validate_emails('invalid-email@'))
print(validate_emails(''))
#b)
def find_all_time(file_path):
    time_pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'
    with open(file_path, 'r') as f:
        text = f.read()
        times = re.findall(time_pattern, text)
        return times

print(find_all_time('time.txt'))

