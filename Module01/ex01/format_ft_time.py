import time
from datetime import date

time_in_ms = time.time()
today = date.today().strftime("%b %d %Y")

# Only works in Python 3.6+
print(
    f"Seconds since January 1, 1970: {time_in_ms:,.4f} or {time_in_ms:.2e} in scientific notation")
# Alternative method
# print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(
#     time_in_ms, time_in_ms))
print(today)
