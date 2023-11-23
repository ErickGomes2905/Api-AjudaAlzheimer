from fastapi import FastAPI, HTTPException

app = FastAPI()

usuarios = {
   1: {"email": "rm95455@fiap.com.br", "senha": "123456789", "nome": "erick gomes"}
}

pessoasConfiaveis = {
   1: {"nome": "Veronica Gomes", "Relação": "Filha", "Contato": "(11) 98745-2532"}
}

memorias = {
   1: {"data": "2023-10-21", "local": "Praia de Bertioga", "Pessoas Presentes": "erick (neto), joao (filho), maria (sobrinha)", "acontecimento": "Estavam na praia curtindo um sol quando começou uma tempestade que levou todas as coisas embora, perdemos todas as toalhas e coisas que estavam soltas"}
}

medicamentos = {
  1: {"nome": "Tebonin 120mg", "dosagem": "2 comprimidos", "intervalo": "8 horas", "efeitos colaterias": "distúrbios gastrintestinais, dor de cabeça e reações alérgicas na pele (vermelhidão, inchaço e coceira)"},
  2: {"nome": "Cloridrato de Donepezila 10mg", "dosagem": "1 comprimido", "intervalo": "12 horas", "efeitos colaterias": "dores, acidentes, fadiga, desmaios, vômitos, anorexia, cãibras, insônia, tontura, sonhos anormais, resfriado comum e distúrbios abdominais"},
  3: {"nome": "Risperidona 1mg", "dosagem": "1 comprimido", "intervalo": "8 horas", "efeitos colaterias": "vômito, náusea, diarreia, prisão de ventre, ganho de peso, boca seca, aumento da saliva e dor de estômago"},
  4: {"nome": "Cloridrato Memantina 10mg", "dosagem": "1 comprimido", "intervalo": "24 horas", "efeitos colaterias": "Dor de cabeça, sonolência, prisão de ventre, tonturas, distúrbios de equilíbrio, falta de ar (dispneia)"},
}

@app.get("/")
def home():
  return {"Medicamentos": len(medicamentos),
        "Memorias": len(memorias),
        "Pessoas Confiaveis": len(pessoasConfiaveis)}


@app.get("/medicamentos")
def pegar_medicamentos():
  return medicamentos

@app.get("/medicamentos/{id_medicamento}")
def pegar_medicamento(id_medicamento: int):
  if id_medicamento in medicamentos:
    return medicamentos[id_medicamento]
  else:
    return {"Id de medicamento não encontrado"}
  
@app.post("/medicamentos")
def post_medicamento(nome: str, dosagem: str, intervalo: str, efeitos_colaterais: str):
    novo_id = max(medicamentos.keys(), default=0) + 1
    novo_medicamento = {
        "nome": nome,
        "dosagem": dosagem,
        "intervalo": intervalo,
        "efeitos_colaterais": efeitos_colaterais,
    }
    medicamentos[novo_id] = novo_medicamento
    return {"message": "Medicamento adicionado com sucesso", "id_medicamento": novo_id}

@app.put("/medicamentos/{id_medicamento}")
def atualizar_medicamento(id_medicamento: int, nome: str, dosagem: str, intervalo: str, efeitos_colaterais: str):
    if id_medicamento in medicamentos:
        medicamentos[id_medicamento] = {
            "nome": nome,
            "dosagem": dosagem,
            "intervalo": intervalo,
            "efeitos_colaterais": efeitos_colaterais,
        }
        return {"message": f"Medicamento {id_medicamento} atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de medicamento não encontrado")
    
@app.delete("/medicamentos/{id_medicamento}")
def deletar_medicamento(id_medicamento: int):
    if id_medicamento in medicamentos:
        del medicamentos[id_medicamento]
        return {"message": f"Medicamento {id_medicamento} removido com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de medicamento não encontrado")
    
@app.get("/memorias")
def pegar_memorias():
  return memorias

