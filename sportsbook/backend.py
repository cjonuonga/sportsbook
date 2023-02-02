import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("sportsbook.db")
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS sportsbook (id INTEGER PRIMARY KEY, player1 text, player2 text, stat1 text, stat2 text, ovrundr1 text, ovrundr2 text, betamnt integer)")
        # creates tabels and sets keys(columns) in database
        self.conn.commit()
        self.conn.close()



    def add_bet(self, player1, player2, stat1, stat2, ovrundr1, ovrundr2, betamnt):
        self.conn = sqlite3.connect("sportsbook.db")
        cur = self.conn.cursor()
        self.conn.execute("INSERT INTO sportsbook VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (player1, player2, stat1, stat2, ovrundr1, ovrundr2, betamnt))
        self.conn.commit()
        self.conn.close()
        

    def all_bets(self):
        self.conn = sqlite3.connect("sportsbook.db")
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM sportsbook")
        rows = cur.fetchall()


    def delete_bets(self):
        self.conn = sqlite3.connect("sportsbook.db")
        cur = self.conn.cursor()
        self.conn.execute("DELETE FROM sportsbook WHERE id = ?" , (id,))
        self.conn.commit()
        self.conn.close()


    

d = Database()
d.__init__()

d.add_bet("bron","steph","0.5 pts","0.5 pts","more","more", 20)
print(d.all_bets())


    



