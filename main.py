import flet as ft

def main(pg):
    #ELEMENTOS
    texto = ft.Text("Estoque de Remedios")
    lista = ft.Column()
    adic = ft.ElevatedButton("adicionar")
    remove = ft.ElevatedButton("remover")
    altera = ft.ElevatedButton("alterar")
   
     
    #ADICIONAR
    pg.add(texto)
    pg.add(lista)
    pg.add(ft.Row([remove,altera,adic]))
ft.app(target=main)