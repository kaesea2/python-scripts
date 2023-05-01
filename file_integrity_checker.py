import hashlib
import time

def generate_hash(filename):
    """Generate SHA-256 hash of a file"""
    hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # to read the file in smaller chunks of 4kb i.e 4096bytes at a time and \
            # the b"" is used to indicate EOF i.e an empty byte string 
        for chunk in iter(lambda: f.read(4096), b""): 
            hash.update(chunk)
    return hash.hexdigest()

def monitor_file(filenames,*args):
    """Monitor a file for changes"""
    current_hash = {filename: generate_hash(filename) for filename in filenames}
    while True:
        time.sleep(5) # Wait for 5 seconds before checking again
        for fname in filenames:
            new_hash = generate_hash(fname)
            if new_hash != current_hash[fname]:
                print(f"File '{fname}' has been modified!")
                current_hash[fname] = new_hash

if __name__ == "__main__":
    filenames = ['activeDirectory_notes.txt','delivery-status.txt','Ekwueme Emmanuel kenechukwu.docx']
    monitor_file(filenames)
