from tqdm import tqdm
import numpy as np
def create():
    for _ in tqdm(range(7), desc='Создание континентов:'):
        pass
    for _ in tqdm(np.arange(2.7e6), desc='Создание городов:'):
        pass
    for i in tqdm(np.arange(10e9), desc='Обновление базы данных '
                                        'пользователей:'):
        try:
            i <= 10e7
        except:
            raise ValueError('Ошибка обновления базы данных')