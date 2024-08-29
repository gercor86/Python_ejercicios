import usuario as uv
import password as pv

user_validator = uv.usuario_validar()
password_validator = pv.password_validar()

correcto = False

while correcto == False:
    
    nombre = input('Ingrese su nombre de usuario: ')
    
    if not user_validator.validar_usuario(nombre):
        for error in user_validator.errors:
            print(error)
            correcto = False
            user_validator.errors.remove(error)
        
        else:
            correcto = True

    while correcto == True:
        passw = input('Ingrese su contraseña: ')
        
        if not password_validator.validar_password(passw):
            for error in password_validator.errors:
                print(error)
                correcto == True
                password_validator.errors.remove(error)
        
        else:
            correcto = False