#
# generic utility function
#

import random
import string

DEBUG = True
# DEBUG = False


def get_random_str(length):
    """
    function to generate random string of given length
    """
    str_range = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.sample(str_range, length))


def dlog(msg):
    if not DEBUG:
       return
    print(")==> DLOG :: %s " % msg)

################################
#                              #
#       SOME QUICK TESTS       #
#                              #
################################
if __name__ == "__main__":
    print (get_random_str(6))
    print (get_random_str(10))
    print (get_random_str(12))
