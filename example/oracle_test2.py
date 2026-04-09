import oracledb

# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()

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

#INSERT 예제
    try:
        # INSERT INTO EMP(EMPNO, ENAME) VALUES('1234','LEO')
        cursor.execute("INSERT INTO EMP(EMPNO, ENAME) VALUES (:1, :2)", [empno, ename.upper()])
        conn.commit()
        print("Data inserted successfully")
    except oracledb.DatabaseError as e:
        print(f"Error inserting data: {e}")

def search_emp():
# SELECT 예제
    try:
        cursor.execute("SELECT * FROM emp")
        for row in cursor:
            print(row)
    except oracledb.DatabaseError as e:
        print(f"Error fetching data: {e}")

loop = True
while loop:
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
        loop = False

# 커서 및 커넥션 닫기
cursor.close()
conn.close()