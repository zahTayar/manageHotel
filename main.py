import os
import tkinter as tk
from tkinter import ttk


class Hotel():
    def __init__(self, numberOfNR, numberOfPR, numberOfRB, numberOfSR, name):
        self.roomDic = {}
        self.managerName = name
        self.numberOfNR = numberOfNR
        self.numberOfPR = numberOfPR
        self.numberOfRB = numberOfRB
        self.numberOfSR = numberOfSR
        self.totalRooms = numberOfNR + numberOfPR + numberOfSR + numberOfRB

    def buildHotel(self, sNR, sRP, sRB, sS, nNR, nRP, nRB, nS, pNR, pRP, pRB,
                   pS):  ## build all kind of room and hold dictionary of rooms
        for i in range(self.numberOfNR):
            self.roomDic[i + 1] = normalRoom(sNR, nNR, None, pNR, i + 1)

        for i in range(self.numberOfPR):
            self.roomDic[i + self.numberOfNR + 1] = poolVRoom(sRP, nRP, None, pRP, (i + self.numberOfNR + 1))

        for i in range(self.numberOfRB):
            self.roomDic[i + self.numberOfNR + self.numberOfPR + 1] = roomBalcony(sRB, nRB, None, pRB, (
                    i + self.numberOfNR + self.numberOfPR + 1))

        for i in range(self.numberOfSR):
            self.roomDic[i + self.numberOfNR + self.numberOfPR + self.numberOfRB + 1] = SuiteR(sS, nS, None, pS, (
                    i + self.numberOfNR + self.numberOfPR + self.numberOfRB + 1))

    def setCheckOut(self):
        pass

    def getClientsDetails(self):
        pass


class Room:
    def __init__(self, size, numOfb, details, price, roomNum):
        self.isAvl = True
        self.roomNumber = roomNum
        self.price = price
        self.details = details
        self.roomSize = size
        self.numOfB = numOfb


class normalRoom(Room):
    def __init__(self, size, numOfB, details, price, roomNum):
        super().__init__(size, numOfB, details, price, roomNum)


class roomBalcony(Room):
    def __init__(self, size, numOfB, details, price, roomNum):
        super().__init__(size, numOfB, details, price, roomNum)


class poolVRoom(Room):
    def __init__(self, size, numofb, details, price, roomNum):
        super().__init__(size, numofb, details, price, roomNum)


class SuiteR(Room):
    def __init__(self, size, numofb, details, price, roomNum):
        super().__init__(size, numofb, details, price, roomNum)


class Details():
    def __init__(self, familyName, numberOfPe, phoneNumber):
        self.phoneNumber = phoneNumber
        self.family = familyName
        self.numberOf = numberOfPe


# check all the files in the folder if there is something with the word
# hotel !!
def checkIfThereIsHotels(folderName):
    liAllFil = []
    for fileName in os.listdir(folderName):
        if "hotel" in fileName:
            liAllFil.append(fileName)
    return liAllFil


def checkValidInput(inp, kind):
    if isinstance(inp, kind):
        return True
    return False


def main():
    while (True):
        startScreen()


def payBut(price):
    win3 = tk.Tk()
    win3.geometry("500x300")
    tk.Label(win3, text="pay window", font="times 20 bold").place(x=100, y=10)
    tk.Label(win3, text="enter credit card", font="times 10 bold").place(x=20, y=80)
    e1 = tk.Entry(win3).place(x=40, y=120)
    e2 = tk.Entry(win3).place(x=100, y=120)
    e3 = tk.Entry(win3).place(x=160, y=120)
    e4 = tk.Entry(win3).place(x=220, y=120)
    # link to the bank to pay for the room
    win3.mainloop()


def clear(eFamNam, ePhoneNum, eRoomKind, eAmount, res, priceL):
    res.destroy()
    priceL.destroy()
    eFamNam.delete(0, 'end')
    ePhoneNum.delete(0, 'end')
    eRoomKind.delete(0, 'end')
    eAmount.delete(0, 'end')


def donothing():
    pass


