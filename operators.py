#!/usr/bin/env python3
#
# operators.py
#
# This is a file to demonstrate open source software collaboration for the
# 2020 CPTR 226 class. This is the second way of using git and GitHub.
#
# Author: Seth McNeill
# Date: 2020 September 11
# Version: 0.1
# Course: CPTR 226
"""This is a file to demonstrate open source software collaboration for the
   2020 CPTR 226 class.
"""

# Includes
import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest   # used for testing the code from docstring examples


# Global Variables


# Functions
def not_equal(num1, num2):
    """This function determines if two numbers are equal

        >>> not_equal(2,3)
        True
        >>> not_equal(4, 4)
        False
        >>> not_equal(-3, -5)
        True

    """
    return(num1 != num2)



# This runs if the file is run as a script vs included as a module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--doctest', action='store_true',
                        help='Pass this flag to run doctest on the script')

    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    if(args.doctest):
        doctest.testmod(verbose=True)  # run the tests in verbose mode

    print("-------------------")
    added = not_equal(4, 5)
    print(f'4 != 5 = {added}')

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
