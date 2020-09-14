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

def sequence(find, numbers):
    """This function checks to see if an object is in a sequence

        >>> sequence(1, [1,2,3,4])
        1
        >>> sequence("i", "Hello world")
        'Nothing'
        >>> sequence(4, (2,4,6))
        4
    """
    for n in numbers:
        if find == n:
            return(n)
    else:
        return("Nothing")

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
    sequenced = sequence(6,[1,2,3,4,5,6])
    print(f'{sequenced} is in the sequence')

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
