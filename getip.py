from sockit import*
while True :
    link = str(input("enter the website link :"))
    host = gethostbyname(link)
    print(host)