def CheckInScreen(tab, myhotel, eRoomKind, ePhoneNum, eFamNam, eAmount):
    fullFlag = False
    labelFlag = False
    room = None
    priceL = tk.Label(tab, text=(0))
    priceL.grid(column=1, row=4, padx=10, pady=10)
    if not (checkValidInput(eRoomKind.get(), str) or checkValidInput(ePhoneNum.get(), int) or checkValidInput(
            eFamNam.get(), str) or checkValidInput(eAmount.get(), int)):
        res = tk.Label(tab, text="Input varibles not good")
        res.grid(column=1, row=5, padx=10, pady=10)
        labelFlag = True

    if eRoomKind.get() == "N" and myhotel.numberOfNR > 0:

        for i in range(myhotel.numberOfNR):
            if (myhotel.roomDic[i + 1]).isAvl:
                (myhotel.roomDic[i + 1]).details = Details(eFamNam, ePhoneNum, eAmount)
                room = myhotel.roomDic[i + 1]
                if labelFlag:
                    res.destroy()
                res = tk.Label(tab, text="success check in room number: " + str(room.roomNumber))
                res.grid(column=1, row=5, padx=10, pady=10)
                room.isAvl = False
                labelFlag = True
            else:
                fullFlag = True

    elif eRoomKind.get() == "P" and myhotel.numberOfPR > 0:
        i = myhotel.numberOfNR

        for i in range(myhotel.numberOfNR + myhotel.numberOfPR):
            if (myhotel.roomDic[i + 1]).isAvl:
                (myhotel.roomDic[i + 1]).details = Details(eFamNam, ePhoneNum, eAmount)
                room = myhotel.roomDic[i + 1]
                if labelFlag:
                    res.destroy()
                res = tk.Label(tab, text="success check in room number: " + str(room.roomNumber))
                res.grid(column=1, row=5, padx=10, pady=10)
                room.isAvl = False
                labelFlag = True
            else:
                fullFlag = True

    elif eRoomKind.get() == "B" and myhotel.numberOfBR > 0:
        i = (myhotel.numberOfNR + myhotel.numberOfPR)
        for i in range(myhotel.numberOfNR + myhotel.numberOfPR + myhotel.numberOfRB):
            if (myhotel.roomDic[i + 1]).isAvl:
                (myhotel.roomDic[i + 1]).details = Details(eFamNam, ePhoneNum, eAmount)
                room = myhotel.roomDic[i + 1]
                if labelFlag:
                    res.destroy()
                res = tk.Label(tab, text="success check in room number: " + str(room.roomNumber))
                res.grid(column=1, row=5, padx=10, pady=10)
                room.isAvl = False
                labelFlag = True
            else:
                fullFlag = True

    elif eRoomKind.get() == "S" and myhotel.numberOfSR > 0:
        i = myhotel.numberOfNR + myhotel.numberOfPR + myhotel.numberOfRB
        for i in range(myhotel.numberOfNR + myhotel.numberOfPR + myhotel.numberOfSR):
            if (myhotel.roomDic[i + 1]).isAvl:
                (myhotel.roomDic[i + 1]).details = Details(eFamNam, ePhoneNum, eAmount)
                room = myhotel.roomDic[i + 1]
                if labelFlag:
                    res.destroy()
                res = tk.Label(tab, text="success check in room number: " + str(room.roomNumber))
                res.grid(column=1, row=5, padx=10, pady=10)
                room.isAvl = False
                labelFlag = True
            else:
                fullFlag = True

    if room is not None:
        priceL.destroy()
        priceL = tk.Label(tab, text=(room.price * int(eAmount.get())))
        priceL.grid(column=1, row=4, padx=10, pady=10)


    else:
        if labelFlag:
            res.destroy()
        res = tk.Label(tab, text="something went wrong")
        res.grid(column=1, row=5, padx=10, pady=10)

    if fullFlag:
        if labelFlag:
            res.destroy()
        res = tk.Label(tab, text="full capacity for " + eRoomKind.get() + " room")
        res.grid(column=1, row=5, padx=10, pady=10)

    bt2 = ttk.Button(tab, text="Clear", width=20,
                     command=lambda: clear(eFamNam, ePhoneNum, eRoomKind, eAmount, res, priceL))
    bt2.grid(column=0, row=7, padx=10, pady=10)
    btPay = ttk.Button(tab, text="pay", width=20, command=
    lambda: payBut(room.price * int(eAmount.get())) if room is not None else donothing())
    btPay.grid(column=2, row=4, padx=10, pady=10)


