""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
if __name__ == "__main__":
    process1 = mp.Process(target=counter, args=("1num",))
    process2 = mp.Process(target=counter, args=("2num",))
    process3 = mp.Process(target=counter, args=("3num",))

    start = time.time()

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    end = time.time()

    print("proc-end", end - start) """

""" import asyncio
import random as rd
import time

async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
    
    print(f"end of {name}")
    

async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))
    
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end-start)
    
    
if __name__ == '__main__':
    asyncio.run(main()) """
    
""" import asyncio
import time

async def worker1():
    for i in range(1,6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)
    
async def worker2():
    for i in range(1,4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
async def main():
    
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())

    print("start task")
    start = time.time()
    await task_1
    await task_2
    end = time.time()
    print("end - ", end-start)
    print("end task")
    
if __name__ == '__main__':
    asyncio.run(main()) """
    



""" import sched
import time

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    print(f"end of {name}")

def run() :
    s = sched.scheduler()
    s.enter(5,1,tester,('1num',))
    s.enter(5,1,tester,('4num',))
    s.enter(3,1,tester,('2num',))
    s.enter(7,1,tester,('3num',))
    s.run()

if __name__ == "__main__":
    run()
    #main()
    print("end") """
    

#문자열 비교
""" import diff_match_patch.diff_match_patch as dm
    
origin = "To be or not to be, That is a question!"
copyed = "To be or not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff :
    print(d) """
    
    
    
""" from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

#with open("fktemp.csv", "w", newline='') as f :
with open("fktemp.txt", "w", newline='') as f :
    for i in range(30):
        f.write(temp.name() + "," +
            temp.address() + "," +
            temp.postcode() + "," +
            temp.country() + "," +
            temp.company() + "," +
            temp.job() + "," +
            temp.phone_number() + "," +
            temp.email() + "," +
            temp.user_name() + "," +
            temp.ipv4_private() + "," +
            temp.catch_phrase() + "," +
            temp.color_name() + "\n")  """
 
""" from faker import Faker as fk

# temp = fk()
temp = fk("ko-KR")
print(temp.name())


with open("fktemp.txt", "w" , newline='') as f :
    for i in range(30):
        f.write(temp.name() + "\n" + 
            temp.address() + "," + 
	        temp.postcode() + "," + 
	        temp.company() + "," + 
	        temp.job() + "," + 
	        temp.phone_number() + "," + 
	        temp.email() + "," + 
	        temp.user_name() + "," + 
	        temp.ipv4_private() + "," + 
	        temp.ipv4_public() + "," + 
	        temp.catch_phrase() + "," + 
	        temp.color_name() + "\n")
 """

#Subprocess

""" import subprocess as sp

# res = sp.run(["cmd", "/c", "dir"], capture_output=True)
res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=False)
#res = sp.run(["cmd", "/c" ,"iexplore.exe"], capture_output=False)

print(res) """


#try - except
""" import traceback as tb

def tester():
    #return 1/0
    return 1

def caller() :
    tester()
    
def main():
    try :
        caller()
        
    #except ZeroDivisionError:
        #print("zde error")
    
    except ValueError:
        print("ve error")
        
    except Exception as ex :
        print("ex error", ex)
        
    else : 
        print("ok")
        
    finally :
        print("end") """
        

