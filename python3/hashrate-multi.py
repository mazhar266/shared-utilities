import os
import time
import hashlib
import multiprocessing

no_of_cores = os.cpu_count()
functions = []
objs = []
number_of_hash = 1999999
queue = multiprocessing.Queue()

print('Number of Cores: {}'.format(no_of_cores))

for i in range(no_of_cores):
    def fn(q):
        start_time = time.time()
        print('Running task on core {}'.format(i))
        # generate hashes
        for j in range(number_of_hash):
            hashlib.sha224(
                str.encode(str(j))
            ).hexdigest()

        print('Finished task on core {}'.format(i))
        took = time.time() - start_time
        q.put(took)

    functions.append(fn)

for i in range(no_of_cores):
    objs.append(
        multiprocessing.Process(
            name=str(i),
            target=functions[i],
            args=(queue, )
        )
    )

for i in range(no_of_cores):
    objs[i].start()

for i in range(no_of_cores):
    objs[i].join()

print('All tasks are completed')

# now make an average of time took
avg_time = 0.0

while not queue.empty():
    avg_time = avg_time + queue.get()

avg_time = avg_time / no_of_cores

# calculate the hashrate
hashrate = (number_of_hash * no_of_cores) / avg_time

# print more human friendly
if ((hashrate / 10000000) > 1):
    print("Hashrate: %.3f GHash/s" % (hashrate / 10000000))
else:
    if ((hashrate / 100000) > 1):
        print("Hashrate: %.3f MHash/s" % (hashrate / 100000))
    else:
        if ((hashrate / 1000) > 1):
            print("Hashrate: %.3f KHash/s" % (hashrate / 1000))
        else:
            print("Hashrate: %.3f Hash/s" % (hashrate))
