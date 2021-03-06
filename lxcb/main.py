#! /usr/bin/env python3

import os
import site


# add the directory which contains the lxcb module to the path. this will only
# ever execute when running the main.py script directly since the python
# package will use an entrypoint
if __name__ == '__main__':
    mod = os.path.dirname(os.path.realpath(__file__))
    site.addsitedir(os.path.dirname(mod))


def main():
    pass
