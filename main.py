from pyprnt import prnt

creation = ["Adam", "Eve"]
menu = {
    "Kimchi": 5000,
    "Ice Cream": 100
}
prnt(creation)
prnt(menu)
prnt(["abcd"], ["efgh"], sep="-")
prnt("010", "8282", "8282", sep="-")
prnt("Hiii")
prnt("Hi", "Kev")
print("Hi", "Kev")
prnt(["A","A","A","A","A","A","A","A","A","A"])
prnt(["Hello"], both=True)
prnt(["ldakfjsdlkjflkasdjflkajflkjdklfjalkjfsalkjfkldnflkndslknlkfndlkfnlkdansfdklnfalnfknlfl"])
prnt(["HI"], enable=False)
prnt(creation, end="")
prnt("The force is with me")
heros = [["Spiderman", "Ironman"], ["Vision", "Scarlet Witch"]]
prnt(heros, both=True)
