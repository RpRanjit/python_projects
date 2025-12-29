import hashlib



file1 = r"path fo first file"
file2 =r"path of second file"
def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    # Now open the file
    with open(fileName1, 'rb') as file:
        # use file.read to read the size of thefile
        # read the file in samll chunk because we cannot read large file size
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file(file1, file2)

if msg1 != msg2:
    print("PDF are not identical:")
else:
    print("pdf are identical")