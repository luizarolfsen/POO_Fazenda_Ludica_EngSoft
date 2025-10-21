class Animal:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def emitir_som(self):
     return "O animal emite um som."
    
  def apresentar(self): 
     return f"Olá, sou {self.nome} e tenho {self.idade} anos."

class Cachorro(Animal):
   def __init__ (self, nome, idade, raca): 
       super().__init__(nome, idade)
       self.raca = raca  
   def emitir_som(self):
      return "Au Au!"
    
class Gato(Animal):
   def __init__ (self, nome, idade, cor_pelo):
       super().__init__(nome, idade)
       self.cor_pelo = cor_pelo
   def emitir_som(self):
      return "Miau Miau!"
   
class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros=20):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros

    @property
    def producao_leite_litros(self):
        return self.__producao_leite_litros

    def emitir_som(self):
        return "Muu Muu!"
   
    
cachorro1 = Cachorro("Rex", 5, "Doberman")
gato1 = Gato("Marrie", 3, "Laranja")
vaca1 = Vaca("Mimosa", 4, 25)

animais = [cachorro1, gato1, vaca1]

for animal in animais:
   print(animal.apresentar())
   print(animal.emitir_som())
