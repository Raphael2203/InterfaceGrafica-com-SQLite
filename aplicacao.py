from tkinter import Tk, messagebox
from frontend import Gui
from backend import view, search, insert, update, delete

class Application:
    def __init__(self, master):
        self.window = master
        self.gui = Gui(self.window)
        self.selected = None

        #Associar comandos aos botões
        self.gui.btnViewAll.config(command=self.view_command)
        self.gui.btnBuscar.config(command=self.search_command)
        self.gui.btnInserir.config(command=self.insert_command)
        self.gui.btnUpdate.config(command=self.update_command)
        self.gui.btnDel.config(command=self.del_command)

        #Vincular seleção de linha na lista de clientes
        self.gui.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)

    def view_command(self):
        rows = view()
        self.gui.listClientes.delete(0, 'end')
        for r in rows:
            self.gui.listClientes.insert('end', r)

    def search_command(self):
        self.gui.listClientes.delete(0, 'end')
        rows = search(self.gui.txtNome.get(), self.gui.txtSobrenome.get(), self.gui.txtEmail.get(), self.gui.txtCPF.get())
        for r in rows:
            self.gui.listClientes.insert('end', r)

    def insert_command(self):
        insert(self.gui.txtNome.get(), self.gui.txtSobrenome.get(), self.gui.txtEmail.get(), self.gui.txtCPF.get())
        self.view_command()

    def update_command(self):
        try:
            if self.selected:
                update(self.selected[0], self.gui.txtNome.get(), self.gui.txtSobrenome.get(), self.gui.txtEmail.get(), self.gui.txtCPF.get())
                self.view_command()
            else:
                messagebox.showerror("Erro", "Nenhum registro selecionado para atualização.")
        except Exception as e:
            messagebox.showerror("Erro ao atualizar o registro", str(e))

    def del_command(self):
        try:
            if not self.selected:
                messagebox.showwarning("Aviso", "Nenhum registro selecionado para exclusão.")
                return

            record_id = self.selected[0]
            confirm = messagebox.askyesno("Confirmação","Tem certeza de que deseja excluir?")
            if confirm:
                delete(record_id)
                messagebox.showinfo("Sucesso", "Registro excluido com sucesso")
                self.view_command()
            else:
                messagebox.showinfo("Cancelado","Ação cancelada pelo usuário.")
        except Exception as e:
            messagebox.showerror("Erro ao deletar o registro", str(e))

    def get_selected_row(self, event=None):
        try:
            index = self.gui.listClientes.curselection()
            if not index:
                self.selected = None
                return

            self.selected = self.gui.listClientes.get(index[0])
            self.gui.txtNome.set(self.selected[1])
            self.gui.txtSobrenome.set(self.selected[2])
            self.gui.txtEmail.set(self.selected[3])
            self.gui.txtCPF.set(self.selected[4])
        except Exception as e:
            messagebox.showerror("Erro ao selecionar a linha",str(e))
            self.selected = None


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()