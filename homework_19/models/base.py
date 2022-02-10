from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import config
engine = create_engine(
    config.SQLALCHEMY_CONN_URL,
    echo=config.SQLALCHEMY_ECHO,
)
Base = declarative_base(bind=engine)
