import random
import matplotlib.pyplot as plt

# 200 veri noktası için rastgele ivme değerleri oluşturma
num_points = 200
time = range(num_points)
acceleration_data = [random.uniform(-10, 10) for _ in range(num_points)]

# Oluşturulan ivme verilerini görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(time, acceleration_data, marker='o', linestyle='-', color='b')
plt.title('Rastgele Oluşturulan İvme Verileri')
plt.xlabel('Zaman')
plt.ylabel('İvme')
plt.grid(True)
plt.show()
