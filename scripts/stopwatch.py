import time


def stopwatch():
    print("Секундомер запущен!")
    print("Нажмите Enter, чтобы остановить...")

    start_time = time.time()

    input()

    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Прошло времени: {elapsed_time:.2f} секунд!")

stopwatch()