

import cProfile
import pstats
import sys
import time
from financial import get_financial_data

pr = cProfile.Profile()
pr.enable()
get_financial_data("MSFT", "Total Revenue")
pr.disable()


with open('pstats-cumulative.txt', 'w') as f:
    ps = pstats.Stats(pr, stream=f)
    ps.strip_dirs().sort_stats('cumulative').print_stats(5)

