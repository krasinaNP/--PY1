money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
add_ = spend - salary  # необходимая доп. сумма на каждый месяц
while money_capital - add_ >= 0:
    money_capital -= add_
    spend = spend * (increase + 1)
    month = month + 1
    add_ = spend - salary
print(month)
