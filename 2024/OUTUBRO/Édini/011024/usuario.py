from Db import Database
class Usuario:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.conectar()
    # CREATE
    def CriarUsuario(self,nome,email):
        query = "INSERT INTO usuario (nome,email) VALUES (?,?,?)"
        self.db.executar(query, (nome,email))
        self.db.commit()
    
    #READ
    def listarUsuarios(self):
        query = "SELECT * FROM USUARIO"
        self.db.executar(query)
        dados = self.db.fetchAll()
        return dados
    
    # UPDATE
    def atualizarUsuario(self, id, novoNome, novoEmail):
        query = "UPDATE usuario SET nome = ?, email = ? where id = ?"
        self.db.executar(query,(novoNome, novoEmail, id))
        self.db.commit()




# usuario = Usuario('bandoDados.db')

# lista = usuario.listarUsuarios()
# print(lista)




