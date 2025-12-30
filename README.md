# 🩹 Redención | IC11
<img src="https://github.com/user-attachments/assets/883a812c-6cd3-4bcd-9389-7cb66df52cb4" width="100%" />

## ℹ️ Info
Pequeño script con GUI que viene incluido en las ISO de IC11 usadas en el aula 44. 

Permite cambiar el numero asignado al equipo y, consecuentemente, el fondo de pantalla del equipo, algo que antes no se podía hacer, pues al configurar el equipo el número se quedaba establecido permanentemente siendo el formateo la única forma de cambiarlo.

## 🚧 Build
```bash
git clone https://github.com/aula44/redencion.git
cd redencion
pip install pyinstaller
pip install -r requirements.txt
pyinstaller --onefile --noconsole --uac-admin main.py
```


