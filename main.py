def main():
    print("Hello from bam5103!")


if __name__ == "__main__":
    main()
import requests

r = requests.get("https://github.com/pimatskku/sturdy-
memory/raw/refs/heads/main/dataset.zip")

open("dataset.zip", "wb").write(r.content)
