import time
import hashlib

start_time = time.time()

number_of_hash = 1999999

# generate hashes
for i in range(number_of_hash):
    hashlib.sha224(
        str.encode(str(i))
    ).hexdigest()

took = time.time() - start_time

print("Hashrate: {}".format(i / took))
