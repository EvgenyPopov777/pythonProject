host = "127.0.0.1"
user = "root"
password = "root"
port = "3306"
dbname = "homework_19"
SQLALCHEMY_CONN_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}"
SQLALCHEMY_ECHO = True
print(SQLALCHEMY_CONN_URL)
