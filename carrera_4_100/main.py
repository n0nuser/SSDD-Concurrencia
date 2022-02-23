from threading import Thread, Semaphore, Timer
import time
import random


class Testigo:
    def __init__(self):
        self.semaforo = Semaphore(1)

    def get(self):
        self.semaforo.acquire()

    def drop(self):
        self.semaforo.release()


class Atleta:
    def __init__(
        self,
        nombre: str,
        testigo: Testigo,
    ):
        self.nombre = nombre
        self.testigo = testigo

    def stop_race(self, tiempo_carrera):
        print(self.nombre, "termina la carrera en", tiempo_carrera, "segundos.")
        self.testigo.drop()

    def start_race(self):
        self.testigo.get()
        print(self.nombre, "inicia la carrera.")
        tiempo_carrera = random.choice(range(9, 12))
        time.sleep(tiempo_carrera)
        self.stop_race(tiempo_carrera=tiempo_carrera)

    def run(self):
        t = Thread(target=self.start_race)
        t.start()
        t.join()


def main():
    testigo = Testigo()
    atletas = [
        Atleta("Darwin Echevarry", testigo),
        Atleta("Carl Lewis", testigo),
        Atleta("Usain Bolt", testigo),
        Atleta("Asafa Powell", testigo),
    ]

    for index, atleta in enumerate(atletas):
        atleta.run()


if __name__ == "__main__":
    main()
