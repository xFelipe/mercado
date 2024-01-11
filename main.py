from fastapi import FastAPI, HTTPException
from typing import List
from models import Categoria


app = FastAPI()

exemplo_categorias = { 
    1: Categoria(nome="Bebidas"),
}

@app.get("/")
async def hello():
    return {"message": "Hello Worldd"}


@app.get("/categorias", response_model=List[Categoria])
async def get_categorias():
    return exemplo_categorias.values() 


@app.get("/categorias/{categoria_id}", response_model=Categoria)
async def get_categoria(categoria_id: int):
    categoria = exemplo_categorias.get(categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria


@app.post("/categorias", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    id = max(exemplo_categorias.keys()) + 1
    exemplo_categorias[id] = Categoria(**categoria.dict())
    return exemplo_categorias[id]

@app.put("/categorias/{categoria_id}", response_model=Categoria)
async def update_categoria(categoria_id: int, categoria: Categoria):
    updated_categoria = exemplo_categorias.get(categoria_id)

    if not updated_categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")

    if categoria.nome and categoria.nome != updated_categoria.nome:
        updated_categoria.nome = categoria.nome

    return updated_categoria


@app.delete("/categorias/{categoria_id}")
async def delete_categoria(categoria_id: int):
    if categoria_id not in exemplo_categorias.keys():
        raise HTTPException(status_code=404, detail="Categoria not found")
        
    return exemplo_categorias.pop(categoria_id)

    # Repeat the above pattern for the other models (Produto, Venda, ItemVenda, User)

