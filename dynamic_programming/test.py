
import os
import sys
from io import BytesIO, IOBase

def knapsack(wt,price,n,c,dp):
    if n<0 or c==0:
        return 0
    if dp[n][c]!=-1:
        return dp[n][c]
    inc=exc=0
    if c>=wt[n]:
        inc=price[n]+knapsack(wt,price,n-1,c-wt[n],dp)
    exc=0+knapsack(wt,price,n-1,c,dp)
    dp[n][c]=max(inc,exc)
    return max(inc,exc)

def main():
    n,c=map(int,input().split())
    wt=[]
    price=[]
    for _ in range(n):
        w,v=map(int,input().split())
        wt.append(w)
        price.append(v)
    dp=[[-1 for x in range(c+1)] for y in range(n+1)]
    print(knapsack(wt,price,n-1,c,dp))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()