import re


def guess_genres(words:int)->list[str]:
 
    if words < 100 : genres = ['микро разказ', 'хайку', 'стих']
    elif words < 1000 : genres = ['флашфикшън', 'стихотворение']
    elif words < 7500 : genres = ['разказ', 'приказка', 'епос']
    elif words < 17000 : genres = ['повест']
    elif words < 40000 : genres = ['новела']
    else : genres = ['роман']
    
 
    return genres
