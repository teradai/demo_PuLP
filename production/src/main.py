import csv
import sys
from typedef import Item

# import pulp

def read_csv(input_file: str) -> list[Item]:
    items: list[Item] = list()
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)    #header
        for info in reader:
            item: Item = {
                "name": info[0],
                "job": info[1:-1],
                "profit": info[-1]
            }
            items.append(item)

    return items

def main():
    args: list[str] = sys.argv
    if ( len(args) != 2):
        print("python main.py ${input_file}")
        sys.exit(1)
    
    input_file: str = args[1]
    items: list[Item] = read_csv(input_file)
    


if __name__ =="__main__":
    main()
