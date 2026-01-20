import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        port=4000,
        user="2dr6yzXnL6Bbrn7.root",
        password="8lPgy0tN2RoPunUG",
        database="phonepe",
        ssl_ca="/etc/ssl/cert.pem"
    )
    return connection
