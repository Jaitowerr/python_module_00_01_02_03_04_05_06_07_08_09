#! /usr/bin/env python3

def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS - SISTEMA DE PRESERVACIÓN ===')
    archive = None
    try:
        archive = open('../data-generator-tools/new_discovery.txt', 'w')
        print('Inicializando nueva unidad de almacenamiento: '
              f'{archive.name.split('/')[-1]}')
        if archive:
            print('Unidad de almacenamiento creada con éxito...\n')
        print('Escribiendo datos de entrada...')
        entry_one = '[ENTRY 001] New quantum algorithm discovered\n'
        entry_two = '[ENTRY 002] Efficiency increased by 347%\n'
        entry_three = '[ENTRY 003] Archived by Data Archivist trainee'
        archive.write(entry_one + entry_two + entry_three)
        print(entry_one + entry_two + entry_three)
    except (FileNotFoundError, PermissionError):
        print('Error: No se ha podido crear el archivo, la ruta está mal '
              'o no tienes permisos para crear un archivo en la carpeta')
    finally:
        if archive:
            archive.close()
            print('\nInscripción de datos completa. '
                  'Unidad de almacenamiento sellada\n'
                  f'Archivo: {archive.name.split('/')[-1]} '
                  'listo para preservación a largo plazo.')


if __name__ == '__main__':
    main()
