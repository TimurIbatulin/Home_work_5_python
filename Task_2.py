# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии


name_man = ['Иван', 'Петр', 'Семен', 'Максим']
salary = [10, 200, 300, 400]
premium = ['10.25%', '11.74%', '70.45%', '56.44%']

happy_worker = {name_1: int(sal) * (float(pre.replace('%', ''))/100)  for name_1 in name_man for sal in salary for pre in premium}
print(happy_worker)