import csv
import sys

import pulp

from typedef import Item, Result, ResultItem

class IpProblem():
    def __init__(self):
        self.__problem = pulp.LpProblem(sense=pulp.LpMaximize)
    
    def create_model(self, items: list[Item], job_limit: list[int]) -> None:
        self.__x_item = [pulp.LpVariable(name=item["name"], lowBound=0, cat=pulp.LpInteger) for item in items]

        #   create objective function
        assert len(items) == len(self.__x_item)
        self.__problem += pulp.lpSum(item["profit"] * x for item, x in zip(items, self.__x_item))
        
        #   create constraints
        assert len(job_limit) == len(items[0]["job"])
        for i in range(len(job_limit)):
            self.__problem += pulp.lpSum(item["job"][i] * x for item, x in zip(items, self.__x_item)) <= job_limit[i]
    

    def solve(self) -> Result:
        self.__problem.solve()

        #   create result
        items: list[ResultItem] = list()
        for x in self.__x_item:
            item: ResultItem = {
                "name": x.getName(),
                "value": pulp.value(x)
            }
            items.append(item)

        result: Result = {
            "status": str(pulp.LpStatus[self.__problem.status]),
            "objective_value": pulp.value(self.__problem.objective),
            "items": items
        }

        return result
    

    __problem: pulp.pulp.LpProblem
    __x_item: list[pulp.pulp.LpVariable]


def read_instance_csv(input_file: str) -> list[Item]:
    items: list[Item] = list()
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)    #header
        for info in reader:
            item: Item = {
                "name": info[0],
                "job": list(map(int, info[1:-1])),
                "profit": int(info[-1])
            }
            items.append(item)

    return items


def read_job_limit_csv(input_file: str) -> list[int]:
    job_limit: list[int] = list()
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)    #header
        for info in reader:
            job_limit.append(int(info[1]))

    return job_limit


def main():
    args: list[str] = sys.argv
    if ( len(args) != 3):
        print("python main.py ${input_instance} ${input_job_info}")
        sys.exit(1)
    
    input_instance: str = args[1]
    input_job_info: str = args[2]

    items: list[Item] = read_instance_csv(input_instance)
    job_limit: list[int] = read_job_limit_csv(input_job_info)

    problem = IpProblem()
    problem.create_model(items, job_limit)

    result: Result = problem.solve()
    print("status: {}".format(result["status"]))
    print("max_profit: {}".format(result["objective_value"]))
    for item in result["items"]:
        print("{}: {}".format(item["name"], item["value"]))


if __name__ =="__main__":
    main()
