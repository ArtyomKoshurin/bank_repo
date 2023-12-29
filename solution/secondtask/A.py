SELECT debtor.debname,
       debtor.inn,
       COUNT(moneyobl)
FROM debtor,
     moneyobl
WHERE debtor.message_id = moneyobl.message_id
ORDER BY COUNT(moneyobl) DESC
LIMIT 10;