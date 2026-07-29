import statistics as stats
import math as m
height = [145,151, 152,
149, 147, 152, 151,149, 152, 151, 147, 148, 155, 147,152,151, 149,145, 147, 152,146,
148, 150, 152, 151]

variance = stats.variance(height)
print(variance)

stddev  = m.sqrt(variance)
print(stddev)