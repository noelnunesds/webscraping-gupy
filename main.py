from db import engine, Base, get_db
import model
from crud import salvar_no_banco
from scraping import extrair_palavras

model.Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    url = str(input('Digite uma url: '))
    
    palavras = extrair_palavras(url)
    
    with next(get_db()) as db:
        salvar_no_banco(palavras, db)
