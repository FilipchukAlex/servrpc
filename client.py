from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient import id_generators

random_ids = id_generators.decimal()
client = HTTPClient("http://localhost:5000/api",
                    id_generator=random_ids,
                    basic_logging=True)
running = True


def hello():
    name = input("Enter your name ... ")
    response = client.request("Servrpc.hello", name)
    print()
    print(response.data.result)
    print()


def add_digit():
    barcode = input("Enter 12 digits ... ")
    response = client.request("Servrpc.add", barcode)
    print()
    print(response.data.result)
    print()


def exit():
    global running
    running = False


def print_prompt():
    print("~ Welcome to Json RPC Client ~")
    print("Select one of the method below:")
    print("     1  - Hello")
    print("     2  - Add check digit to yor EAN13 barcode")
    print("     3  - Exit")


def main():
    while running:
        menu = {
                '1':  hello,
                '2':  add_digit,
                '3':  exit
        }
        print_prompt()
        user_input = input("your choice: ")
        menu[user_input]()


if __name__ == '__main__':
    main()
