import oracledb

# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()

class Person:
    def __init__(self, empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno

    def print_person(self):
        print(f"{self.empno} : {self.ename}")

def show_menu():
    print("-- 임직원 관리 시스템 --")
    print("- 1. 직원 추가    -")
    print("- 2. 직원 삭제    -")
    print("- 3. 직원 조회    -")
    print("- 4. 프로그램 종료 -")
    menu_num = input("메뉴를 선택해 주세요.")
    print(menu_num)
    return menu_num

def insert_emp(): # empno, ename, job, mgr, hiredate, sal, comm, deptno  
    print("새로운 직원의 사번, 이름을 입력하세요....")
    empno, ename = input().split()
    print(empno, ename)

    if empno.isdigit():        
#INSERT 예제
        try:
            # INSERT INTO EMP(EMPNO, ENAME) VALUES('1234','LEO')
            cursor.execute("INSERT INTO EMP(EMPNO, ENAME) VALUES (:1, :2)", [empno, ename.upper()])
            conn.commit()
            print("Data inserted successfully")
        except oracledb.DatabaseError as e:
            print(f"Error inserting data: {e}")
    else:
        print("ERR-INSERT-001 : 사번 입력 오류 입니다. 숫자만 입력 가능합니다.")

def search_emp():
# SELECT 예제
    try:
        cursor.execute('''
            SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO 
            FROM emp
            ORDER BY EMPNO''')
        for row in cursor:
            # print(row)
            p = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            p.print_person()
    except oracledb.DatabaseError as e:
        print(f"Error fetching data: {e}")

while True:
    select = int(show_menu())
    if select == 1:
        print("1. 직원 추가 메뉴")
        insert_emp()
    elif select == 2:
        print("2. 직원 삭제 메뉴")
    elif select == 3:
        print("3. 직원 조회 메뉴")
        search_emp()
    else:
        print("프로그램 종료 ***")
        break

# 커서 및 커넥션 닫기
cursor.close()
conn.close()