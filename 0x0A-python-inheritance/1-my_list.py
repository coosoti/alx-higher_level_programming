#!/ust/bin/python3
"""My List class Documentation"""


class MyList(list):
    """MyList class inherits from the python class list"""

    def print_sorted(self):
        """this function sorts the current instance of the class MyList"""

        print(sorted(self))
