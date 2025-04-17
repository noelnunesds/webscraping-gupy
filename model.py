from sqlalchemy import Column, Integer, String, DateTime, func 
from db import Base 

class Palavra(Base):
    __tablename__ = 'palavras_gupy'
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    palavra = Column(String, index=True)
    contagem = Column(Integer, default=1)
    
    


