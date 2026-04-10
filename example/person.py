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
        if self.sal is not None:
            print(f"{self.empno} : {self.ename:>10} : {int(self.sal):>7}")
        else:
            print(f"{self.empno} : {self.ename:>10} :       0")