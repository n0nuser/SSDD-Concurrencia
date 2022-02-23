from threading import Thread, Semaphore, Timer
import time
import random


class Testigo:
    """Crea un semáforo.
    · get(): Coge el testigo
    · drop(): Suelta el testigo
    """

    def __init__(self):
        """Crea el semáforo al instanciar la clase."""
        self.semaforo = Semaphore(1)

    def get(self):
        """Decrementa el contador del semáforo, bloqueando su uso por otros hilos."""
        self.semaforo.acquire()

    def drop(self):
        """Incrementa el contador del semáforo, liberando su uso para otros hilos."""
        self.semaforo.release()


class Atleta:
    def __init__(
        self,
        nombre: str,
        testigo: Testigo,
    ):
        self.nombre = nombre
        self.testigo = testigo

    def start_race(self):
        """Coge el testigo, empieza la carrera, la termina y suelta el testigo."""
        self.testigo.get()
        print(self.nombre, "inicia la carrera.")
        tiempo_carrera = random.choice(range(9, 12))
        time.sleep(tiempo_carrera)
        print(self.nombre, "termina la carrera en", tiempo_carrera, "segundos.")
        self.testigo.drop()

    def run(self):
        """Método para crear el hilo y ejecutar el método start_race()."""
        t = Thread(target=self.start_race)
        t.start()
        t.join()


def main():
    """Se crea un testigo y se presenta a los atletas. Corre uno detrás del otro cogiéndose y pasándose el testigo.
    En realidad, se ejecuta un hilo que bloquea el semáforo y cuando termina lo libera, permitiendo que otro hilo lo coja.
    """
    testigo = Testigo()
    atletas = [
        Atleta("Darwin Echevarry", testigo),
        Atleta("Carl Lewis", testigo),
        Atleta("Usain Bolt", testigo),
        Atleta("Asafa Powell", testigo),
    ]

    for atleta in atletas:
        atleta.run()


if __name__ == "__main__":
    main()
