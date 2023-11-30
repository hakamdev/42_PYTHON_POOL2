import time
from datetime import date

time_in_ms = time.time()
today = date.today().strftime("%b %d %Y")

print(
    "Seconds since January 1, 1970: "
    f"{time_in_ms:,.4f} or {time_in_ms:.2e} in scientific notation")
print(today)
