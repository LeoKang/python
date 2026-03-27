products = ['JOA-2020', 'JOA-2021',
 'SIRO-2021', 'SIRO-2022']
recall = []
for p in products:
    if p.startswith('SIRO'):
        recall.append(p)

print(recall)