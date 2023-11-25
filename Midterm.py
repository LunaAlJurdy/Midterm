def openTab():#o(n+n)=o(n), n being the length of the list
  print("please choose a Title")
  title=str(input())
  for i in range(len(list)):#o(n)
    if title in list:
     print("the title you chose is present: ",title)

    else:
      print("the title you chose is added: ",title)
  print("please choose a link")
  link=str(input())
  
  for i in range(len(tab)):#o(n)
    if link in tab:
      print("the link you chose is present: ",link)

def closeTab():
  print("Enter the index of the tab you would like to close")
  index=int(input())
  if index in range (len(list)):
    list.pop(index)
  else:
    print("Invalid input")
    list.pop()
  print(list)
def switchTab():
  print("Enter the index of the tab you would like to switch to")
  index=int(input())
  if index in range(len(list)):
    print("Switching to tab: ",list[index])
    print(tab[list[index]])
  else:
    print("Invalid input")
    print("Switching to tab: ",list[-1])
    print(tab[list[-1]])
  return index
def displayTab():
  print("The tabs are: ")
  print(list)
  print(tab)
  return list

def nestedTab():
  #watched some youtube videos and kept on trying to solve this problem
  print("Enter the index of the tab you want to insert additional tabs to")
  index=int(input())
  content=input("Enter the content of the new tab: ")
  title=input("Enter the title you would like to add: ")
  if index in range(len(list)):
    print(title+tab[list[index]]+content)
  else:
    print("Invalid index")

def insertionSort(list): #o(n^2)
  border=1
  while border<len(list): #o(n)
    current=border
    while current>0 and list[current-1].lower()>list[current].lower(): #o(n)
      list[current],list[current-1]=list[current-1],list[current]
      current-=1
    border+=1
  print(list)
list=["Replit","Github","Stack Overflow","W3Schools"]
insertionSort(list)
def saveTab():
  import json
  tab={"Replit":"https://replit.com/", "Github":"https://github.com/", "Stack Overflow":"https://stackoverflow.com/","W3Schools":"https://www.w3schools.com/"}
  y=json.dumps(tab) 
  print(y)
  return (y)

def importTab():
  with open("tab.json","w") as file:
    file.write("This is my FCS midterm")
  with open("tab.json","r") as file:
    print(file.read())
def mainMenu():
  choice=-99 # dummy value
  while choice !=9:
    print("Welcome")
    print("Enter")
    print("1. to open tab")
    print("2. to close tab")
    print("3. to switch tab")
    print("4. to display all tabs")
    print("5. to open nested tab")
    print("6. to sort all tabs")
    print("7. to save tabs")
    print("8. to import tabs")
    print("9. to exit")
    
    choice=int(input())

    if choice==1:
      openTab()
    elif choice==2:
      closeTab()
    elif choice==3:
      switchTab()
    elif choice==4:
      displayTab()
    elif choice==5:
      nestedTab()
    elif choice==6:
      sortTab()
    elif choice==7:
      saveTab()
    elif choice==8:
      importTab()
    elif choice ==9:
      print("bye bye")
    else:
      print("ivalid input")

mainMenu()

