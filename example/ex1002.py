def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2026년 3월 27일', '나장발')
visit('2026년 3월 27일', '나장발', '나수염', '나김리', '강승진')