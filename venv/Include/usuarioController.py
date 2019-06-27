import pandas as pd
class controlador:
    dfUsuarios = pd.DataFrame(columns={'Nombre','Apellido'})
    def __init__(self):
        self.dfUsuarios = self.dfUsuarios.append({'Nombre' : 'Bruno' , 'Apellido' : 'Romero'} , ignore_index=True)
        self.dfUsuarios = self.dfUsuarios.append({'Nombre' : 'Sebastian' , 'Apellido' : 'Villa-Garcia'} , ignore_index=True)

    def listarUsuarios(self):
        return self.dfUsuarios.to_json(orient='records')

    def insertarUsuario(self,nombre,apellido):
        dfUsuarios = dfUsuarios.append({'Nombre' : nombre , 'Apellido' : apellido} , ignore_index=True)