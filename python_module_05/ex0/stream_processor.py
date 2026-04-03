#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f'Salida: {result}'


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print('Inicializando Procesador Numérico...')
        print(f'Procesando datos: {data}')
        try:
            if not self.validate(data):
                raise ValueError
            print('Validación: Datos numéricos verificados')
            size, total = 0, 0
            for i in data:
                size += 1
                total += i
            media = total / size
            return self.format_output(
                f'Procesados {size} valores numéricos, '
                f'suma={total}, promedio={media:.2f}')
        except Exception:
            return self.format_output(
                '[ALERTA] '
                'Los datos no son numéricos o no están separados con '','' ')

    def validate(self, data: Any) -> bool:
        if data.__class__ == list:
            for i in data:
                if i.__class__ != int and i.__class__ != float:
                    return False
            return True
        return False


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print('Inicializando Procesador de Texto...')
        print(f'''Procesando datos: '{data}' ''')
        try:
            if not self.validate(data):
                raise ValueError
            print('Validación: Datos de texto verificados')
            letters, word, flag = 0, 0, 0
            for i in data:
                letters += 1
                if i != ' ' and flag != 1:
                    word += 1
                    flag = 1
                if i == ' ':
                    flag = 0
            return self.format_output(
                f'Texto procesado: {letters} caracteres, {word} palabras')

        except Exception:
            return self.format_output(
                '[ALERTA] No es de tipo alfanumérico')

    def validate(self, data: Any) -> bool:
        if data.__class__ == str:
            return True
        return False


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print('Inicializando Procesador de Registros...')
        print(f'Procesando datos: {data}')
        try:
            if not self.validate(data):
                raise ValueError
            print('Validación: Entrada de registro verificada')
            pos = 0
            type_log, mensaje = '', ''
            for i in data:
                if i == ':':
                    type_log = data[:pos]
                    mensaje = data[pos + 2:]
                    break
                pos += 1
            if type_log == 'ERROR':
                return self.format_output(
                    f'[ALERTA] Nivel {type_log} detectado: {mensaje}')
            return self.format_output(
                f'Nivel {type_log} detectado: {mensaje}')

        except Exception:
            return self.format_output(
                '[ALERTA] Datos introducidos no son de tipo Log: '
                'OK, INFO.. or ERROR: MENSAJE')

    def validate(self, data: Any) -> bool:
        if data.__class__ == str:
            for i in data:
                if i == ':':
                    return True
        return False


def main() -> None:
    print('=== CODE NEXUS - FUNDACIÓN DEL PROCESADOR DE DATOS ===\n')

    numeric = NumericProcessor()
    print(numeric.process([1, 2, 3, 'a', 5]), '\n')
    print(numeric.process([1, 2, 3, 4, 5]), '\n')

    phrase = TextProcessor()
    print(phrase.process(False), '\n')
    print(phrase.process('Hola corrector de 42 Madrid'), '\n')

    log = LogProcessor()
    print(log.process('ERROR: Connection timeout'), '\n')
    print(log.process('INFO: System ready'), '\n')
    print(log.process(123), '\n')

    print('\n=== Demostración de Procesamiento Polimórfico ===')
    print('Procesando múltiples tipos de datos '
          'a través de la misma interfaz...\n')

    processors = [
                  (NumericProcessor(), [1, 2, 3]),
                  (TextProcessor(), 'Hello World'),
                  (LogProcessor(), 'INFO: System ready')
                 ]
    count = 0
    for processor, data in processors:
        count += 1
        print(f'***************Resultado {count}***************')
        print(f'{processor.process(data)}\n')

    print('\nSistemas base en línea. '
          'Nexus listo para transmisiones avanzadas.')


if __name__ == '__main__':
    main()
