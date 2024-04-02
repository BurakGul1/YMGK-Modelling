import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def bifurcation_diagram(r_values, x0, num_iterations, num_transient, num_points):
    bifurcation_points = []

    for r in r_values:
        x = x0
        for _ in range(num_transient):
            x = logistic_map(r, x)
        
        for _ in range(num_points):
            x = logistic_map(r, x)
            bifurcation_points.append([r, x])

    return np.array(bifurcation_points)

r_min = float(input("Minimum r değerini girin: "))
r_max = float(input("Maksimum r değerini girin: "))
num_r_values = int(input("Kullanılacak r değeri sayısını girin: "))

r_values = np.linspace(r_min, r_max, num_r_values)  # r değerlerinin aralığı
x0 = 0.5  # Başlangıç değeri
num_iterations = 1000  # Her r için iterasyon sayısı
num_transient = 100  # Transient sayısı
num_points = 200  # Bifurkasyon noktası sayısı

# Bifurkasyon diyagramını hesapla
bifurcation_data = bifurcation_diagram(r_values, x0, num_iterations, num_transient, num_points)

plt.figure(figsize=(10, 6))
plt.scatter(bifurcation_data[:, 0], bifurcation_data[:, 1], s=0.5, c='b', marker='.')
plt.xlabel('r')
plt.ylabel('x')
plt.title('Logistik Harita Bifurkasyon Diyagramı')
plt.show()
