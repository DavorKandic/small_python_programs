import hashlib

def hash_file(filename):
    """Returns the SHA-1 hash of passed file"""
    hash_obj = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            # There is a reason for reading that
            # size of chunks! 
            chunk =file.read(1024) 
            hash_obj.update(chunk)
            # returns the hex representation of digest
        return hash_obj.hexdigest()
		
		
msg = hash_file('find_file_hash.py')
print(msg)
