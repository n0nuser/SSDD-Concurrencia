from carrera_100.main import main as carrera_100
from carrera_4_100.main import main as carrera_4_100


def main():
    print(
        """\
┌───────────────────────────────────┐
 EJECUCIÓN CARRERA DE RELEVOS 4X100 
└───────────────────────────────────┘
    """
    )
    carrera_4_100()
    print(
        """\n\n\
┌───────────────────────────────────┐
 EJECUCIÓN CARRERA 100 METROS LISOS 
└───────────────────────────────────┘
    """
    )
    carrera_100()


if __name__ == "__main__":
    main()
