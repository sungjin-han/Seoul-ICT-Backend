import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


start = time.time()

for i in range(4):
    heavy_work(i)

end = time.time()

print("수행시간: %f 초" % (end - start))
