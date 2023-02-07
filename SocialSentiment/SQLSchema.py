import pyodbc
import time

class SocialSentimentSchema():
    def __init__(self):
        self.conn = pyodbc.connect("Driver={SQL Server};"
                            "Server=DESKTOP-FRBUP45\SQLEXPRESS;"
                            "Database=SocialSentimentDB;"
                            "Trusted_Connection=yes;")
        
        self.conn.autocommit=True
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def create_table(self):
        # Make sure to remove any preexisting tables
        self.cursor.execute("DROP TABLE IF EXISTS finnhub")

        self.cursor.execute("CREATE TABLE finnhub("
                            "sentiment_id INT IDENTITY(1,1) PRIMARY KEY,"
                            "date DATETIME NOT NULL,"
                            "source VARCHAR(10) NOT NULL,"
                            "symbol VARCHAR(5) NOT NULL,"
                            "mention INTEGER,"
                            "positive_score DECIMAL(10,6),"
                            "negative_score DECIMAL(10,6),"
                            "positive_mention INTEGER,"
                            "negative_mention INTEGER,"
                            "score DECIMAL (10, 5));"
                            )
        

def main():
    ss = SocialSentimentSchema()
    time.sleep(1)
    ss.create_table()
    time.sleep(1)

    ss.cursor.execute("SELECT * FROM information_schema.tables;")
    
    for i in ss.cursor:
        print(i)

if __name__ == '__main__':
    main()