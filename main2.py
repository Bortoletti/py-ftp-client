#
# upload de multiplos arquivos
#
import os
import ftplib

path_upload = "/home/luis/usr/py/ftp-client/upload"

arquivos = os.listdir( path_upload )

for arquivo in arquivos:
    print( arquivo )


HOSTNAME = "***"
USERNAME = "***"
PASSWORD = "***"

ftp = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD) 
#ftp.set_debuglevel(2)
ftp.set_pasv( False )
ftp.encoding = "utf-8"
ftp.dir() 

for arquivo in arquivos:
    try:
            ftp.delete( arquivo )
            print(f"\n{arquivo} - excluido")
    except:
        print(f"\nfalhou exclusao{arquivo}")

    filenamein = path_upload + "/"+ arquivo
    filenameout = arquivo
    with open(filenamein, "rb") as file: 
        ftp.storbinary(f"STOR {filenameout}", file) 

ftp.dir() 
ftp.quit()
