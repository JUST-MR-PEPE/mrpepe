from socket import*
while True :
    link = input("enter the website link :")
    host = gethostbyname(link)
    print(host)
