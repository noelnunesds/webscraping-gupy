from sqlalchemy.orm import Session
from model import Palavra

def salvar_no_banco(contagem: dict, db: Session):
    for palavra, qtd in contagem.items():
        if len(palavra) <= 3:
            continue

        palavra_existente = db.query(Palavra).filter_by(palavra=palavra).first()

        if palavra_existente:
            palavra_existente.contagem += qtd
        else:
            nova = Palavra(palavra=palavra, contagem=qtd)
            db.add(nova)

    db.commit()