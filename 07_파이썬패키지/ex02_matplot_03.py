import matplotlib as mpl
import matplotlib.pyplot as plt

# 마커 옵션
# https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

x_values = [1, 2, 3, 4]
y_values = [2, 5, 6, 10]
# marker 표시(동그라미)
# plt.plot(x_values, y_values, "o")
# marker 표시(동그라미, 선)
# plt.plot(x_values, y_values, "o-")
# marker 표시(네모, 선)
# plt.plot(x_values, y_values, "s-")
# marker 표시(동그라미, 대시선)
plt.plot(x_values, y_values, "o--")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()