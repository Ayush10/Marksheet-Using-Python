from PIL import Image, ImageFont, ImageDraw
from datetime import date
marksheet = Image.open("marksheet.png")
today = date.today()
draw = ImageDraw.Draw(marksheet)
font = ImageFont.truetype("arial.ttf", 20)


def main():
    user_input()
    basic_marketing()
    commerce()
    mobile_programming()
    marksheet.show()
    marksheet.save("final_result.png")


def user_input():
    print("Information about Student: ")
    name = input("Enter student name: ")
    issued_date = today
    semester = input("Enter student semester: ")
    section = input("Enter student section: ")
    registration_number = input("Enter student Registration Number: ")
    draw.text((143, 220), name, "Black", font=font)
    draw.text((682, 220), semester, "Black", font=font)
    draw.text((1056, 220), section, "Black", font=font)
    draw.text((1315, 220), registration_number, "Black", font=font)
    draw.text((1172, 161), str(issued_date), "Red", font=font)


def basic_marketing():
    print("Basic Marketing: ")
    first_assignment = int(input("Enter student first assignment marks out of 10: "))
    internal = int(input("Enter Internal Examination marks out of 10: "))
    attendance = int(input("Enter student attendance marks out of 10: "))
    quiz = int(input("Enter student quiz marks out of 10: "))
    group_project = int(input("Enter student group project marks: "))
    total = first_assignment + internal + attendance + quiz + group_project
    height = 383
    draw.text((401, height), str(first_assignment), "Black", font=font)
    draw.text((587, height), str(internal), "Black", font=font)
    draw.text((823, height), str(attendance), "Black", font=font)
    draw.text((1123, height), str(quiz), "Black", font=font)
    draw.text((1287, height), str(group_project), "Black", font=font)
    draw.text((1387, height), str(total), "Red", font=font)


def commerce():
    print("Introduction to E-Commerce: ")
    first_assignment = int(input("Enter student first assignment marks out of 10: "))
    internal = int(input("Enter Internal Examination marks out of 10: "))
    attendance = int(input("Enter student attendance marks out of 10: "))
    quiz = int(input("Enter student quiz marks out of 10: "))
    group_project = int(input("Enter student group project marks: "))
    total = first_assignment + internal + attendance + quiz + group_project
    height = 499
    draw.text((401, height), str(first_assignment), "Black", font=font)
    draw.text((587, height), str(internal), "Black", font=font)
    draw.text((823, height), str(attendance), "Black", font=font)
    draw.text((1123, height), str(quiz), "Black", font=font)
    draw.text((1287, height), str(group_project), "Black", font=font)
    draw.text((1387, height), str(total), "Red", font=font)


def computer_graphics():
    print("Computer Graphics: ")
    first_assignment = int(input("Enter student first assignment marks out of 10: "))
    internal = int(input("Enter Internal Examination marks out of 10: "))
    attendance = int(input("Enter student attendance marks out of 10: "))
    quiz = int(input("Enter student quiz marks out of 10: "))
    group_project = int(input("Enter student group project marks: "))
    total = first_assignment + internal + attendance + quiz + group_project
    height = 595
    draw.text((401, height), str(first_assignment), "Black", font=font)
    draw.text((587, height), str(internal), "Black", font=font)
    draw.text((823, height), str(attendance), "Black", font=font)
    draw.text((1123, height), str(quiz), "Black", font=font)
    draw.text((1287, height), str(group_project), "Black", font=font)
    draw.text((1387, height), str(total), "Red", font=font)


def mobile_programming():
    print("Mobile Programming: ")
    first_assignment = int(input("Enter student first assignment marks out of 10: "))
    internal = int(input("Enter Internal Examination marks out of 10: "))
    attendance = int(input("Enter student attendance marks out of 10: "))
    quiz = int(input("Enter student quiz marks out of 10: "))
    group_project = int(input("Enter student group project marks: "))
    total = first_assignment + internal + attendance + quiz + group_project
    height = 671
    draw.text((401, height), str(first_assignment), "Black", font=font)
    draw.text((587, height), str(internal), "Black", font=font)
    draw.text((823, height), str(attendance), "Black", font=font)
    draw.text((1123, height), str(quiz), "Black", font=font)
    draw.text((1287, height), str(group_project), "Black", font=font)
    draw.text((1387, height), str(total), "Red", font=font)


if __name__ == '__main__':
    main()

