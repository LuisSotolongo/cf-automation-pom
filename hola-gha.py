import os


def main():
    print("Hola, GitHub Actions!")
    secret_value = os.getenv("USERNAME")
    if secret_value:
        print(f"My secret value is: {secret_value}")
    else:
        print("No secret value found.")


if __name__ == "__main__":
    main()