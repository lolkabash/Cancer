import sqlite3
connection = sqlite3.connect('JC_2019.db')
user_L1R5 = input('L1R5: ') #L1R5 from HTML form.
user_L1R4 = input('L1R4: ') #L1R4 from HTML form.
Arts_Data = connection.execute('''
SELECT JuniorCollege, Arts
FROM JC_2019
WHERE Arts >= ?
ORDER BY Arts ASC
''',(user_L1R5,))

Science_Data = connection.execute('''
SELECT JuniorCollege, Science_IB
FROM JC_2019
WHERE Science_IB >= ?
ORDER BY Science_IB ASC
''',(user_L1R5,))
Arts_List = Arts_Data.fetchall()
Science_List = Science_Data.fetchall()
print(Arts_List)
print(Science_List)
connection.close()

connection = sqlite3.connect('Poly_2019.db')
Poly_Data = connection.execute('''
SELECT *
FROM Poly_2019
WHERE JAE_ELR2B2 >= ?
ORDER BY JAE_ELR2B2 ASC
''',(user_L1R4,))
Poly_List = Poly_Data.fetchall()
print(Poly_List)
connection.close()

if user_L1R4 <= 20:
    print([('Millennial Institution', 20)])