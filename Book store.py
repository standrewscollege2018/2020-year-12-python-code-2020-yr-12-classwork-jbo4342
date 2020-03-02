titles = [["Harry Potter", "J.K. Rowling", "$12.99"], ["Captain Underpants", "Dave Pilkey", "$7.99"], ["Percy Jackson", "Rick Riordan", "$11.99"], ["Hunger Games", "Suzanne Collins", "$12.99"], ["Maze Runnner", "James Dashner", "$9.99"]]
print("Welcome to Josh's Book Catolouge")


ask = True
while ask == True:
    task = input("what would you like to do? \na) Add a new book \nb) Edit a book name \nc) Delete an existing book \nd) Preview List \nAnswer:")
    if task == "a":
        new_book = input("What is the title of the book you want add?")
        new_author = input("What is the name of the author?")
        new_price = input("What is the price?")
        new_title = []
        new_title.append(new_book)
        new_title.append(new_author)
        new_title.append(new_price)
        titles.append(new_title)
        question = input("Thank you, the catologue has been updated, would you like to go back to the menu?")
        if question == "Yes" or "yes":
            ask = True
        else:
            break
            

    elif task == "b":
        number = 0
        value = 1
        loop = True
        while loop == True:
            lenoflist = len(titles)
            if number == lenoflist:
                loop = False
            else:
                print(value, ":", titles[number][0])
                number+= 1
                value+= 1
        book_edit = int(input("What book would you like to edit? (please enter the number of the book)"))
        book_edit-= 1
        new_name = input("What would you like to rename the book?")
        titles[book_edit][0] = new_name
        question = input("Succsess! Title Updated, would you like to go back to the menu")
        if question == "Yes" or "yes":
            ask = True
        else:
            print("ok, cya later!")
            break
                
    elif task == "c":
        cnumber = 0
        cvalue = 1
        cloop = True
        while cloop == True:
            lenoflist = len(titles)
            if cnumber == lenoflist:
                break
            else:
                print(cvalue, ":", titles[cnumber][0])
                cnumber+= 1
                cvalue+= 1
                            
        cdelete = int(input("What title would you like to delete (Please select by number)"))
        titles.pop[cdelete]                                    
        
        
    elif task == "d":
        number2 = 0
        listcount = 0
        title_number = 1
        preview = True
        while preview == True:
            if number2 == len(titles):
                break
            
            else:
                print("Title", title_number, "\nBook:", titles[listcount][0], "\nAuthor:", titles[listcount][1], "\nPrice:", titles[listcount][2])
                print(" ")
                number2+= 1 
                listcount+= 1
                title_number+= 1