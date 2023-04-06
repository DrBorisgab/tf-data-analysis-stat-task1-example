import pandas as pd
import numpy as np
import scipy.stats as sts

chat_id = 530463349 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 67
    e = sts.laplace().rvs(len(x))
    a = (x - e)/t**2
    return a.mean() # Ваш ответ
