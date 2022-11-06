from contextlib import contextmanager

import cm_decor

estack = cm_decor.Decorator('estack')


@contextmanager
def cm():
    print('__enter__')
    yield


@estack
def f(*, estack):
    estack.enter_context(cm())
    return 1


if __name__ == '__main__':
    print(f())