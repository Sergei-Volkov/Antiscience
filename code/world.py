from tqdm import tqdm
import numpy as np
def create():
    for _ in tqdm(range(7), desc='Создание континентов'):
        pass
    for _ in tqdm(np.arange(2.7e6), desc='Создание городов'):
        pass
    for i in tqdm(np.arange(0, 7.5), desc='Обновление базы данных пользователей'):
        if i <= 5:
            raise ValueError('Ошибка обновления базы данных')