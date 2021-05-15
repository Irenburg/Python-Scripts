from datetime import date ; from hijri_converter import convert ; from random import choice ; from time import sleep

def do_greetings():
  ls = ['عيدكم مبارك','عيد سعيد','تقبل الله منا و منكم','كل عام و أنتم بخير']
  print(choice(ls))

def check_for_eid():
  today = date.today()
  h = convert.Gregorian(today.year, today.month, today.day).to_hijri()
  if (h.month == 10 and h.day in (1, 2, 3)) or (h.month == 12 and h.day in (10, 11, 12)):
    return True
  else:
    return False

while check_for_eid():
  do_greetings()
  sleep(3)
else:
  print('العام القادم إن شاء الله')
