import numpy as np
import matplotlib.pyplot as plt
import os
import glob


def collect_data():
    # Создание пустого массива для хранения данных из файлов
    all_data = []

    folder_path = './data'

    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file_path in txt_files:
        with open(file_path, 'r') as file:
            data = file.readlines()
            data_array = np.array([np.array([float(num) for num in line.split()]) for line in data])
            all_data.append(data_array)

    return all_data


if __name__ == '__main__':
    all_data = collect_data()
    # Подготовка данных для визуализации
    dataset = {f'Данные_{i + 1}': data for i, data in enumerate(all_data)}

    # Инициализация графика
    plt.figure(figsize=(12, 8))

    # Построение графиков для каждого набора данных
    for data_label, data_array in dataset.items():
        plt.plot(data_array, label=data_label)

    # Добавление подписей осей и легенды
    plt.xlabel('Индекс точки данных')
    plt.ylabel('Значение данных')
    plt.title('Визуализация нескольких наборов данных')
    plt.legend()

    # Отображение графика
    plt.grid(True)
    plt.show()
