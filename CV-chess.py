import cv2
import sys

#init
args = sys.argv
gray = cv2.imread(args[1],cv2.IMREAD_GRAYSCALE)
chess_board_image = cv2.imread(args[1])

#Automativally find chessboard within x and y size
def automode(maxsizex,maxsizey):
 for nx in range(1,maxsizex):
  for ny in range(nx,maxsizey):
   checkno=True
   print("Scanning "+str(nx)+"x"+str(ny)+"....",end='')
   try:
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)    
    if ret == True:
     checkno=False
     print("True!")
     cv2.drawChessboardCorners(chess_board_image, (nx, ny), corners, ret)
     result_name = "img_"+str(nx)+"x"+str(ny)+'.jpg'
     print("Outputing "+result_name+"....")
     cv2.imwrite(result_name, chess_board_image)
   except Exception:
    print(",False")
    pass
   else:
    if(checkno):
     print(",False")

#Manually enter chessboard size
def manualmode(nx,ny):
 ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
 if ret == True:
  cv2.drawChessboardCorners(chess_board_image, (nx, ny), corners, ret)
  result_name = "img_"+str(nx)+"x"+str(ny)+'.jpg'
  print("Found!!....")
  print("Outputing "+result_name+"....")
  cv2.imwrite(result_name, chess_board_image)
 elif(ret==False):
  print("Couldn't fild such size of chessboard....")


#Main from here
if (len(args) != 2):  
 print("이미지 파일의 이름을 주세요...")
 quit() 

#Choose mode
choose=-1
while(choose<0)or(choose>1):
 print("Choose format of output images:")
 print("0: Automode")
 print("1: Manual mode")
 print("choose(0-1):",end='')
 choose=int(input())
 
#Auto mode
if(choose==0):
 print("max range to find chesssboard blocks vertically(x):",end='')
 maxx=int(input())
 print("max range to find chesssboard blocks horizontally(y):",end='')
 maxy=int(input())
 automode(maxx,maxy)
 
#Manual mode
elif(choose==1):
 print("Number of chessboard blocks vertically:",end='')
 chessx=int(input())
 print("Number of chessboard blocks horizontally:",end='')
 chessy=int(input())
 manualmode(chessx,chessy)


