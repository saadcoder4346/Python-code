a=[0,0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0,0,0,0]
def board():
      zero="x" if a[0] else('o' if b[0] else 0)
      one="x" if a[1] else('o' if b[1] else 1)
      two="x" if a[2] else('o' if b[2] else 2)
      three="x" if a[3] else('o' if b[3] else 3)
      four="x" if a[4] else('o' if b[4] else 4)
      five="x" if a[5] else('o' if b[5] else 5)
      six="x" if a[6] else('o' if b[6] else 6)
      seven="x" if a[7] else('o' if b[7] else 7)
      eight="x" if a[8] else('o' if b[8] else 8)
      print(f" {zero} | {one} | {two} ")
      print(f"-----------")
      print(f" {three} | {four} | {five} ")
      print(f"-----------")
      print(f" {six} | {seven} | {eight} ") 



def winner(a,b):
  wins=[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
  for win in wins:
    if a[win[0]] + a[win[1]] + a[win[2]] == 3:
            return "x won"
    elif b[win[0]] + b[win[1]] + b[win[2]] == 3:
            return "o won"
  
  if all(a[i] != 0 for i in range(1, 10)) and all(b[i] != 0 for i in range(1, 10)):
        return "tie"
  return None
    

turn=1
while True:
    board() 

    if turn ==1:
        try:
         print("x turn")
         place=int(input("where do u want to place x:"))
         if place>8 or place<0:
             print("invalid input")
             continue
         
         elif a[place] or b[place]:
            print("Position already occupied. Choose another position.")
            continue
         a[place]=1
        except ValueError:
            print("invalid input")
            continue



        
        
    else:
        try:
         print("o turn")
         place=int(input("where do u want to place o:"))
         if a[place] or b[place]:
            print("Position already occupied. Choose another position.")
            continue 
         elif place>8 or place<0:
             print("invalid input")
             continue
         b[place]=1
        except ValueError:
            print("invalid input")
            continue   
        
    
    



    win = winner(a, b)
    if win:
        board()
        print(win)
        print("Match end")
        break
    turn=1-turn
    
    
       

        
    