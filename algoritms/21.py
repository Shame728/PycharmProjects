import random

k = 2
m, n = 2, 3

with open("file1.txt", "w", encoding="utf-8") as f1:
    for i in range(k):
        for j in range(m):
            row = [str(random.randint(1, 9)) for h in range(n)]
            f1.write(" ".join(row) + "\n")

        for j in range(m):
            row = [str(random.randint(10, 20)) for h in range(n)]
            f1.write(" ".join(row) + "\n")

with (open("file1.txt", "r", encoding="utf-8") as f1,
      open("file2.txt", "w", encoding="utf-8") as f2):

    for h in range(k):
        mat1 = [list(map(int, f1.readline().split())) for g in range(m)]
        mat2 = [list(map(int, f1.readline().split())) for g in range(m)]

        for i in range(m):
            summa = [str(mat1[i][j] + mat2[i][j]) for j in range(n)]
            f2.write(" ".join(summa) + "\n")

print("Матрицы:")
with open("file1.txt", "r", encoding="utf-8") as f1:
    print(f1.read())

print("Сумма матриц:")
with open("file2.txt", "r", encoding="utf-8") as f2:
    print(f2.read())
