import os

POEM = "Two minds, one road. We read the same map, chose the same north, and walked. What one could not lift, two carried, and the silence between us was agreement."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