@app.get("/memorias/{id_memoria}")
def pegar_memoria(id_memoria: int):
  if id_memoria in memorias:
    return medicamentos[id_memoria]
  else:
    return {"Id de memoria não encontrado"}
  
@app.post("/memorias")
def post_medicamento(data: str, local: str, pessoas: str, acontecimento: str):
    novo_id = max(memorias.keys(), default=0) + 1
    nova_memoria = {
        "data": data,
        "local": local,
        "pessoas": pessoas,
        "acontecimento": acontecimento,
    }
    memorias[novo_id] = nova_memoria
    return {"message": "Memoria adicionado com sucesso", "id_memoria": novo_id}

@app.put("/memorias/{id_memoria}")
def atualizar_memoria(id_memoria: int, data: str, local: str, pessoas: str, acontecimento: str):
    if id_memoria in memorias:
        memorias[id_memoria] = {
            "data": data,
            "local": local,
            "pessoas": pessoas,
            "acontecimento": acontecimento,
        }
        return {"message": f"Memoria {id_memoria} atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de memoria não encontrado")
    
@app.delete("/memorias/{id_memoria}")
def deletar_memoria(id_memoria: int):
    if id_memoria in memorias:
        del memorias[id_memoria]
        return {"message": f"Memoria {id_memoria} removido com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de memoria não encontrado")
    
@app.get("/pessoasConfiaveis")
def pegar_pessoasConfiaveis():
  return pessoasConfiaveis

@app.get("/pessoasConfiaveis/{id_pessoaConfiavel}")
def pegar_pessoaConfiavel(id_pessoaConfiavel: int):
  if id_pessoaConfiavel in pessoasConfiaveis:
    return pessoasConfiaveis[id_pessoaConfiavel]
  else:
    return {"Id de pessoa confiavel não encontrado"}
  
@app.post("/pessoasConfiaveis")
def post_pessoaConfiavel(nome: str, relação: str, contato: str):
    novo_id = max(pessoasConfiaveis.keys(), default=0) + 1
    nova_pessoaConfiavel = {
        "nome": nome,
        "relação": relação,
        "contato": contato,
    }
    pessoasConfiaveis[novo_id] = nova_pessoaConfiavel
    return {"message": "pessoa confiavel adicionado com sucesso", "id_pessoaConfiavel": novo_id}

@app.put("/pessoasConfiaveis/{id_pessoaconfiavel}")
def atualizar_pessoaconfiavel(id_pessoaConfiavel: int, nome: str, relação: str, contato: str):
    if id_pessoaConfiavel in pessoasConfiaveis:
        pessoasConfiaveis[id_pessoaConfiavel] = {
            "nome": nome,
            "relação": relação,
            "contato": contato
        }
        return {"message": f"Pessoa confiavel {id_pessoaConfiavel} atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de pessoa confiavel não encontrado")
    
@app.delete("/pessoasConfiaveis/{id_pessoaConfiavel}")
def deletar_pessoaConfiavel(id_pessoaConfiavel: int):
    if id_pessoaConfiavel in pessoasConfiaveis:
        del pessoasConfiaveis[id_pessoaConfiavel]
        return {"message": f"Pessoa confiavel {id_pessoaConfiavel} removido com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Id de pessoa confiavel não encontrado")
    
@app.get("/usuarios")
def pegar_usuarios():
  return usuarios

@app.get("/usuarios/{email_usuario}")
def pegar_usuario(email_usuario: str):
    for usuario_id, dados_usuario in usuarios.items():
        if dados_usuario["usuario"].lower() == email_usuario.lower():
            return {usuario_id: dados_usuario}
    
    return {"Usuario não encontrado"}


@app.post("/usuarios")
def post_usuario(email: str, senha: str, nome: str):
    novo_id = max(usuarios.keys(), default=0) + 1
    novo_usuario = {
        "email": email,
        "senha": senha,
        "nome": nome,
    }
    usuarios[novo_id] = novo_usuario
    return {"message": "Usuario adicionado com sucesso", "id_usuario": novo_id}
