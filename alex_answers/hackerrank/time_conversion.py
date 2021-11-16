
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.
    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    """

    hour = int(s[:2])
    am_pm = s[-2:]
    middle_digits = s[2:-2]
    is_12 = hour == 12
    is_am = am_pm == "AM"
    is_pm = not is_am

    if is_am and not is_12 or is_pm and is_12:
        return s[:-2]

    if is_am and is_12:
        return f"00{middle_digits}"

    hour = (hour+12)
    return f"{hour}{middle_digits}"





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()