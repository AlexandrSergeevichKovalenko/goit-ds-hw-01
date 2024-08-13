from contextlib import contextmanager
from functions_block import *

#creating a context manager 
@contextmanager
def record_manager():
    book = load_data()
    try:
        yield book
    finally:
        save_data(book)
