from contextlib import contextmanager

from cm_decor import exitstack


@contextmanager
def cm():
    print('__enter__')
    yield


@exitstack('estack')
def f(*, estack):
    estack.enter_context(cm())
    return 1


if __name__ == '__main__':
    print(f())