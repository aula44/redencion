############################################
##                                        ##
##     "Redención", herramienta para      ##
##   cambiar el nombre del equipo si se   ##
##      introduce erróneamente en la      ##
##             instalación                ##
##                                        ##
##      Por Héctor Del Pino, para el      ##
##       proyecto IC11 del aula 44.       ##
##                                        ##
############################################

# dependencias
import sys
import ctypes
import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)
from PyQt5.QtCore import Qt

# llamada a win32 para comprobar si tenemos privilegios de administrador
# no es realmente necesaria esta comprobación pues el 99% de casos (ejecución desde menú win + r) no tendremos administrador
def comprobar_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# si no hay administrador (flujo normal y esperado) invocamos al bendito UAC de windows para que nos deje autenticarnos como "Profesorado"
if not comprobar_admin():
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",          
        sys.executable,  
        params,
        None,
        1
    )
    sys.exit(0)

# ventana principal
class RedencionMain(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciar_iu()

    # elementos y layout
    def iniciar_iu(self):
        # titulo y dimensiones de la ventana
        self.setWindowTitle("Redención")
        self.setFixedSize(250, 100)

        # definición de la caja de texto donde introduciremos nuestro nuevo numero de equipo
        self.caja_numeropc = QLineEdit()
        self.caja_numeropc.setFixedHeight(30)
        self.caja_numeropc.setPlaceholderText("Número (el aula no se cambiará)")

        # boton para cambiar el nombre del equipo
        self.boton_cambiarnumero = QPushButton("Cambiar nombre del equipo y fondo")
        self.boton_cambiarnumero.setFixedHeight(36)
        self.boton_cambiarnumero.clicked.connect(self.presionar_cambiarnum)

        # definición de nuestra layout
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(self.caja_numeropc)
        layout.addWidget(self.boton_cambiarnumero)

        # establecer la layout 
        self.setLayout(layout)

    # la lógica detrás del botón de cambiar número de equipo
    def presionar_cambiarnum(self):
        # definir variable del numero nuevo extrayendo el valor que hemos introducido en la caja, quitando espacios y cosas raras (strip)
        numeroNuevo = self.caja_numeropc.text().strip()

        # construir lo que será nuestro nuevo nombre de equipo (PC, nuestro nuevo numero y AULA44)
        nombrePC = "PC" + numeroNuevo + "-AULA44"

        # el comando que cambia el fondo. redirigimos la tarea a un script de powershell que ya está en nuestra carpeta común
        cmd_cambiofondo = (
            r'powershell -ExecutionPolicy Bypass '
            r'-File "C:\IC11\scripts\fondo_assist.ps1"'
        )

        # comando para cambiar el nombre del equipo y posteriormente reiniciar. se ejecuta también en powershell
        cmd_nombreequipo = (
            f'powershell -command "Rename-Computer '
            f'-NewName \'{nombrePC}\' -Force -Restart"'
        )

        # llamada al programa que genera los fondos de pantalla, pasando como argumento numeroNuevo
        os.system(r"C:\IC11\bg.exe " + numeroNuevo)

        # llamada al comando que cambia el fondo
        os.system(cmd_cambiofondo)

        # llamada al comando que cambia el nombre del equipo
        os.system(cmd_nombreequipo)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RedencionMain()
    window.show()
    sys.exit(app.exec_())
