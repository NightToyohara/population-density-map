import numpy as np

"""
этот небольшой скрипт обрабатывает файл и возвращает два списка различного разрешения для отображения на карте

input: NaN
output: два списка с ключами формата:
{'lat', 'lon', 'pop', 'year', 'color'} и {'lat', 'lon', 'pop', 'year'}
"""

def load_f():
    """
    принимает разрешение данных для визуализации, возвращает список для отображения на карте
    :param:
    :return: data_density[{'lat', 'lon', 'pop', 'year', 'color'}], data_density_no_time[{'lat', 'lon', 'pop', 'year'}]
    """
    # загружаем датасеты, пропуская первые 6 строк
    density_array_2000 = np.loadtxt('data/gpw_v4_population_density_rev11_2000_1_deg.asc', skiprows=6)
    density_array_2005 = np.loadtxt('data/gpw_v4_population_density_rev11_2005_1_deg.asc', skiprows=6)
    density_array_2010 = np.loadtxt('data/gpw_v4_population_density_rev11_2010_1_deg.asc', skiprows=6)
    density_array_2015 = np.loadtxt('data/gpw_v4_population_density_rev11_2015_1_deg.asc', skiprows=6)
    density_array_2020 = np.loadtxt('data/gpw_v4_population_density_rev11_2020_1_deg.asc', skiprows=6)

    # датасет с разрешением 30 метров
    density_array_2020_min = np.loadtxt('data/gpw_v4_population_density_rev11_2020_30_min.asc', skiprows=6)

    # перебираем массивы
    # пересобираем каждую ячейку массива в словарь, а словари добавляем в список
    pop = 0
    color = 0
    data_density = []
    data_density_no_time = []

    lat_int = 90
    lon_int = -180

    for lat in density_array_2000:
        # перебираем каждую ячейку с севера на юг
        lat_int -= 1
        lon_int = -180
        for lon in lat:
            # перебираем каждую ячейку с запада нак восток
            lon_int += 1
            # отсеиваем пустые пустые значения
            if lon > 0:
                match lon:
                    case lon if lon < 5:
                        color = 1
                    case lon if lon < 20:
                        color = 2
                    case lon if lon < 70:
                        color = 3
                    case lon if lon < 150:
                        color = 4
                    case lon if lon < 200:
                        color = 5
                    case lon if lon < 300:
                        color = 6
                    case lon if lon < 500:
                        color = 7
                    case lon if lon < 700:
                        color = 8
                    case lon if lon < 1000:
                        color = 9
                    case lon if lon > 1000:
                        color = 10

                data_density.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2000, 'color': color})

    lat_int = 90
    for lat in density_array_2005:
        lat_int -= 1
        lon_int = -180
        for lon in lat:
            lon_int += 1
            # отсеиваем пустые пустые значения
            if lon > 0:
                match lon:
                    case lon if lon < 5:
                        color = 1
                    case lon if lon < 20:
                        color = 2
                    case lon if lon < 70:
                        color = 3
                    case lon if lon < 150:
                        color = 4
                    case lon if lon < 200:
                        color = 5
                    case lon if lon < 300:
                        color = 6
                    case lon if lon < 500:
                        color = 7
                    case lon if lon < 700:
                        color = 8
                    case lon if lon < 1000:
                        color = 9
                    case lon if lon > 1000:
                        color = 10
                data_density.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2005, 'color': color})

    lat_int = 90
    for lat in density_array_2010:
        lat_int -= 1
        lon_int = -180
        for lon in lat:
            lon_int += 1
            # отсеиваем пустые пустые значения
            if lon > 0:
                match lon:
                    case lon if lon < 5:
                        color = 1
                    case lon if lon < 20:
                        color = 2
                    case lon if lon < 70:
                        color = 3
                    case lon if lon < 150:
                        color = 4
                    case lon if lon < 200:
                        color = 5
                    case lon if lon < 300:
                        color = 6
                    case lon if lon < 500:
                        color = 7
                    case lon if lon < 700:
                        color = 8
                    case lon if lon < 1000:
                        color = 9
                    case lon if lon > 1000:
                        color = 10
                data_density.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2010, 'color': color})

    lat_int = 90
    for lat in density_array_2015:
        lat_int -= 1
        lon_int = -180
        for lon in lat:
            lon_int += 1
            # отсеиваем пустые пустые значения
            if lon > 0:
                match lon:
                    case lon if lon < 5:
                        color = 1
                    case lon if lon < 20:
                        color = 2
                    case lon if lon < 70:
                        color = 3
                    case lon if lon < 150:
                        color = 4
                    case lon if lon < 200:
                        color = 5
                    case lon if lon < 300:
                        color = 6
                    case lon if lon < 500:
                        color = 7
                    case lon if lon < 700:
                        color = 8
                    case lon if lon < 1000:
                        color = 9
                    case lon if lon > 1000:
                        color = 10
                data_density.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2015, 'color': color})

    lat_int = 90
    for lat in density_array_2020:
        lat_int -= 1
        lon_int = -180
        for lon in lat:
            lon_int += 1
            # отсеиваем пустые пустые значения
            if lon > 0:
                match lon:
                    case lon if lon < 5:
                        color = 1
                    case lon if lon < 20:
                        color = 2
                    case lon if lon < 70:
                        color = 3
                    case lon if lon < 150:
                        color = 4
                    case lon if lon < 200:
                        color = 5
                    case lon if lon < 300:
                        color = 6
                    case lon if lon < 500:
                        color = 7
                    case lon if lon < 700:
                        color = 8
                    case lon if lon < 1000:
                        color = 9
                    case lon if lon > 1000:
                        color = 10
                data_density.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2020, 'color': color})
                # версия без времени, для отображения на тепловой карте
                # data_density_no_time.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2020})

    # версия с разрешением 30 минут
    lat_int = 90
    for lat in density_array_2020_min:
        lat_int -= 0.5
        lon_int = -180
        for lon in lat:
            lon_int += 0.5
            # отсеиваем пустые пустые значения
            if lon > 0:
                # версия без времени, для отображения на тепловой карте
                data_density_no_time.append({'lat': lat_int, 'lon': lon_int, 'pop': lon, 'year': 2020})

    return data_density, data_density_no_time


# для отладки
load_f()
