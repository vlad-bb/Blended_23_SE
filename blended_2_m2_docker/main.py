from datetime import datetime


def main():
    with open('data/cron.log', 'a') as file:
        info = f"Now is {datetime.now()}\n"
        print(info)
        file.write(info)


if __name__ == "__main__":
    main()
