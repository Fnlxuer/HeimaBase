import time
start = time.clock()
print('This will be output immediately.')
end = time.clock()
print(end-start)

start = time.clock()
print('This will be output immediately.',flush=True)
end = time.clock()
print(end-start)