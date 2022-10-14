from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlim3d(0, 12)
ax.set_ylim3d(0, 5)
ax.set_zlim3d(0, 12)

# Creo il nodo "free"
x = np.linspace(0, 12, 100)
y = np.ones(100) * 5
z = np.linspace(0, 12, 100)
X, Z = np.meshgrid(x, z)
ax.plot_surface(X, y, Z, alpha=0.6)


# creo le aree del nodo "busy"
# 1) da dove non partono frecce (in basso a sinistra)
x = np.linspace(0, 2, 100)
y = np.zeros(100)
z = np.linspace(0, 10, 100)
X, Z = np.meshgrid(x, z)
ax.plot_surface(X, y, Z, alpha=0.2)

# 2) da dove parte la freccia hit (in basso a destra)
x = np.linspace(2, 12, 100)
y = np.zeros(100)
z = np.linspace(0, 12, 100)
X, Z = np.meshgrid(x, z)
ax.plot_surface(X, y, Z, alpha=0.2)

# 3) da dove parte la freccia done (in alto)
x = np.linspace(0, 12, 100)
y = np.zeros(100)
z = np.linspace(10, 12, 100)
X, Z = np.meshgrid(x, z)
ax.plot_surface(X, y, Z, alpha=0.2)



plt.show()