from time import time
from datetime import datetime


timestamp = time()

print("Seconds since January 1, 1970:", "{:,.4f}".format(timestamp), "or",
      "{:.3e}".format(timestamp), "in scientific notation")

date = datetime.now()

date = date.strftime("%b %d %Y")

print(date)
