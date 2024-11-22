import boto3

def upload_file_to_s3(bucket_name, file_path, key):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, key)
    print(f"Fichier {file_path} uploadé dans {bucket_name} avec la clé {key}.")

if __name__ == "__main__":
    bucket_name = "votre-bucket"
    file_path = "documents/mon_document.txt"
    key = "mon_document.txt"
    upload_file_to_s3(bucket_name, file_path, key)
