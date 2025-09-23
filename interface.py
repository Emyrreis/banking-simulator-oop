from tkinter import *
from tkinter import messagebox
from bank import Account

BG_COLOR = "#1e1e3f"       #Fundo escuro
CARD_COLOR = "#e0e0e5"     #Card central
BUTTON_COLOR = "#2d2d7a"   #Botão padrão
BUTTON_HOVER = "#4a4abf"   #Hover do botão
TEXT_COLOR = "#333333"     #Texto
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_SUBTITLE = ("Helvetica", 14, "bold")
FONT_NORMAL = ("Helvetica", 12)

#Contas
conta1 = Account("Emilly Reis", "0001", "12345-6", "1234", balance = 1000.0)
conta2 = Account("Bella Santos", "0002", "65432-1", "4321", balance = 500.0)

#conta2.create_pix_key("123456789")


class BankApp:
    def __init__(self, master):
        self.master = master
        self.master.title("APP Bank")
        self.master.geometry("500x400")
        self.master.configure(bg = BG_COLOR)
        self.current_account = None
        self.login_screen()

    #Tela de Login
    def login_screen(self):
        self.clear_window()
        card = Frame(self.master, bg = CARD_COLOR)
        card.place(relx = 0.5, rely = 0.5, anchor = CENTER, width = 350, height = 320)

        Label(card, text ="APP Bank\nLogin", font = FONT_TITLE, bg = CARD_COLOR, fg = TEXT_COLOR).pack(pady = 15)
        
        Label(card, text = "Agência:", font = FONT_NORMAL, bg = CARD_COLOR).pack()
        self.agency_entry = Entry(card, font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.agency_entry.pack(pady = 5)

        Label(card, text = "Conta:", font = FONT_NORMAL, bg = CARD_COLOR).pack()
        self.account_entry = Entry(card, font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.account_entry.pack(pady = 5)

        Label(card, text = "Senha:", font = FONT_NORMAL, bg = CARD_COLOR).pack()
        self.pwd_entry = Entry(card, show = "*", font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.pwd_entry.pack(pady = 10)

        btn_login = Button(card, text = "Entrar", font = FONT_NORMAL, bg = BUTTON_COLOR, fg = "white", bd = 0, command = self.login)
        btn_login.pack(fill = 'x', padx = 40, pady = 5)
        self.add_hover(btn_login)

    def login(self):
        agency = self.agency_entry.get()
        account_num = self.account_entry.get()
        pwd = self.pwd_entry.get()

        for acc in (conta1, conta2):
            if acc.agency == agency and acc.account_number == account_num and acc.check_password(pwd):
                self.current_account = acc
                self.home_screen()
                return
        
        messagebox.showerror("Erro", "Agência, conta ou senha inválidos!")

    #Tela Principal
    def home_screen(self):
        self.clear_window()
        card = Frame(self.master, bg = CARD_COLOR)
        card.place(relx = 0.5, rely = 0.5, anchor = CENTER, width = 400, height = 400)

        Label(card, text = f"Bem-vindo(a), {self.current_account.name}", font = FONT_SUBTITLE, bg = CARD_COLOR, fg = TEXT_COLOR).pack(pady = 10)
        Label(card, text = f"Agência: {self.current_account.agency}", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        Label(card, text = f"Conta: {self.current_account.account_number}", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        Label(card, text = f"Saldo: R${self.current_account.balance:.2f}", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        Label(card, text = f"Limite: R${self.current_account.limit:.2f}", bg = CARD_COLOR, font = FONT_NORMAL).pack(pady = 10)

        self.create_menu_button(card, "Saque / Depósito", self.transaction_screen)
        self.create_menu_button(card, "Pix", self.pix_screen)
        self.create_menu_button(card, "Extrato", self.extrato_screen)
        self.create_menu_button(card, "Alterar Senha", self.change_password_screen)
        self.create_menu_button(card, "Alterar Limite", self.change_limit_screen)
        self.create_menu_button(card, "Sair", self.logout)

    #Tela de Transações
    def transaction_screen(self):
        self.clear_window()
        card = self.create_card("Saque / Depósito")
        Label(card, text = "Valor:", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        self.amount_entry = Entry(card, font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.amount_entry.pack(pady = 10)

        self.create_menu_button(card, "Depositar", self.deposit)
        self.create_menu_button(card, "Sacar", self.withdraw)
        self.create_menu_button(card, "Voltar", self.home_screen)

    def deposit(self):
        try:
            valor = float(self.amount_entry.get())
            if self.current_account.deposit(valor):
                messagebox.showinfo("Sucesso", f"Depósito de R${valor:.2f} realizado!")
                self.home_screen()
            else:
                messagebox.showerror("Erro", "Valor inválido.")
        except:
            messagebox.showerror("Erro", "Digite um número válido.")

    def withdraw(self):
        try:
            valor = float(self.amount_entry.get())
            if self.current_account.withdraw(valor):
                messagebox.showinfo("Sucesso", f"Saque de R${valor:.2f} realizado!")
                self.home_screen()
            else:
                messagebox.showerror("Erro", "Saque não permitido.")
        except:
            messagebox.showerror("Erro", "Digite um número válido.")

    #Tela Pix
    def pix_screen(self):
        self.clear_window()
        card = self.create_card("Pix")

        if not self.current_account.pix_key:
            # Primeiro acesso: cadastrar chave Pix
            Label(card, text = "Cadastre sua chave Pix:", bg = CARD_COLOR, font = FONT_NORMAL).pack(pady = 5)
            self.new_pix_entry = Entry(card, font = FONT_NORMAL, width = 25, bd = 2, relief = FLAT)
            self.new_pix_entry.pack(pady = 5)
            self.create_menu_button(card, "Cadastrar Chave Pix", self.register_pix_key)
        else:
            # Pix normal
            Label(card, text = f"Sua chave Pix: {self.current_account.pix_key}", bg = CARD_COLOR, font = FONT_NORMAL).pack(pady = 5)
            Label(card, text = "Chave Pix destino:", bg = CARD_COLOR, font = FONT_NORMAL).pack()
            self.pix_key_entry = Entry(card, font = FONT_NORMAL, width = 25, bd = 2, relief = FLAT)
            self.pix_key_entry.pack(pady = 5)

            Label(card, text = "Valor:", bg = CARD_COLOR, font = FONT_NORMAL).pack()
            self.pix_amount_entry = Entry(card, font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
            self.pix_amount_entry.pack(pady = 5)

            self.create_menu_button(card, "Enviar Pix", self.send_pix)
        
        self.create_menu_button(card, "Voltar", self.home_screen)

    def register_pix_key(self):
        chave = self.new_pix_entry.get()
        if self.current_account.create_pix_key(chave):
            messagebox.showinfo("Sucesso", f"Chave Pix {chave} cadastrada!")
            self.pix_screen()
        else:
            messagebox.showerror("Erro", f"Você já possui uma chave Pix: {self.current_account.pix_key}")

    def send_pix(self):
        try:
            valor = float(self.pix_amount_entry.get())
            chave = self.pix_key_entry.get()
            destino = self.current_account.send_pix(valor, chave, conta1, conta2)
            if destino:
                messagebox.showinfo("Sucesso", f"Pix enviado para {destino.name}!")
                self.home_screen()
            else:
                messagebox.showerror("Erro", "Pix não realizado. Verifique saldo ou chave.")
        except:
            messagebox.showerror("Erro", "Digite um valor válido.")

    #Tela Extrato
    def extrato_screen(self):
        self.clear_window()
        card = self.create_card("Extrato")
        for t in self.current_account.extrato():
            Label(card, text = t, anchor = 'w', bg = CARD_COLOR,  width = 400, font = ("Helvetica", 10)).pack(fill = 'x')
        self.create_menu_button(card, "Voltar", self.home_screen)

    #Tela Alterar Senha
    def change_password_screen(self):
        self.clear_window()
        card = self.create_card("Alterar Senha")

        Label(card, text = "Senha atual:", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        self.old_pwd_entry = Entry(card, show = "*", font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.old_pwd_entry.pack(pady = 5)

        Label(card, text = "Nova senha:", bg = CARD_COLOR, font = FONT_NORMAL).pack()
        self.new_pwd_entry = Entry(card, show = "*", font = FONT_NORMAL, width = 20, bd = 2, relief = FLAT)
        self.new_pwd_entry.pack(pady = 5)

        self.create_menu_button(card, "Alterar", self.change_password)
        self.create_menu_button(card, "Voltar", self.home_screen)

    def change_password(self):
        old = self.old_pwd_entry.get()
        new = self.new_pwd_entry.get()
        if self.current_account.change_password(old, new):
            messagebox.showinfo("Sucesso", "Senha alterada! Faça login novamente.")
            self.logout()
        else:
            messagebox.showerror("Erro", "Senha antiga incorreta.")

    #Tela Alterar Limite
    def change_limit_screen(self):
        self.clear_window()
        card = self.create_card("Alterar Limite")

        Label(card, text=f"Limite atual: R${self.current_account.limit:.2f}", bg=CARD_COLOR, font=FONT_NORMAL).pack(pady=5)
        Label(card, text="Novo limite:", bg=CARD_COLOR, font=FONT_NORMAL).pack()
        self.limit_entry = Entry(card, font=FONT_NORMAL, width=20, bd=2, relief=FLAT)
        self.limit_entry.pack(pady=10)

        self.create_menu_button(card, "Alterar", self.change_limit)
        self.create_menu_button(card, "Voltar", self.home_screen)

    def change_limit(self):
        try:
            novo = float(self.limit_entry.get())
            if self.current_account.change_limit(novo):
                messagebox.showinfo("Sucesso", f"Novo limite: R${novo:.2f}")
                self.home_screen()
            else:
                messagebox.showerror("Erro", "Não foi possível alterar o limite.")
        except:
            messagebox.showerror("Erro", "Digite um valor válido.")

    #Funções Auxiliares
    def logout(self):
        self.current_account = None
        self.login_screen()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_card(self, title):
        card = Frame(self.master, bg = CARD_COLOR)
        card.place(relx = 0.5, rely = 0.5, anchor = CENTER, width = 400, height = 300)
        Label(card, text = title, font = FONT_SUBTITLE, bg = CARD_COLOR, fg = TEXT_COLOR).pack(pady = 10)
        return card

    def create_menu_button(self, parent, text, command):
        btn = Button(parent, text = text, font = FONT_NORMAL, bg = BUTTON_COLOR, fg = "white", bd = 0, command = command)
        btn.pack(fill = 'x', padx = 40, pady = 3)
        self.add_hover(btn)

    def add_hover(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg=BUTTON_HOVER))
        widget.bind("<Leave>", lambda e: widget.config(bg=BUTTON_COLOR))


root = Tk()
app = BankApp(root)
root.mainloop()
