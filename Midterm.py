list=["Replit","Github","Stack Overflow","W3Schools"]
tab={}
tab["Replit"]="https://replit.com/"
tab["Github"]="https://github.com/"
tab["Stack Overflow"]="https://stackoverflow.com/"
tab["W3Schools"]="https://www.w3schools.com/"
print(tab)
print(list)
def openTab():
  print("please choose a Title")
  title=str(input())
  for i in range(len(list)):
    if title in list:
     print("the title you chose is present: ",title)

    else:
      print("the title you chose is added: ",title)
  print("please choose a link")
  link=str(input())
  
  for i in range(len(tab)):
    if link in tab:
      print("the link you chose is present: ",link)

    else:
      print("the link you chose is added: ",link)
  
      list.append(title)
    
      return title

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
  print("Enter the index of the tab you want to insert additional tabs to")
  index=int(input())
  content=input("Enter the content of the new tab: ")
  title=input("Enter the title you would like to add: ")
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

