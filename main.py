#
# upload de unico arquivo
#
import ftplib 

HOSTNAME = "****"
USERNAME = "***"
PASSWORD = "*****"

ftp = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD) 
#ftp.set_debuglevel(2)
ftp.set_pasv( False )
ftp.encoding = "utf-8"
ftp.dir() 

try:
    ftp.delete("teste2.txt")
except:
    print("\nfalhou exclusao\n")

filenamein = "upload/teste.txt"
filenameout = "teste.txt"
with open(filenamein, "rb") as file: 
   ftp.storbinary(f"STOR {filenameout}", file) 

ftp.dir() 
ftp.quit()
