midterms = [90, 21, 32]
finals = [90, 99, 25]
students = ['Joe', 'Kaila', 'Qhawe']

# check = (zip(midterms, finals))
# # print(list(check))
#
# # final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
# # print(final_grades)
# grades = zip (students,
#     map(
#     lambda pair: max(pair),
#     zip(midterms, finals)
# ))
#
# print(dict(grades))

def interleave(str1, str2):
    z = zip(str1, str2)
    total = ""
    for pair in z:
        total += pair[0] + pair[1]
    return total


x = interleave("pig", "dog")
print(x)
