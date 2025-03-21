import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(data_x, data_y, alpha=0.7, color='blue', edgecolor='black')

# Настройка заголовков и меток
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('ось x')
plt.ylabel('ось у')

# Показ диаграммы рассеяния
plt.show()