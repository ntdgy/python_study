import random

def main():
    N = random.randint(2147483647, 21474836470)
    writer = open("input.txt", "w")
    writer.write(str(N))
    writer.close()

if __name__ == "__main__":
    main()
