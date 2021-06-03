# Задание 7_1
# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлоны в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число

def dyim_v_sant(d):  # Дюймы в сантиметры
    d *= 2.54
    return d


def sant_v_dyim(s):  # Сантиметры в дюймы
    s /= 2.54
    return s


def mili_v_km(m):  # Мили в километры
    m *= 1.6
    return m


def km_v_mili(k):  # Километры в мили
    k /= 1.6
    return k


def funt_v_kg(f):  # Фунты в килограммы
    f /= 2.2
    return f


def kg_v_funt(kg):  # Килограммы в фунты
    kg *= 2.2
    return kg


def unc_v_gr(u):  # Унции в граммы
    u *= 28.35
    return u

def gr_v_unc(gr):  # Граммы в унции
    gr /= 28.35
    return gr


def gall_v_litr(g):  # Галлоны в литры
    g *= 4.55
    return g


def litr_v_gall(lt):  # Литры в галлоны
    lt /= 4.55
    return lt


def pint_v_litr(p):  # Пинты в литры
    p /= 1.76
    return p


def litr_v_pint(lit):  # Литры в пинты
    lit *= 1.76
    return lit
