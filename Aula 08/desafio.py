# Crie um programa que receba uma data de entrada e converta para timestamp

import calendar

yr = int(input("Year: "))
mth = int(input("Month: "))
day = int(input("Day: "))

data = (yr, mth, day, 0, 0, 0)

print(calendar.timegm(data))

