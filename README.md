# student-grades-analyzer

This code is a simple student performance analysis program that calculates subject-wise statistics, determines the average score for each student, and assigns a pass or fail result based on the average score.

# Approach
The code uses pandas to create a DataFrame with student data and performs various operations on it. The approach involves:

1. Data Creation: Creating a DataFrame with student data, including names and scores in different subjects.
2. Subject-wise Analysis: Calculating and printing the average, highest, and lowest scores for each subject.
3. Average Score Calculation: Calculating the average score for each student and assigning it to a new column "Average" in the DataFrame.
4. Top 3 Students: Sorting the DataFrame by the "Average" column in descending order and printing the top 3 students with their average scores.
5. Pass/Fail Result: Assigning a pass or fail result to each student based on their average score, with a threshold of 40.

# How to Run
1. Save the code in a file named student_performance_analysis.py.
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the program using the command python student_performance_analysis.py.

# Example Input/Output
The code generates the following output:


=== Student Dataset ===
  Name  Math  Science  English
0    A    78       65       89
1    B    90       70       60
2    C    45       35       55
3    D    80       92       88
4    E    55       60       50

=== Subject-wise Analysis ===
Math -> Avg: 69.60, High: 90, Low: 45
Science -> Avg: 64.40, High: 92, Low: 35
English -> Avg: 68.40, High: 89, Low: 50

=== Top 3 Students by Average Score ===
  Name  Average
1    B    73.33
0    A    77.33
3    D    86.67

=== Final Student Data with Result ===
  Name  Math  Science  English  Average Result
0    A    78       65       89    77.33   Pass
1    B    90       70       60    73.33   Pass
2    C    45       35       55    45.00   Pass
3    D    80       92       88    86.67   Pass
4    E    55       60       50    55.00   Pass


# Challenges Faced
1. Data Manipulation: One of the challenges faced was manipulating the DataFrame to calculate the average score for each student and assign a pass or fail result.
2. Sorting and Indexing: Another challenge was sorting the DataFrame by the "Average" column and indexing the top 3 students.

Overall, this project demonstrates the use of pandas to analyze student performance data and provide insights into student achievement.
