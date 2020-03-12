import sys

#
# Receiver
# knows how to perform the operations associated 
# with carrying out a request
#
class Word:
  def action(self):
    print("Word: ejecutar accion.")

#
# Command
# declares an interface for all commands
#
class Command:
  def execute(self, accion):
    if accion == "Abrir":
      return Abrir
    if accion == "Imprimir":
      return Imprimir
    if accion == "Guardar":
      return Guardar
    pass

#
# Concrete Command
# implements execute by invoking the corresponding 
# operation(s) on Receiver 
#
class Abrir(Command):
  def __init__(self, word):
    self.imagen = "./imagenes/Command/A.jpg"
    self.word = Word

  def execute(self):
    self.word.action()
    print("Abrir")


class Imprimir(Command):
  def __init__(self, word):
    self.imagen = "./imagenes/Command/I.jpg"
    self.word = word

  def execute(self):
    self.word.action()
    print("Imprimiendo...")

class Guardar(Command):
  def __init__(self, word):
    self.imagen = "./imagenes/Command/G.jpg"
    self.word = word

  def execute(self):
    self.word.action()
    print("Guardando")

#
# Invoker
# asks the command to carry out the request
#
class Acciones:
  def __init__(self):
      self.imagen = None
      self.command = None  


  def getImagen(self):
    return self.imagen

  
  def set(self, command):
    self.command = command

  def confirm(self):
    if (self.command is not None):
      self.command.execute()


if __name__ == "__main__":
  word = Word()
  command = Abrir(word)
  command = Imprimir(word)

  command = Guardar(word)

  acciones = Acciones()
  acciones.set(command)
  acciones.confirm()
