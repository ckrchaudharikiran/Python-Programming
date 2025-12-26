from datetime import datetime
import parser

date = "oct 14 2025 6:45PM"
date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")

print(date_time)
print(type(date_time))



# #using parser

# from dateutil import parser

# date = "oct 14 2025 6:45PM"
# date_time = parser.parse(date)

# print(type(date_time))
# print(date_time)
