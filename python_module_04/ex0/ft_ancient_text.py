#! /usr/bin/env python3

def main() -> None:
    print(' === ARCHIVOS CIBERNÉTICOS - SISTEMA DE RECUPERACIÓN DE DATOS ==='
          '\n')
    archive = None
    try:
        archive = open('../data-generator-tools/ancient_fragment.txt', 'r')
        print(f'Accediendo al almacén de datos: {archive.name.split('/')[-1]}'
              '\n')
        print('Conexión establecida...\n')
        print('Datos recuperados:')
        print(archive.read())
    except FileNotFoundError:
        print('Error: Almacén de almacenamiento no encontrado')
    finally:
        if archive:
            archive.close()
            print('\nRecuperación de datos completa.'
                  ' Unidad de almacenamiento desconectada.')


if __name__ == '__main__':
    main()
