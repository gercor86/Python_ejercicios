class usuario_validar():
    
    errors=[]
    
    def longitud(self, username):
        if len(username) <6:
            self.errors.append('El nombre de usuario debe contener al menos 6 caracteres.')
            return False
    
        elif len(username)>12:
            self.errors.append('El nombre de usuario debe contener un maximo de 12 caracteres.')
            return False
        
        else:
            True

    def alfanumerico(self, username):
        if username.isalnum() == False:
            self.errors.append('El nombre del usuario puede contener solo letrar y numeros.')
            return False
        
        else:
            True
    
    def validar_usuario(self, username):
        valido = self.longitud(username) and self.alfanumerico(username)
        return valido