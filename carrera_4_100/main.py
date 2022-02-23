from threading import Thread, Semaphore


class Testigo:
    def __init__(self):
        semaforo = Semaphore(1)
        # Crear variable semáforo

    # private Semaphore sem_testigo= new Semaphore(1);
    # public void tomarTestigo(){
    #     try {
    #         sem_testigo.acquire();
    #     } catch (InterruptedException e) {
    #         e.printStackTrace();
    #     }
    # }
    # public void soltarTestigo(){
    #     sem_testigo.release();
    # }


class Atleta:
    def __init__(
        self,
        nombre: str,
        testigo: Testigo,
    ):
        self.nombre = nombre
        self.testigo = testigo

    # public void run(){
    #     elTestigo.tomarTestigo();
    #     System.out.println(this.nombre+" comienza a correr");
    #     try {
    #         Thread.sleep((int)(Math.random()*(11-8)+9)*1000);
    #     } catch (InterruptedException e) {
    #         e.printStackTrace();
    #     }
    #     System.out.println(this.nombre+ " termino la carrera");
    #     elTestigo.soltarTestigo();
    # }
