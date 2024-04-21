import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from typing import List


def collect_data() -> List[List[float]]:
    # Создание пустого массива для хранения данных из файлов
    result_data = []

    folder_path = './data'

    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file_path in txt_files:
        with open(file_path, 'r') as file:
            data = file.readlines()
            data_array = np.array([np.array([float(num) for num in line.split()]) for line in data])
            result_data.append(data_array)

    return result_data


def build_2d(all_data: List[List[float]]):
    dataset = {f'Мюоны_{i + 1}': data for i, data in enumerate(all_data)}

    # Инициализация графика
    plt.figure(figsize=(12, 8))

    # Построение графиков для каждого набора данных
    for data_label, data_array in dataset.items():
        plt.plot(data_array, label=data_label)

    # Добавление подписей осей и легенды
    plt.xlabel('Индекс точки данных')
    plt.ylabel('Значение мюонов')
    plt.title('Визуализация наборов данных мюонов')
    plt.legend()

    # Отображение графика
    plt.grid(True)
    plt.show()


def build_3d(all_data: List[List[float]]):
    # Инициализация трехмерного графика для визуализации
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Построение трехмерной модели для данных из файлов
    for i, data in enumerate(all_data):
        x = data[:, 0]
        y = data[:, 1]
        z = data[:, 2]

        ax.scatter(x, y, z, label=f'Мюоны {i + 1}', marker='o')

    # Добавление подписей к осям
    ax.set_xlabel('Энергия мюонов')
    ax.set_ylabel('Угол наклона траектории мюонов')
    ax.set_zlabel('Глубина проникновения мюонов в вещество')

    # Отображение трехмерной модели
    plt.title('3D Модель Мюонов')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    collected_data = collect_data()

    build_2d(collected_data)
    build_3d(collected_data)

