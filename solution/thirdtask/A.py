import sqlite3

import matplotlib.pyplot as plt


con = sqlite3.connect('db.sqlite')
cur = con.cursor()

dbvalues = list(cur.execute('''
SELECT debtor.region,
       SUM(moneyobl.debtsum)
FROM debtors,
     moneyobl;
'''))

new_list = {}
for region in dbvalues:
    if region[0] in new_list.keys():
        new_list[region[0]] += region[1]
    else:
        new_list[region[0]] = region[1]

labels = list(new_list.keys())
sizes = list(new_list.values())

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
