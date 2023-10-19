# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

import gits_logging


def gits_hello_world(args):
    """
    Function that prints hello message
    to user console
    """
    print("Hello from GITS Commandline Tools")
    gits_logging.gits_logger.info("Hello from GITS Commandline Tools")
