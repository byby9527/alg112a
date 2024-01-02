def newton_raphson(f, f_prime, x0, tol=1e-6):

    while True:
        f_x0 = f(x0)
        f_prime_x0 = f_prime(x0)
        if abs(f_x0) < tol:
            return x0
        x1 = x0 - f_x0 / f_prime_x0
        x0 = x1
def main():
    n = int(input("請輸入 n 值："))
    coefficients = [float(input("請輸入係數 a_" + str(i) + "：")) for i in range(n + 1)]

    # 定義多項式函數
    def f(x):
        return sum([coefficients[i] * x**i for i in range(n + 1)])


    # 定義多項式函數的導數
    def f_prime(x):
        return sum([i * coefficients[i] * x**(i - 1) for i in range(1, n + 1)])


    # 求解多項式的根
    x0 = 1
    x = newton_raphson(f, f_prime, x0)
    print("多項式的根是：", x)

if __name__ == "__main__":
    main()


