import time
import winsound


def beep_timer(interval):
    start_time = time.time()
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Alarma detectada a las {current_time}")
        winsound.Beep(500, 500)
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        print(f"Levantate de la silla ya pasaron: {minutes} minutos {seconds} segundos")
        print(
            "---------------------------------------------------------------------------"
        )
        print()
        time.sleep(interval)


if __name__ == "__main__":
    interval_minutes = 50
    interval_seconds = interval_minutes * 60
    print(
        f"Temporizador configurado para lanzar un sonido cada {interval_minutes} minuto(s)."
    )
    try:
        beep_timer(interval_seconds)
    except KeyboardInterrupt:
        print("Temporizador interrumpido manualmente.")
