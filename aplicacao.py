from frontend import *
import backend as core

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    try:
        if app.selected:
            core.update(app.selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
            view_command()
        else:
            print("Erro: Nenhum registro selecionado para atualização.")
    except Exception as e:
        print(f"Erro ao atualizar o registro: {e}")

def del_command():
    try:
        if not app.selected:
            print("Aviso", "Nenhum registro selecionado para exclusão.")
            return

        record_id = app.selected[0]
        confirm = print("Confirmação", "Tem certeza de que deseja excluir?")
        if confirm:
            core.delete(record_id)
            print("Sucesso", "Registro excluido com sucesso")
            view_command()
    except Exception as e:
        print(f"Erro ao deletar o registro: {e}")

def get_selected_row(event=None):
    try:
        index = app.listClientes.curselection()
        if not index:
            app.selected = None
            return

        app.selected = app.listClientes.get(index[0])
        app.entNome.delete(0, END)
        app.entNome.insert(END, app.selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, app.selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, app.selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, app.selected[4])
    except Exception as e:
        print(f"Erro ao selecionar a linha: {e}")
        app.selected = None


if __name__ == "__main__":
    window = Tk()
    app = Gui(window)
    app.listClientes.bind('<<ListboxSelect>>', get_selected_row)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
