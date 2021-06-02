# with open("img3.jpg", "rb") as image:
#   f = image.read()
# #   print (f)
#   b = bytearray(f)
# #   //print( b[0])," "

# # print(f)
# data = f.decode('utf-16')
# print(data)
# # n = open("img4.png", "wb")
# # n.write(f)
# # n.close

# with open("k20.txt",'w') as file:
#   for i in range(200000,201700):
#     file.write("k"+str(i)+"@nu.edu.pk")
#     file.write("\n")

import concurrent.futures
from threading import Thread
import queue
import time

def foo(bar):
    # if i == 2:
    #   time.sleep(5)
    print('hello {}'.format(bar[0])+bar[1])
    return bar

que = queue.Queue()
threads_list = list()


for i in range(1,11):
  t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, ['world!',str(i)]))
  t.start()
  threads_list.append(t)

# Add more threads here
# ...
# threads_list.append(t2)
# ...
# threads_list.append(t3)
# ...

# Join all the threads
for t in threads_list:
    t.join()

# Check thread's return value
while not que.empty():
    result = que.get()
    print (result)

# for i in range(1,11):
#   with concurrent.futures.ThreadPoolExecutor() as executor:
#       future = executor.submit(foo, 'world!',i)
#       return_value = future.result()
#       print(return_value)