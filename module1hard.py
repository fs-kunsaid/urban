grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
Aaron = grades[0]
Aaron_ave = sum(Aaron) / len(Aaron)
Bilbo = grades[1]
Bilbo_ave = sum(Bilbo) / len(Bilbo)
Johnny = grades[2]
Johnny_ave = sum(Johnny) / len(Johnny)
Khendrik = grades[3]
Khendrik_ave = sum(Khendrik) / len(Khendrik)
Steve = grades[4]
Steve_ave = sum(Steve) / len(Steve)
grades_new = {students_list[0]: Aaron_ave, students_list[1]: Bilbo_ave, students_list[2]: Johnny_ave,
           students_list[3]: Khendrik_ave, students_list[4]: Steve_ave}
print(grades_new)