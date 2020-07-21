def display_board(board):
#
# Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# i wyświetla go w oknie konsoli.
#    
    for rows in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for field in rows:
            print("|  ",field, "  ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    nr = int(input("Podaj numer wolnego pola (1-9):"))
    if nr > 0 and nr < 10:
        row = (nr-1) // 3
        col = (nr-1) % 3
        board[row][col] = "o"
    else:
        print("Błędne dane!!!"
#
# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu, 
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
#

def make_list_of_free_fields(board):
    free_fields = []
    
#
# Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól; 
# lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
#

def victory_for(board, sign):
    a=1
#
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#

def draw_move(board):
    a=1
#
# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
#

board = [[1,2,3],[4,"x",6],[7,8,9]]
display_board(board)
enter_move(board)
display_board(board)
