from threading import Thread, Condition, Lock
from time import sleep
from random import choice


class Shot:
    """Clase manejadora de los hilos. Define las funciones para la gestión de la concurrencia y notificación a los demás hilos."""

    def __init__(self):
        """ """
        self._cond = Condition(Lock())
        self._flag = False

    def is_set(self):
        """Devuelve el valor de la flag.

        Returns:
            flag (bool): Condición de espera.
        """
        return self._flag

    def wait(self, timeout=None):
        """Si el flag es falso, espera a que sea notificado.

        Args:
            timeout (int, optional): Tiempo a esperar máximo. Por defecto es: None.

        Returns:
            flag (bool): Se devuelve si es verdadero (no está esperando).
        """
        self._cond.acquire()
        try:
            signaled = self._flag
            if not signaled:
                signaled = self._cond.wait(timeout)
            return signaled
        finally:
            pass
            self._cond.release()

    def notify(self):
        """Habilita la flag a verdadero y lo notifica. Dejando así los hilos que estuvieran bloqueados ejecutar sus funciones."""
        self._cond.acquire()
        try:
            self._flag = True
            self._cond.notify_all()
        finally:
            pass
            self._cond.release()


class Atleta(Thread):
    """Clase del atleta, hereda de la clase Thread."""

    def __init__(
        self,
        dorsal: str,
        shot: Shot,
    ):
        self.dorsal = dorsal
        self.shot = shot
        Thread.__init__(self)

    def start_race(self):
        """Espera un tiempo entre 9 y 11 segundos y lo imprime por pantalla."""
        tiempo_carrera = choice(range(9, 12))
        sleep(tiempo_carrera)
        print(
            "El atleta con el dorsal",
            self.dorsal,
            "llega en",
            tiempo_carrera,
            "segundos.",
        )

    def run(self):
        """Método que sobrescribe al propio de la clase Thread.
        Realiza el bloqueo hasta recibir la notificación, entonces ejecuta ciertas funciones.
        """
        self.shot.wait()
        self.start_race()


def main():
    """Se instancian los Atletas (que en realidad son hilos), se ejecutan los hilos y estos quedan a la espera.
    Se imprimen mensajes de preparación para los atletas y los notifica, por lo que realizan su función, correr hasta la meta.
    """
    pumpum = Shot()
    atletas = [
        Atleta("101", pumpum),
        Atleta("102", pumpum),
        Atleta("103", pumpum),
        Atleta("104", pumpum),
        Atleta("105", pumpum),
        Atleta("106", pumpum),
        Atleta("107", pumpum),
        Atleta("108", pumpum),
    ]

    for atleta in atletas:
        atleta.start()

    print("Preparados...")
    sleep(1)
    print("Listos...")
    sleep(1)
    print("¡¡¡Ya!!!")
    pumpum.notify()


if __name__ == "__main__":
    main()
