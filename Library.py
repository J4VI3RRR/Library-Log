
#Library log that reads through a given dataset to output a list of students who owe fines 
#Created by: Javier Strang

#Open txt files
bookread = open("Booklist.txt","r")
logread = open("Librarylog.txt","r")
  

#Loop to put booklist into a 2d list
oldBookList = bookread.readlines()
booklist = []
i = 0
while i < len(oldBookList):
    oldBookList[i] = oldBookList[i].rstrip("\n")
    booklist.append(oldBookList[i].split("#"))
    i += 1


#Loop to put library log into a 2d list
oldLogList = logread.readlines()
loglist = []
k = 0
while k < len(oldLogList):
    oldLogList[k] = oldLogList[k].rstrip("\n")
    loglist.append(oldLogList[k].split("#"))
    k += 1


#Converts the number of copies a book has in booklist.txt from a string to an integer
indcopies = 0
x = 1
while x <= len(booklist):
    copies = int(booklist[0+indcopies][1])
    booklist[0+indcopies][1] = copies
    indcopies += 1
    x += 1


#Converts the day in librarylog.txt from a string to integer
loglist.pop()
inddy = 0
q = 1
while q <= len(loglist):
    dy = int(loglist[0+inddy][1])
    loglist[0+inddy][1] = dy
    inddy += 1
    q += 1



#Loop that finds which notation an input has
l = 1
index1 = 0
finelst = []
while l <= len(loglist):
    #Borrow Notation
    if loglist[0+index1][0] == "B":
        #Converts day returned from string to integer
        re = int(loglist[0+index1][4])
        loglist[0+index1][4] = re

        #Borrowing books/can a student borrow a book loop
        count = 0
        v = 1
        indbname = 0
        while v <= len(booklist):
            #Copy of a book is borrowed from library (-1 copies)
            if loglist[0+index1][3] == booklist[0+indbname][0] and booklist[0+indbname][1] > 0: 
                count = booklist[0+indbname][1]
                count -= 1
                booklist[0+indbname][1] = count
                print("On day", loglist[0+index1][1], loglist[0+index1][2], "borrowed", loglist[0+index1][3])
                
                #After borrowing a book if student takes book for longer than 7 days for restricted book they get fined
                if booklist[0+indbname][2] == "TRUE" and loglist[0+index1][4] > 7:
                    fineday = loglist[0+index1][4]
                    fin = fineday - 7
                    fine = fin * 5
                    #Adds new student to fine list if they haven't been fined before
                    if any(loglist[0+index1][2] in tp for tp in finelst) == False:
                        stuname = loglist[0+index1][2]
                        tmplst = []
                        tmplst.append(stuname)
                        tmplst.append(fine)
                        finelst.append(tmplst)
                        print("On day", loglist[0+index1][1], loglist[0+index1][2], "was fined", fine)

                    #If student has been fined before it adds to their existing balance  
                    else:
                        indfine = 0
                        u = 1
                        while u <= len(finelst):
                            if loglist[0+index1][2] == finelst[0+indfine][0]:
                                prevfine = finelst[0+indfine][1]
                                totalfines = fine + prevfine
                                finelst[0+indfine][1] = totalfines
                                print("On day", loglist[0+index1][1], loglist[0+index1][2], "has a total fine of", finelst[0+index1][1])

                            indfine += 1
                            u += 1
                #After borrowing a book if student takes book for longer than 28 days for unrestricted book they get fined
                elif booklist[0+indbname][2] == "FALSE" and loglist[0+index1][4] > 28:
                    fineday2 = loglist[0+index1][4]
                    fin2 = fineday2 - 28
                    fine2 = fin2 * 1
                    #Adds new student to fine list if they haven't been fined before
                    if any(loglist[0+index1][2] in tp for tp in finelst) == False:
                        stuname = loglist[0+index1][2]
                        tmplst = []
                        tmplst.append(stuname)
                        tmplst.append(fine2)
                        finelst.append(tmplst)
                        print("On day", loglist[0+index1][1], loglist[0+index1][2], "was fined", fine)
                    #If student has been fined before it adds to their existing balance  
                    else:
                        indfine2 = 0
                        t = 1
                        while t <= len(finelst):
                            if loglist[0+index1][2] == finelst[0+indfine2][0]:
                                prevfine2 = finelst[0+indfine2][1]
                                totalfines2 = fine2 + prevfine2
                                finelst[0+indfine2][1] = totalfines
                                print("On day", loglist[0+index1][1], loglist[0+index1][2], "has a total fine of", finelst[0+index1][1])
                            indfine2 += 1
                            t += 1
            v += 1
            indbname += 1

    #Return Notation
    elif loglist[0+index1][0] == "R":
        #Copy of a book is returned
        cout = 0
        m = 1
        indnam = 0
        while m <= len(booklist):
            if loglist[0+index1][3] == booklist[0+indnam][0]:
                cout = booklist[0+indnam][1]
                cout += 1
                booklist[0+indnam][1] = cout
                print("On day", loglist[0+index1][1], loglist[0+index1][2], "returned", loglist[0+index1][3])
            m += 1
            indnam += 1

    #Addition notation - adds book to copies / creates new books
    elif loglist[0+index1][0] == "A":
        #New copy of a book the library already has added
        num = 0
        g = 1
        indname = 0
        while g <= len(booklist):
            if loglist[0+index1][2] == booklist[0+indname][0]:
                num = booklist[0+indname][1]
                num += 1
                booklist[0+indname][1] = num
                print("On day", loglist[0+index1][1], "a copy of" ,loglist[0+index1][2],"was added to the library")
            g += 1
            indname += 1

        #New book in library added
        if any(loglist[0+index1][2] in tmp for tmp in booklist) == False:
            newbook = loglist[0+index1][2]
            newbooklst = []
            newbooklst.append(newbook)
            newbooklst.append(1)
            newbooklst.append("FALSE")
            booklist.append(newbooklst)
            print("On day", loglist[0+index1][1], loglist[0+index1][2], "was added to the library")

    #Fine Pay notation
    elif loglist[0+index1][0] == "P":
        #Student pays fines
        indfine3 = 0
        y = 1
        if any(loglist[0+index1][2] in TMP for TMP in finelst) == True:
            while y <= len(finelst):
                if loglist[0+index1][2] == finelst[0+indfine3][0]:
                    prevfine3 = finelst[0+indfine3][1]
                    payback = int(loglist[0+index1][3])
                    totalfines = prevfine3 - payback
                    finelst[0+indfine3][1] = totalfines
                    print("On day", loglist[0+index1][1], loglist[0+index1][2], "made a payment of $", payback, "for fines")
                indfine3 += 1
                y += 1
    l += 1
    index1 += 1


#Print all pending fines at the library at the end of log
penfine = 1
indpenfine = 0
while penfine <= len(finelst):
    if finelst[0+indpenfine][1] > 0:
        print("\nAll pending library fines")
        print("-------------------------")
        print(finelst[0+indpenfine][0], "had total fines of $", finelst[0+indpenfine][1])
    else:
        print("\nAll pending library fines")
        print("-------------------------")
        print("No pending fines!")
    
    print("\n")
    penfine += 1
    indpenfine += 1
