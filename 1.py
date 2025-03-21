import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Настройка заголовков и меток
plt.title('Гистограмма для случайных данных')
plt.xlabel('Ось Х')
plt.ylabel('Ось У')

# Показ гистограммы
plt.show()