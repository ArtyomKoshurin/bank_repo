SELECT debtor.debname,
       debtor.inn,
       SUM(moneyobl.debtsum)
FROM debtor,
     moneyobl
WHERE debtor.message_id = moneyobl.message_id
ORDER BY SUM(moneyobl.debtsum) DESC
LIMIT 10;