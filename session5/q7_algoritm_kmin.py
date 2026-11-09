import numpy as np
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pylab as plt

data = [
    [25,26],
    [37,8],
    [67,82],
    [44,23],
    [56,17]
]

data =np.random.randint(0,100, size=(30,2))
model =KMeans(n_clusters=3, random_state=42)
model.fit(data)

print(model.labels_)
print(model.cluster_centers_)

plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=model.labels_, cmap='viridis', s=80, label='Data Points')

plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            c='red', marker='X', s=250, edgecolors='black', linewidths=2, label='Centroids')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('KMeans Clustering')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
