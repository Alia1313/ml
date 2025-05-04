import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def read_data(filename):
    return pd.read_csv(filename, header=None)

def print_statistics(data):
    print("Статистика по данным:")
    print(f"Количество элементов: {len(data)}")
    print(f"Минимальное значение: {min(data)}")
    print(f"Максимальное значение: {max(data)}")
    print(f"Среднее значение: {sum(data)/len(data)}")
    print()

def least_squares(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(i**2 for i in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b
def plot_data(x, y, a, b):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.scatter(x, y, color='blue', label='Исходные точки')
    plt.title('Исходные данные')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.subplot(1, 3, 2)
    plt.scatter(x, y, color='blue', label='Исходные точки')
    plt.plot(x, [a * i + b for i in x], color='red', label='Регрессионная прямая')
    plt.title('Регрессионная прямая')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.subplot(1, 3, 3)
    plt.scatter(x, y, color='blue', label='Исходные точки')
    plt.plot(x, [a * i + b for i in x], color='red', label='Регрессионная прямая')
    for i in range(len(x)):
        error = y[i] - (a * x[i] + b)
        rect = patches.Rectangle((x[i] - 0.05, min(y[i], a * x[i] + b)), 0.1, abs(error), linewidth=1, edgecolor='gray', facecolor='gray', alpha=0.5)
        plt.gca().add_patch(rect)
    plt.title('Ошибки (квадраты отклонений)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    filename = 'student_scores.csv'
    data = read_data(filename)
    x = list(map(float, data[0].tolist()[1:]))
    y = list(map(float, data[1].tolist()[1:]))
    print_statistics(x)
    print_statistics(y)
    a, b = least_squares(x, y)
    plot_data(x, y, a, b)
