class Singleton:
   __instance = None
   __imgenes = None

   
   @staticmethod 
   def getInstance():

      if Singleton.__instance == None:
         Singleton()

      return Singleton.__instance
    
   @staticmethod 
   def get_Imagen():

      if Singleton.__instance == None:
          Singleton.__imgenes = "./imagenes/Singleton/S.jpg"

      return  Singleton.__imgenes
    

    
    
   def __init__(self):
      
      if Singleton.__instance != None:
         raise Exception("Esto es windows!")
      else:
         Singleton.__instance = self
         Singleton.__imgenes = "./imagenes/Singleton/S.jpg"

if __name__ == "__main__":         
   s = Singleton()
   #print (s)

   s = Singleton.getInstance()
   #print (s)

   s = Singleton.getInstance()
   #print (s)



