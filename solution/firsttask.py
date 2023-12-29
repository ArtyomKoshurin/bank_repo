from xml.etree import ElementTree


tree = ElementTree.parse("solution/test_file.xml")
root = tree.getroot()

for message in range(0, len(root)):
    id = root[message][0].text
    number = root[message][1].text
    type = root[message][2].text
    publish_date = root[message][3].text

    debtor = root[message][4]
    debtor_name = debtor[0].text
    birth_date = debtor[1].text
    birth_place = debtor[2].text
    adress = debtor[3].text.split(',')
    if len(debtor) == 4 or debtor[4].tag != 'Inn':
        debtor_inn = None
    else:
        debtor_inn = debtor[4].text
    if len(debtor) in [4, 5] or debtor[5].tag != 'NameHistory':
        name_history = None
    else:
        name_history = []
        for prev_name in debtor[5].findall('PreviousName'):
            name_history.append(prev_name.find('Value').text)

    publisher = root[message][5]
    publisher_name = publisher[0].text
    publisher_inn = publisher[1].text
    publisher_ogrn = publisher[2].text

    if root[message][6].tag == 'FinishReason':
        bank_id = None
        monetaryobligation_id = None
        obligatorypayment_id = None
        finish_reason = root[message][6].text
    else:

        finish_reason = None
        bank_id = []
        for bank in root[message][6]:
            bank_name = bank[0].text
            if len(bank) == 1 or bank[1].tag != 'Bik':
                bik = None
            else:
                bik = bank[1].text
            bank_id.append(bank_name)
            bank_id.append(bik)

        obligatorypayment_id = []
        for obl in root[message].findall('.//ObligatoryPayment'):
            name = obl[0].text
            sum = obl[1].text
            if len(obl) == 2:
                penalty_sum = None
            else:
                penalty_sum = obl[2].text
            obligatorypayment_id.append(name)
            obligatorypayment_id.append(sum)
            obligatorypayment_id.append(penalty_sum)

        monetaryobligation_id = []
        for monobl in root[message].findall('.//MonetaryObligation'):
            creditor_name = monobl[0].text
            content = monobl[1].text
            basis = monobl[2].text
            total_sum = monobl[3].text
            if len(monobl) == 4:
                debt_sum = None
                penalty_sum = None
            elif monobl[4].tag == 'DebtSum' and len(monobl) == 5:
                debt_sum = monobl[4].text
                penalty_sum = None
            elif monobl[4].tag == 'PenaltySum' and len(monobl) == 5:
                penalty_sum = monobl[4].text
                debt_sum = None
            elif monobl[5].tag == 'PenaltySum' and len(monobl) == 6:
                penalty_sum = monobl[5].text
            monetaryobligation_id.append(creditor_name)
            monetaryobligation_id.append(content)
            monetaryobligation_id.append(basis)
            monetaryobligation_id.append(total_sum)
            monetaryobligation_id.append(debt_sum)
            monetaryobligation_id.append(penalty_sum)

    print(id)
    print(number)
    print(type)
    print(publish_date)
    print(debtor_name)
    print(birth_date)
    print(birth_place)
    print(adress)
    print(debtor_inn)
    print(name_history)
    print(publisher_name)
    print(publisher_inn)
    print(publisher_ogrn)
    print(bank_id)
    print(monetaryobligation_id)
    print(obligatorypayment_id)
    print(finish_reason)
    print('\n')
