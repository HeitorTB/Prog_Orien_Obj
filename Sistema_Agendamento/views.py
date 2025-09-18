from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
class View: 
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone): 
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone): 
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        ClienteDAO.excluir(id)
    
    def Servico_listar():
        return ServicoDAO.listar()
    def Servico_inserir(descricao, valor): 
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def Servico_atualizar(id, descricao, valor): 
        servico = Servico(id, descricao,valor)
        ServicoDAO.inserir(servico)
    def Servico_excluir(id): 
        ServicoDAO.excluir(id)

