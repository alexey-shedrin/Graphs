def get_start_node():  # Получаем номер вершины, защита от ввода не int
    while True:
        try:
            print("Введите номер начальной вершины:")
            node = input()
            node = int(node)
            break

        except ValueError:
            print("Ошибка: вы ввели не число")

    return node


def get_finish_node():  # Получаем номер вершины, защита от ввода не int
    while True:
        try:
            print("Введите номер конечной вершины:")
            node = input()
            node = int(node)
            break

        except ValueError:
            print("Ошибка: вы ввели не число")

    return node


# Список смежности, нумерация в списке совпадает с номерами вершин
# Можно записать свой вариант графа, любой длины и сложности
graph = [None, [3, 5], [8], [2, 7], [1], [3], [5], [5, 6], [2, 4]]

start_node = get_start_node()
finish_node = get_finish_node()

# На сколько ребер мы отошли от стартовой вершины (глубина)
depth_level = 1
# Для обработки всех вершин на равном удалении от искомой вершины (ширина)
width_level = [None, 0, 0, 0, 0, 0, 0, 0, 0]

# Показывает текущий путь, если это ответ - записываем в all_ways
way = [start_node]
# Хранит все возможные верные пути от стартовой до финальной точек
all_ways = []

# Обход в глубину, если встречаем ранее встреченную вершину или искомую,
# то начинаем обход в ширину. Если на данном уровне глубины проверили
# все варианты, то возвращаемся назад, так пока не проверим все варианты.
while True:
    try:
        way.append(graph[(way[-1])][(width_level[depth_level])])
        if way[-1] == finish_node:
            copy_way = way.copy()
            all_ways.append(copy_way)
            way.pop()
            width_level[depth_level] += 1
        elif way[-1] in way[:-1]:
            way.pop()
            width_level[depth_level] += 1
        else:
            depth_level += 1
    except IndexError:
        if depth_level == 1:
            break
        else:
            way.pop()
            width_level[depth_level] = 0
            depth_level -= 1
            width_level[depth_level] += 1

# Вывод результатов
if len(all_ways) == 0:
    print(f"Нет путей из точки {start_node} в точку {finish_node}:")
else:
    min_ways = []
    max_ways = []
    min_len = len(all_ways[0])
    max_len = len(all_ways[0])
    index = 0
    print(f"Все возможные пути из точки {start_node} в точку {finish_node}:")
    while index < len(all_ways):
        print(all_ways[index])
        if len(all_ways[index]) < min_len:
            min_len = len(all_ways[index])
            min_ways.clear()
            min_ways.append(all_ways[index])
        elif len(all_ways[index]) == min_len:
            min_ways.append(all_ways[index])

        if len(all_ways[index]) > max_len:
            max_len = len(all_ways[index])
            max_ways.clear()
            max_ways.append(all_ways[index])
        elif len(all_ways[index]) == max_len:
            max_ways.append(all_ways[index])
        index += 1
    print(f"Наименьший путь: {min_ways}")
    print(f"Наибольший путь: {max_ways}")
