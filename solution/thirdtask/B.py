import sqlite3
import datetime

import matplotlib.pyplot as plt


con = sqlite3.connect('db.sqlite')
cur = con.cursor()

dbvalues = list(cur.execute('''
SELECT debtor.birthdate,
       SUM(moneyobl.debtsum)
FROM debtors,
     moneyobl;
'''))

new_list = {}
for debtor in dbvalues:
    age = round(datetime.datetime.now() - debtor[0])
    if age in new_list.keys():
        new_list[age] += debtor[1]
    else:
        new_list[age] = debtor[1]

labels = list(new_list.keys())
sizes = list(new_list.values())

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
