scores ={
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

students =[]
average_students =0
top_student =""
highest_score =-1

for name,score in scores.items():
    if score >= 17:
        grade = "عالی"
    elif score >= 14:
        grade ="خوب"
    elif score >= 10:
        grade ="قبول"
    else:
        grade ="مردود"
    print(f"{name}: {score} -> {grade}")

if score >=10:
    students.append(name)

average_students = average_students + score
if score > highest_score:
    highest_score = score
    top_student = name

print(f"کسانی که قبول شده اند: {students}")    
av = average_students / len(scores)
print(f"میانگین: {av}")
print(f"نفر اول: {top_student}")
