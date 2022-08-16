import functions

def main():
    val = input("Ingrese de que quiere ver el top 10: ")
    if val=='tweets':
        general_function('retweetCount')
    elif val=='usuarios':
        general_function('user')
    elif val=='dias':
        general_function('days')
    elif val=='hashtags':
        general_function('hashtag')