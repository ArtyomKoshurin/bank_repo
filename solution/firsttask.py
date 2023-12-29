import sqlite3

from xml.etree import ElementTree


tree = ElementTree.parse("solution/test_file.xml")
root = tree.getroot()

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS debtors(
    id INTEGER PRIMARY KEY,
    debname TEXT,
    birthdate TEXT,
    birthplace TEXT,
    adress TEXT,
    inn INTEGER,
    namehistory TEXT,
    message_id INTEGER,
    FOREIGN KEY (message_id)  REFERENCES messages (id)
);

CREATE TABLE IF NOT EXISTS banks(
    id INTEGER PRIMARY KEY,
    bankname TEXT,
    bik INTEGER,
    message_id INTEGER,
    FOREIGN KEY (message_id)  REFERENCES messages (id)
);

CREATE TABLE IF NOT EXISTS moneyobl(
    id INTEGER PRIMARY KEY,
    creditorname TEXT,
    content TEXT,
    basis TEXT,
    totalsum REAL,
    debtsum REAL,
    penaltysum REAL,
    message_id INTEGER,
    FOREIGN KEY (message_id)  REFERENCES messages (id)
);

CREATE TABLE IF NOT EXISTS obligatorypayments(
    id INTEGER PRIMARY KEY,
    oblname TEXT,
    sum REAL,
    oblpenaltysum REAL,
    message_id INTEGER,
    FOREIGN KEY (message_id)  REFERENCES messages (id)
);

CREATE TABLE IF NOT EXISTS publishers(
    id INTEGER PRIMARY KEY,
    pubname TEXT,
    inn INTEGER,
    ogrn INTEGER,
    message_id INTEGER,
    FOREIGN KEY (message_id)  REFERENCES messages (id)
);

CREATE TABLE IF NOT EXISTS messages(
    id TEXT,
    number INTEGER,
    type TEXT,
    publishdate TEXT,
    finishreason TEXT
);
''')
con.commit()

bank_id = 1
obl_id = 1
monobl_id = 1


for message in range(0, len(root)):
    message_id = root[message][0].text
    number = root[message][1].text
    type = root[message][2].text
    publish_date = root[message][3].text
    if root[message][6].tag == 'FinishReason':
        finish_reason = root[message][6].text
    else:
        finish_reason = None

    cur.execute(
        'INSERT INTO messages VALUES(?, ?, ?, ?, ?);',
        (message_id, number, type, publish_date, finish_reason)
    )
    con.commit()

    debtor_id = message + 1
    debtor = root[message][4]
    debtor_name = debtor[0].text
    birth_date = debtor[1].text
    birth_place = debtor[2].text
    adress = debtor[3].text
    if len(debtor) == 4 or debtor[4].tag != 'Inn':
        debtor_inn = None
    else:
        debtor_inn = debtor[4].text
    if len(debtor) in [4, 5] or debtor[5].tag != 'NameHistory':
        name_history = None
    else:
        names = []
        for prev_name in debtor[5].findall('PreviousName'):
            names.append(prev_name.find('Value').text)
        name_history = ', '.join(names)

    cur.execute(
        'INSERT INTO debtors VALUES(?, ?, ?, ?, ?, ?, ?, ?);',
        (debtor_id, debtor_name, birth_date, birth_place,
         adress, debtor_inn, name_history, message_id)
    )
    con.commit()

    publisher_id = message + 1
    publisher = root[message][5]
    publisher_name = publisher[0].text
    publisher_inn = publisher[1].text
    publisher_ogrn = publisher[2].text

    cur.execute(
        'INSERT INTO publishers VALUES(?, ?, ?, ?, ?);',
        (publisher_id, publisher_name, publisher_inn,
         publisher_ogrn, message_id)
    )
    con.commit()

    if root[message][6].tag == 'FinishReason':
        finish_reason = root[message][6].text

    else:
        for bank in root[message][6]:
            bank_name = bank[0].text
            if len(bank) == 1 or bank[1].tag != 'Bik':
                bik = None
            else:
                bik = bank[1].text
                cur.execute(
                    'INSERT INTO banks VALUES(?, ?, ?, ?);',
                    (bank_id, bank_name, bik, message_id)
                )
                con.commit()
            bank_id += 1

        for obl in root[message].findall('.//ObligatoryPayment'):
            obl_name = obl[0].text
            obl_sum = obl[1].text
            if len(obl) == 2:
                penalty_sum = None
            else:
                penalty_sum = obl[2].text
                cur.execute(
                    'INSERT INTO obligatorypayments VALUES(?, ?, ?, ?, ?);',
                    (obl_id, obl_name, obl_sum,
                     penalty_sum, message_id)
                )
                con.commit()
            obl_id += 1

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
                cur.execute(
                    'INSERT INTO moneyobl VALUES(?, ?, ?, ?, ?, ?, ?, ?);',
                    (monobl_id, creditor_name, content, basis,
                     total_sum, debt_sum, penalty_sum, message_id)
                )
                con.commit()
            monobl_id += 1


con.commit()
con.close()
