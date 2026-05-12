import time
import os
import platform
import sys


def shutdown():
    sistema = platform.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 1")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("sudo shutdown -h now")  # Note: Linux/Mac often requires sudo
        else:
            print("\nSistema operacional não reconhecido.")
    except Exception as e:
        print(f"\nErro ao tentar o shutdown: {e}")


def temporizador_com_shutdown():
    print("=== Temporizador com Shutdown ===")

    try:
        segundos = int(input("Digite o tempo em segundos: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    while segundos > 0:
        mins, secs = divmod(segundos, 60)
        timer = f"{mins:02d}:{secs:02d}"

        # Audio cue for the final 10 seconds
        bip = "\a" if segundos <= 10 else ""

        # \r brings the cursor to the start of the line to overwrite it
        print(f"\rTempo restante: {timer} {bip}", end="")
        sys.stdout.flush()

        time.sleep(1)
        segundos -= 1

    print("\n\nIniciando desligamento...")
    shutdown()


if __name__ == "__main__":
    temporizador_com_shutdown()