from src.index import PrimeNumbers

if __name__ == "__main__":
    n = int(input("Nhập n: "))
    print("Các số 1nguyên tố từ 2 đến", n, "là:", PrimeNumbers(n))