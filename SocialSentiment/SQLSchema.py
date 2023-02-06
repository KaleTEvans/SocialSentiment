import pyodbc

class SocialSentimentSchema():
    def __init__(self):
        self.conn = pyodbc.connect("Driver={SQL Server (SQLEXPRESS)};"
                            "Server=DESKTOP-FRBUP45\SQLEXPRESS;"
                            "Database=SocialSentimentDB;"
                            "Trusted_Connection=yes;")
        
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # def create_table(self, ticker):
    #     # Make sure to remove any preexisting tables
    #     self.cursor.execute(f"DROP TABLE IF EXISTS {ticker}")

    #     self.cursor.execute(f"CREATE TABLE {ticker}("
    #                         "sentiment_id INT IDENTITY(1,1) PRIMARY KEY,"
    #                         "date DATETIME NOT NULL,"
    #                         )