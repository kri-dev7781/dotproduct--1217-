from multiprocessing import Pool

def dot(a, b):
    
    def mul(xy):
        x, y = xy
        return x * y
    with Pool(2) as p:
        parts = p.map(mul, zip(a, b))
    return sum(parts)

if __name__ == "__main__":
    a = list(map(int, input("Enter first vector: ").split()))
    b = list(map(int, input("Enter second vector: ").split()))
    if len(a) != len(b):
        print("Error: vectors must be of same length")
    else:
        print("Dot product : ", dot(a, b))
