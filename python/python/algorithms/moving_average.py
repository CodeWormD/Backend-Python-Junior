# метод скользящего среднего
# создаётся новый массив данных, и в нём значение каждой точки высчитывается
# как среднее арифметическое предыдущих K значений из исходного набора

def moving_average(timeseries, K):
    result = []  # Пустой список.
    for begin_index in range(0, len(timeseries) - K + 1):
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / K
        result.append(current_avg)
    return result

moving_average([4,3,8,1,5,6,3], 3)