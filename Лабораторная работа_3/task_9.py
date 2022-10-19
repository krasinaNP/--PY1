salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months > 0:
    months = months - 1
    add_ = spend - salary  # необходимая доп. сумма на каждый месяц
    need_money += add_
    spend = spend * (increase + 1)
print(round(need_money))
