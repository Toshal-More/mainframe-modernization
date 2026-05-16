import boto3

# ============================================================
#  PHASE 4 — Cloudflare R2 Cloud Upload
#  Uploads CSV file to Cloudflare R2 bucket
# ============================================================

# Your Cloudflare R2 credentials
ACCESS_KEY    = "7c729f3b6dcb887305420fedbcabddeb"        # ← paste your Access Key ID
SECRET_KEY    = "e7e8945135a99c074a356db3e33c3b26c31fef127eb91c214cdbc809975fb286"    # ← paste your Secret Access Key
ENDPOINT_URL  = "https://6be126bed672ad6dfc29895ea332cf31.r2.cloudflarestorage.com"         # ← paste your Endpoint URL
BUCKET_NAME   = "mainframe-modernization"

# Local file to upload
LOCAL_FILE    = (r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\output\employees.csv")

# Name of file inside R2 bucket
R2_FILE_NAME  = "employee-salary/employees_salary.csv"

def main():
    Connect_R2()

def Connect_R2():
    print("Connecting to Cloudflare R2...")

    s3 = boto3.client(
        's3',
        endpoint_url          = ENDPOINT_URL,
        aws_access_key_id     = ACCESS_KEY,
        aws_secret_access_key = SECRET_KEY,
        region_name           = 'auto'
    )

    print("Connected successfully!")
    Upload_File(s3)

def Upload_File(s3):
    print("Uploading file...")

    s3.upload_file(
        LOCAL_FILE,
        BUCKET_NAME,
        R2_FILE_NAME
    )

    print(f"File uploaded successfully!")
    print(f"Location: {BUCKET_NAME}/{R2_FILE_NAME}")

main()
