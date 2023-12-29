import sqlite3


con = sqlite3.connect('db.sqlite')
cur = con.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS debtors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    birthdate TEXT,
    birthplace TEXT,
    region TEXT,
    district TEXT,
    city TEXT,
    street TEXT,
    housenumber TEXT,
    apartmentnumber TEXT
    publishdate TEXT,
    inn INTEGER,
    snils INTEGER,
    namehistory TEXT
);

CREATE TABLE IF NOT EXISTS banks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    bik INTEGER
);

CREATE TABLE IF NOT EXISTS monetaryobligations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    creditorname TEXT,
    content TEXT,
    basis TEXT,
    totalsum REAL,
    debtsum REAL,
    penaltysum REAL
);

CREATE TABLE IF NOT EXISTS obligatorypayments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    sum REAL,
    penalty_sum REAL
);

CREATE TABLE IF NOT EXISTS publishers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    inn INTEGER,
    ogrn INTEGER
);

CREATE TABLE IF NOT EXISTS messages(
    id TEXT,
    number INTEGER,
    type TEXT
    publishdate TEXT,
    debtor_id INTEGER,
    FOREIGN KEY (debtor_id)  REFERENCES debtors (id),
    bank_id INTEGER,
    FOREIGN KEY (bank_id)  REFERENCES banks (id),
    monetaryobligation_id INTEGER,
    FOREIGN KEY (monetaryobligation_id)  REFERENCES monetaryobligations (id),
    obligatorypayment_id INTEGER,
    FOREIGN KEY (obligatorypayment_id)  REFERENCES obligatorypayments (id),
    publisher_id INTEGER,
    FOREIGN KEY (publisher_id)  REFERENCES publishers (id),
    finishreason TEXT
);
''')
con.commit()
