import dropbox

class TransferData:

    def __init__p(self,access_Token):

        self.access_Token = access_Token

    def uploadFile(self,file_from,file_to):

        dbx = dropbox.Dropbox(self.access_Token)
        f = open(file_from , 'rb')
        dbx.files_upload(f.read(),file_to)

def main():

    access_Token = 'HGP16dUUIoUAAAAAAAAAAVwxvkAQ4wETx4oB32HkcTIfz_RAHZhZ5dGP3Wg-hTS2' 
    transferData = TransferData(access_Token)     
    file_from = input("Enter the full name to transfer : ")
    file_to = input("Enter the full path th upload to DropBox : ") 
    transferData.uploadFile(file_from,file_to)
    print("The File has been moved ")

main()
