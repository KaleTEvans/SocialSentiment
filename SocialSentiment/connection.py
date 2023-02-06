import pyodbc

def connectToDB():
    conn = pyodbc.connect("Driver={SQL Server (SQLEXPRESS)};"
                            "Server=DESKTOP-FRBUP45\SQLEXPRESS;"
                            "Database=SocialSentimentDB;"
                            "Trusted_Connection=yes;")
    
    return conn