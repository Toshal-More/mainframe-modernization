import boto3

ACCESS_KEY    = "7c729f3b6dcb887305420fedbcabddeb"        # ← paste your Access Key ID
SECRET_KEY    = "e7e8945135a99c074a356db3e33c3b26c31fef127eb91c214cdbc809975fb286"    # ← paste your Secret Access Key
ENDPOINT_URL  = "https://6be126bed672ad6dfc29895ea332cf31.r2.cloudflarestorage.com"         # ← paste your Endpoint URL
BUCKET_NAME   = "mainframe-modernization"


def main():
   R3 = connect_cloud_R3()

   LOCAL_FILE = (r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\02_bank-transaction-pipeline\output\Tran_Export.csv")

   R3_FILE_NAME = ("Tran_Export/Tran_Export_cloud.csv")

   upload_files(R3,LOCAL_FILE,R3_FILE_NAME)


def connect_cloud_R3():

    R3 = boto3.client(
        's3',
        endpoint_url          = ENDPOINT_URL,
        aws_access_key_id     = ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY,
        region_name           = 'auto'
    )

    return R3

def upload_files(R3,LOCAL_FILE,R3_FILE_NAME):

    R3.upload_file(
        LOCAL_FILE,
        BUCKET_NAME,
        R3_FILE_NAME
    )
    
    print(f"File uploaded successfully!")
    print(f"Location: {BUCKET_NAME}/{R3_FILE_NAME}")

main()