def CheckOutScreen():
    pass


def Checkavai():
    pass


def search():
    pass


def summary():
    pass


def detalis():
    pass


def exitPro():
    exit(0)


def loadHotel():
    pass


# ,enum.get(),enum1.get(),enum2.get(),enum3
def create(myHote, NR, RP, RB, S, Name, sizeRP, sizeRB, sizeS, sizeNR, numRP, numRB, numS, numNR, priceRP, priceRB,
           priceS, priceNR):
    myHote = Hotel(NR, RP, RB, S, Name)
    myHote.buildHotel(sizeNR, sizeRP, sizeRB, sizeS, numNR, numRP, numRB, numS, priceNR, priceRP, priceRB, priceS)
    return myHote


def buttonpress(win, function, *args):
    win.destroy()
    myhotel = function(*args)

    menuScreen(myhotel)


def creatHotel():
    win2 = tk.Tk()

    validInput = False
    validSize = False
    validPrice = False
    validNum = False

    win2.geometry("500x500")
    win2.config(bg="light blue")
    labelT = tk.Label(win2, text="Create Hotel", font="times 28")
    labelT.place(x=150, y=30)

    labelNR = tk.Label(win2, text="Normal rooms: ", font="times 10")
    labelNR.place(x=20, y=90)
    eNR = tk.Entry(win2)
    eNR.place(x=140, y=90)
    eNR.insert(0, 0)

    labelRP = tk.Label(win2, text="Rooms with Pool: ", font="times 10")
    labelRP.place(x=20, y=110)
    eRP = tk.Entry(win2)
    eRP.place(x=140, y=110)
    eRP.insert(0, 0)

    labelRB = tk.Label(win2, text="Rooms with Balcony: ", font="times 10")
    labelRB.place(x=20, y=130)
    eRB = tk.Entry(win2)
    eRB.place(x=140, y=130)
    eRB.insert(0, 0)

    labelS = tk.Label(win2, text="Suits: ", font="times 10")
    labelS.place(x=20, y=150)
    eS = tk.Entry(win2)
    eS.place(x=140, y=150)
    eS.insert(0, 0)

    labelName = tk.Label(win2, text="Name: ", font="times 10")
    labelName.place(x=20, y=170)
    eName = tk.Entry(win2)
    eName.place(x=140, y=170)
    eName.insert(0, "default name")

    if checkValidInput(eNR.get(), int) or checkValidInput(eRB.get(), int) or checkValidInput(eS.get(),
                                                                                             int) or checkValidInput(
        eRP.get(), int) or checkValidInput(eName.get(), str):
        validInput = True

    ##tab menu
    tabCon = ttk.Notebook(win2)
    tabNR = ttk.Frame(tabCon)
    tabCon.add(tabNR, text="Normal Room")
    ttk.Label(tabNR, text="room size:").grid(column=0, row=0, padx=10, pady=10)
    ttk.Label(tabNR, text="Number of Beds:").grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(tabNR, text="price:").grid(column=0, row=2, padx=10, pady=10)

    esize3 = tk.Entry(tabNR)
    esize3.insert(0, 0)
    esize3.grid(column=1, row=0, padx=10, pady=10)
    enum3 = tk.Entry(tabNR)
    enum3.insert(0, 0)
    enum3.grid(column=1, row=1, padx=10, pady=10)
    eprice3 = tk.Entry(tabNR)
    eprice3.insert(0, 0)
    eprice3.grid(column=1, row=2, padx=10, pady=10)

    tabRP = ttk.Frame(tabCon)
    tabCon.add(tabRP, text="Room with Pool")
    ttk.Label(tabRP, text="room size:").grid(column=0, row=0, padx=10, pady=10)
    ttk.Label(tabRP, text="Number of Beds:").grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(tabRP, text="price:").grid(column=0, row=2, padx=10, pady=10)

    esize = ttk.Entry(tabRP)
    esize.insert(0, 0)
    esize.grid(column=1, row=0, padx=10, pady=10)
    enum = ttk.Entry(tabRP)
    enum.insert(0, 0)
    enum.grid(column=1, row=1, padx=10, pady=10)
    eprice = ttk.Entry(tabRP)
    eprice.insert(0, 0)
    eprice.grid(column=1, row=2, padx=10, pady=10)

    tabRB = ttk.Frame(tabCon)
    tabCon.add(tabRB, text="Room with Balcony")
    ttk.Label(tabRB, text="room size:").grid(column=0, row=0, padx=10, pady=10)
    ttk.Label(tabRB, text="Number of Beds:").grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(tabRB, text="price:").grid(column=0, row=2, padx=10, pady=10)

    esize1 = ttk.Entry(tabRB)
    esize1.insert(0, 0)
    esize1.grid(column=1, row=0, padx=10, pady=10)
    enum1 = ttk.Entry(tabRB)
    enum1.insert(0, 0)
    enum1.grid(column=1, row=1, padx=10, pady=10)
    eprice1 = ttk.Entry(tabRB)
    eprice1.insert(0, 0)
    eprice1.grid(column=1, row=2, padx=10, pady=10)

    tabS = ttk.Frame(tabCon)
    tabCon.add(tabS, text="Suite")
    ttk.Label(tabS, text="room size:").grid(column=0, row=0, padx=10, pady=10)
    ttk.Label(tabS, text="Number of Beds:").grid(column=0, row=1, padx=10, pady=10)
    ttk.Label(tabS, text="price:").grid(column=0, row=2, padx=10, pady=10)

    esize2 = ttk.Entry(tabS)
    esize2.insert(0, 0)
    esize2.grid(column=1, row=0, padx=10, pady=10)
    enum2 = ttk.Entry(tabS)
    enum2.insert(0, 0)
    enum2.grid(column=1, row=1, padx=10, pady=10)
    eprice2 = ttk.Entry(tabS)
    eprice2.insert(0, 0)
    eprice2.grid(column=1, row=2, padx=10, pady=10)

    if checkValidInput(esize.get(), int) or checkValidInput(esize1.get(), int) or checkValidInput(esize2.get(),
                                                                                                  int) or checkValidInput(
        esize3.get(), int):
        validSize = True
    if checkValidInput(enum.get(), int) or checkValidInput(enum1.get(), int) or checkValidInput(enum2.get(),
                                                                                                int) or checkValidInput(
        enum3.get(), int):
        validNum = True
    if checkValidInput(eprice.get(), int) or checkValidInput(eprice1.get(), int) or checkValidInput(eprice2.get(),
                                                                                                    int) or checkValidInput(
        eprice3.get(), int):
        validPrice = True
    tabCon.place(x=20, y=250)

    # if not (validPrice and validNum and validSize and validInput):
    #     exit(0)
    myHotel = None
    bt = tk.Button(win2, text="Save", width=20,
                   command=lambda: buttonpress(win2, create, myHotel, int(eNR.get()), int(eRP.get()), int(eRB.get()),
                                               int(eS.get()), str(eName.get()), int(esize.get()),
                                               int(esize1.get()), int(esize2.get()), int(esize3.get()), int(enum.get()),
                                               int(enum1.get()), int(enum2.get()),
                                               int(enum3.get()), int(eprice.get()), int(eprice1.get()),
                                               int(eprice2.get()), int(eprice3.get())))
    bt.place(x=150, y=430)
    win2.mainloop()


