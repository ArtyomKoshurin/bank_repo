# for element in root.iter("Debtor"):
#    name = element[0].text
#    birth_date = element[1].text
#    birth_place = element[2].text
#    adress = element[3].text.split(',')
#    if len(element) == 4 or element[4].tag != 'Inn':
#        inn = None
#    else:
#        inn = element[4].text
#    if len(element) in [4, 5] or element[5].tag != 'NameHistory':
#        name_history = None
#    else:
#        name_history = []
#        for prev_name in element[5].findall('PreviousName'):
#            name_history.append(prev_name.find('Value').text)

# for element in root.iter("Bank"):
#    name = element[0].text
#    if len(element) == 1 or element[1].tag != 'Bik':
#        bik = None
#    else:
#        bik = element[1].text

# for element in root.iter("MonetaryObligation"):
#    creditor_name = element[0].text
#    content = element[1].text
#    basis = element[2].text
#    total_sum = element[3].text
#    if len(element) == 4:
#        debt_sum = None
#        penalty_sum = None
#    elif element[4].tag == 'DebtSum' and len(element) == 5:
#        debt_sum = element[4].text
#        penalty_sum = None
#    elif element[4].tag == 'PenaltySum' and len(element) == 5:
#        penalty_sum = element[4].text
#        debt_sum = None
#    elif element[5].tag == 'PenaltySum' and len(element) == 6:
#        penalty_sum = element[5].text

# for element in root.iter("ObligatoryPayment"):
#    name = element[0].text
#    sum = element[1].text
#    if len(element) == 2:
#        penalty_sum = None
#    else:
#        penalty_sum = element[2].text
