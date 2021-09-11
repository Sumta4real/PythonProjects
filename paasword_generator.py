#def NumSplitByRatio(num):

def password_generator(passwordLength,special__char = False):
    """
    This function takes in one argument, the length of password to be generated
    and returns a generated alphanumeric password as a string

    INPUT - passwordLength(int) - length of password to be generated
            user_specific(bool) - if user want to be special character included
            in the password or not

    OUTPUT - password(str) - generated alphanumeric password

    """

    import string
    import random

    if user_specific == False:

        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ''.join(random.choice(chars) for i in range(passwordLength))

    else:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits+string.punctuation
        dummy_str = ''.join(random.choice(string.ascii_lowercase) for i in range(password-4))
        dummy_str += ''.join(random.choice(string.ascii_uppercase) for i in range(2))
        dummy_str += ''.join(random.choice(string.digits) for i in range(1))
        dummy_str += ''.join(random.choice(string.punctuation) for i in range(1))
        #convert str to list and shuffle to mix
        dummy_list = list(dummy_str)
        random.shuffle(dummy_list)
        password = ''.join(dummy_list)


    return 'Your password is ' + password

    #dummy_str = ''.join(random.choice(chars) for i in range(alpha_lower))
    #dummy_str += ''.join(random.choice(chars) for i in range(alpha_upper))
    #dummy_str += ''.join(random.choice(chars) for i in range(digits))
    #convert str to list and shuffle to mix
    #dummy_list = list(dummy_str)
    #random.shuffle(dummy_list)
    #f_password = ''.join(dummy_list)
    #return f_password