def startScreen():
    win1 = tk.Tk()
    win1.geometry("400x300")
    win1.config(bg="light blue")
    labelS = tk.Label(win1, text="Start Screen", font="times 28 bold")
    labelS.place(x=100, y=35)
    bt1 = tk.Button(win1, text="creatHotel", width=20, command=creatHotel)
    bt1.place(x=125, y=100)
    bt2 = tk.Button(win1, text="Load Hotel", width=20, command=loadHotel)
    bt2.place(x=125, y=175)
    bt3 = tk.Button(win1, text="Exit", width=20, command=exitPro)
    bt3.place(x=125, y=250)
    win1.mainloop()


def menuScreen(myhotel):
    win = tk.Tk()
    win.geometry("700x500")
    win.config(bg="light blue")
    ##----menu---##
    lable1 = tk.Label(win, text=(myhotel.managerName.upper()) + " Hotel Menu", font="times 28 bold")
    lable1.place(x=175, y=35)

    # tab win
    tabControl = ttk.Notebook(win)
    tabControl.place(x=50, y=100)

    tabChIn = ttk.Frame(tabControl)
    tabControl.add(tabChIn, text="Check In")

    ttk.Label(tabChIn, text="Enter Room Kind: ").grid(column=0, row=0, padx=10, pady=10)
    eRoomKind = ttk.Entry(tabChIn)
    eRoomKind.grid(column=1, row=0, padx=10, pady=10)
    ttk.Label(tabChIn, text="Enter Phone Number: ").grid(column=0, row=1, padx=10, pady=10)
    ePhoneNum = ttk.Entry(tabChIn)
    ePhoneNum.grid(column=1, row=1, padx=10, pady=10)
    ttk.Label(tabChIn, text="Enter Family Name: ").grid(column=0, row=2, padx=10, pady=10)
    eFamNam = ttk.Entry(tabChIn)
    eFamNam.grid(column=1, row=2, padx=10, pady=10)
    ttk.Label(tabChIn, text="Enter Amount of Nights: ").grid(column=0, row=3, padx=10, pady=10)
    eAmount = ttk.Entry(tabChIn)
    eAmount.grid(column=1, row=3, padx=10, pady=10)
    ttk.Label(tabChIn, text="your price is:  ").grid(column=0, row=4, padx=10, pady=10)
    ttk.Label(tabChIn, text="status: ").grid(column=0, row=5, padx=10, pady=10)

    bt1 = ttk.Button(tabChIn, text="Check IN", width=20,
                     command=lambda: CheckInScreen(tabChIn, myhotel, eRoomKind, ePhoneNum, eFamNam,
                                                   eAmount))
    bt1.grid(column=0, row=6, padx=10, pady=10)

    tabChOut = ttk.Frame(tabControl)
    tabControl.add(tabChOut, text="Check Out")
    ttk.Label(tabChOut, text="Enter room Number:").grid(column=0, row=0, padx=10, pady=10)
    eroomNu = ttk.Entry(tabChOut)
    eroomNu.grid(column=1, row=0, padx=10, pady=10)
    # check box if they returned everything
    # button check out , press and delete the details in the room

    tabSear = ttk.Frame(tabControl)
    tabControl.add(tabSear, text="Search")
    ttk.Label(tabSear, text="please choose the way to search:", font="times 10").grid(column=1, row=0, padx=10, pady=10)
    byPn = tk.IntVar()
    byfamilyName = tk.IntVar
    byRoomNum = tk.IntVar()
    tk.CHECKBUTTON(tabSear, text="by phone Number", varible=byPn).grid(column=0, row=0)
    tk.CHECKBUTTON(tabSear, text="by family name", varible=byfamilyName).grid(column=1, row=0)
    tk.CHECKBUTTON(tabSear, text="by Room Number", varible=byRoomNum).grid(column=2, row=0)

    tabDeta = ttk.Frame(tabControl)
    tabControl.add(tabDeta, text="See Details")

    tabSumm = ttk.Frame(tabControl)
    tabControl.add(tabSumm, text="Summary")

    #

    # bt2 = tk.Button(win, text="Check OUT", width=20, command=CheckOutScreen)
    # bt2.place(x=100, y=150)
    # bt3 = tk.Button(win, text="Check available rooms", width=20, command=Checkavai)
    # bt3.place(x=100, y=200)
    # bt4 = tk.Button(win, text="Search", width=20, command=search)
    # bt4.place(x=100, y=250)
    # bt5 = tk.Button(win, text="Summary the day ", width=20, command=summary)
    # bt5.place(x=100, y=300)
    bt6 = tk.Button(text="See Details", width=20, command=detalis)
    bt6.place(x=100, y=350)
    win.mainloop()


if __name__ == '__main__':
    main()
