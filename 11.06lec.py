#입력암호화
""" import getpass

pw = getpass.getpass("Pass : ")
# pw = input("Pass :")
print(pw)
 """

#해시함수

#sha256
""" import hashlib

hl = hashlib.sha256()
# target = "hello"
# target = "python"
target = "db"

hl.update(target.encode("utf-8"))
print(hl.hexdigest()) """

#keccak256

""" import Crypto.Hash.keccak as kek

target = "as sa as"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

# print(kksh.digest())
print(kksh.hexdigest()) """

#활용

""" import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """


""" import os
import hashlib

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs=hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
        
    else :
        return True
    
if pwInsert():
    pw = input('new pass:')
    with open('pw.txt', 'w') as fp :
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
        
else:
    print("not allow password")
     """
    
#시스템정보 확인

""" import platform as pf

pn = pf.uname()
pm = pf.machine()
pp = pf.processor()
ps = pf.system()

print(pn)
print(pm)
print(pp)
print(ps) """


#웹페이지 읽기

""" import urllib.request as ur

# url = 'https://www.google.com'
# url = 'https://www.daum.net'
url = 'https://www.xkcd.com'

#res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
print(web) """



""" import http.client as hc

# url = 'www.daum.net'
url = 'v.daum.net'

conn = hc.HTTPSConnection(url)
# conn.request("GET", "/")
conn.request("GET", "/v/20231103063908539")

r = conn.getresponse()

with open("ulcl.html","wb") as fp :
    fp.write(r.read())
    
conn.close()

print(r) """



""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)
    
print(web) """


""" import time
# import threading

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

for i in range(3) :
    counter(f"num{i}")
    
    
start = time.time()
for i in range(3):
    counter(f"num{i}")
end = time.time()

print("single end",start - end)
 """


""" import threading as td

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("multi end") """


""" import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))


start = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end" , start - end) """

#mutil processing(error)
""" import multiprocessing
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
        
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))


start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc- end", end - start) """


#main 실행

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    # run()
    main()