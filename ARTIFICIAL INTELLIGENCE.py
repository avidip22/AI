# QUESTION-1
# A class with 10 students wants to produce some information from the results of the four standard
# tests in Maths, Science, English and IT. Each test is out of 100 marks. The information output
# should be the highest, lowest and average mark for each test and the highest, lowest and average
# mark overall. Write a program in Python to complete this task.

#ANS

def calculate_statistics(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average

def main():
    num_students = 10
    tests = ['Maths', 'Science', 'English', 'IT']
    overall_scores = []

    for test in tests:
        test_scores = []
        for i in range(num_students):
            score = int(input(f"Enter {test} score for student {i+1}: "))
            test_scores.append(score)
            overall_scores.append(score)

        highest, lowest, average = calculate_statistics(test_scores)
        print(f"\n{test} Test:")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score: {lowest}")
        print(f"Average Score: {average:.2f}\n")

    overall_highest, overall_lowest, overall_average = calculate_statistics(overall_scores)
    print("Overall Results:")
    print(f"Highest Score: {overall_highest}")
    print(f"Lowest Score: {overall_lowest}")
    print(f"Average Score: {overall_average:.2f}")

if __name__ == "__main__":
    main()
