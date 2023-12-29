SELECT debtor.name,
       debtor.inn,
       ROUND((SUM(moneyobl.totalsum) - SUM(moneyobl.debtsum)) / SUM(moneyobl.totalsum) * 100) AS percent
FROM debtor,
     moneyobl
WHERE debtor.message_id = moneyobl.message_id
ORDER BY percent;
