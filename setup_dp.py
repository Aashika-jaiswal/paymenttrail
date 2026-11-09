import sqlite3

conn = sqlite3.connect("wallet.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS wallets (
    user_id INTEGER PRIMARY KEY,
    balance INTEGER NOT NULL CHECK (balance >= 0)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user INTEGER NOT NULL,
    to_user INTEGER NOT NULL,
    amount INTEGER NOT NULL CHECK (amount > 0),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, 'Aashika')")
cur.execute("INSERT OR IGNORE INTO users (id, name) VALUES (2, 'Rahul')")
cur.execute("INSERT OR IGNORE INTO wallets (user_id, balance) VALUES (1, 1000)")
cur.execute("INSERT OR IGNORE INTO wallets (user_id, balance) VALUES (2, 1000)")

conn.commit()

for row in cur.execute("SELECT * FROM wallets"):
    print(row)

conn.close()