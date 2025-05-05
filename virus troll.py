import subprocess
import webbrowser
import os
import time
import platform

def open_notepad_and_type(text="vc foi hackeado"):
    """Abre o Notepad e digita o texto especificado."""
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["notepad.exe"])
            time.sleep(1)  # Espera o Notepad abrir
            import pyautogui
            pyautogui.typewrite(text)
        else:
            print("Abertura e digitação no Notepad só são totalmente suportadas no Windows.")
            print("Em outros sistemas, o Notepad será aberto, mas a digitação não será automática.")
            if platform.system() == "Linux":
                subprocess.Popen(["gedit"])
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", "-a", "TextEdit"])
            time.sleep(2) # Espera o editor de texto abrir
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o Notepad: {e}")

def open_browser_and_youtube(music_url="https://www.youtube.com/watch?v=Aq_1z97v994"):
    """Abre o navegador padrão e a URL do YouTube especificada."""
    try:
        webbrowser.open_new_tab("https://www.google.com")
        webbrowser.open_new_tab(music_url)
    except webbrowser.Error as e:
        print(f"Ocorreu um erro ao abrir o navegador: {e}")

def set_volume_100():
    """Define o volume do sistema para 100%."""
    try:
        if platform.system() == "Windows":
            from ctypes import cast, POINTER
            from comtypes import CLSCTX_ALL
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            if volume.GetMute() == 1:
                volume.SetMute(0, None)
            volume.SetMasterVolumeLevelScalar(1.0, None)
            print("Volume definido para 100%.")
        elif platform.system() == "Linux":
            subprocess.run(["amixer", "set", "Master", "100%"])
            print("Volume definido para 100% (via amixer).")
        elif platform.system() == "Darwin":
            subprocess.run(["osascript", "-e", "set volume output volume 100"])
            print("Volume definido para 100% (via osascript).")
        else:
            print(f"A definição de volume para 100% não é suportada neste sistema operacional: {platform.system()}")
    except Exception as e:
        print(f"Ocorreu um erro ao definir o volume: {e}")

if __name__ == "__main__":
    open_notepad_and_type()
    open_browser_and_youtube()
    set_volume_100()