# pruduction
## overview
下記のような整数計画問題を解くためのプログラム.  
table  と chair を作成するために、1個あたりの作成時間, 利益がそれぞれ下記のように与えられている.

|   | table | chair |
|---|---|---|
| job1 | 2h | 2h |
| job2 | 3h | 5h |
| profit | 4000円 | 5000円 |

job1は7時間, job2は1日あたり14時間稼働することができる.  
利益を最大化するのはtableとchairをそれぞれ1日あたり何個作成すれば良いか?


## Requirement
* PuLP  2.6.0

## install
```
pip install PuLP
```

## Usage
```
git clone 
cd production
python src/main.py sample/instance1.txt sample/job_limit1.txt
```
