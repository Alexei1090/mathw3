# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). 
# на факультете B в). на факультете C?

v = 1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9

v1 = (1/4 * 0.8) / v # на факультете A
v2 = (1/4 * 0.7) / v # на факультете B 
v3 = (1/2 * 0.9) / v # на факультете c

print(v1)
print(v2)
print(v3)