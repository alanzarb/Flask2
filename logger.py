import logging
import math
import time

# create and configure logger
LOG_FORMAT = "%(levelname)s \t | %(asctime)s - %(message)s "
logging.basicConfig(filename="logging\\log1.log", level=logging.DEBUG,
                    format=LOG_FORMAT)

logger = logging.getLogger()

# test the logger
logger.info("This is our first message")
#logger.debug("We're in file %s", __file__)
print(logger.level)


def quadratic_formula(a, b, c):
    """ Return the solutions to the euation ax^2 + bx + c = 0 """
    logger.info("quadratic_formula({0}, {1}, {2}) ".format(a, b, c))

    # compute discriminant
    logger.debug("# compute the discriminant")
    disc = b**2 - 4*a*c
    # compute the 2 roots
    logger.debug("# compute the 2 roots")
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc))/(2*a)

    logger.debug("# return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)

# t = time.localtime()
# print ("time.asctime(t): %s ", time.asctime(t))
# Sun Feb  9 21:59:45 2020
