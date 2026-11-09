import sqlite3

def transfer(from_id, to_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if from_id == to_id:
        raise ValueError("Cannot send money to yourself")

    conn = sqlite3.connect("wallet.db")
    cur = conn.cursor()
    try:
        cur.execute("UPDATE wallets SET balance = balance - ? WHERE user_id = ?", (amount, from_id))
        cur.execute("UPDATE wallets SET balance = balance + ? WHERE user_id = ?", (amount, to_id))
        cur.execute(
            "INSERT INTO transactions (from_user, to_user, amount) VALUES (?, ?, ?)",
            (from_id, to_id, amount),
        )
        conn.commit()      # all three succeed together
    except Exception:
        conn.rollback()    # or none of them happen
        raise
    finally:
        conn.close()