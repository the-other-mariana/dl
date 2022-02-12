import numpy as np
import matplotlib.pyplot as plt

x = np.array([ 1, 2, 3, 4, 5, 5.5, 6])
y = np.array([7.7, 8.7, 10.6, 11.5,12,14, 15.5])

x=np.array( [44,46.4,43.6,35,35,32.6,28.9,27.7,25.5,20.375,12.5,37,37.5,36.5,36.2,33,43,46,29,31.7,31,28.75,32.4,31,29.5,22.5,20.6,35,33.1,31.5,28.8,21.3,37.80,37,37.1])
y=np.array( [26.944,25.833,25.556,23.056,21.389,20,18.889,18.33,16.389,13.889,12.778,24.583,23.33,23.33,22.5,18.889,25.278,25.278,25.833,20.278,20.278,20,18.889,15,21.11,20.556,19.44,16.25,14.722,22.222,21.667,20.556,19.167,15.556,23.889 ])  # Temperature °C data

 # number of observations/points
n = np.size(x)

	# mean of x and y vector
m_x, m_y = np.mean(x), np.mean(y)

	# calculating cross-deviation and deviation about x
SS_xy = np.sum(y*x) - n*m_y*m_x
SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
m = SS_xy / SS_xx
b = m_y - m*m_x

print("Pendiente calculada",m)
print("bias calculado",b)
  #print("Estimated coefficients:\nb_0 = {} \ \nb_1 = {}".format(b[0], b[1]))

# plotting the actual points as scatter plot
plt.scatter(x, y, color = "m",
marker = "o", s = 30)

	# predicted response vector
y_pred = b + m*x

	# plotting the regression line
plt.plot(x, y_pred, color = "g")

	# putting labels
plt.xlabel('x')
plt.ylabel('y')

	# function to show plot
plt.show()
