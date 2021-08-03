def password_generator(passwordLength):
    """
    This function takes in one argument, the length of password to be generated
    and returns a generated alphanumeric password as a string

    INPUT - passwordLength(int) - length of password to be generated

    OUTPUT - password(str) - generated alphanumeric password

    """

    import string
    import random

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits 
    password = ''.join(random.choice(chars) for i in range(passwordLength))

    return 'Your password is ' + password
