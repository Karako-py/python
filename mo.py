sum=0
counter=0
ap="Ναι"
while ap=="Ναι" or ap=="ναι":
    number=int(input("Δώσε βαθμό:"))
    sum=sum+number
    counter+=1
    ap=raw_input("Θες να ξανα δώσεις βαθμό;")
mo=sum/counter
print "Ο μέσος όρος είναι",mo
