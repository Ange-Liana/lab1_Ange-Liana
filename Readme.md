This Lab1 project is a Python-based application that is executed together with a bash script to evaluate, process, and manage students’ grades. The system reads data from a CSV file(grades.csv), hence evaluating a student’s performance based on certain guidelines, and immediately automates the organization of a file through archiving and logging using the organizer.sh script. 

How to run the Python application: 
           1. The CSV file grades.csv has to be in the same directory as the Python file       grade-evaluator.py
2. In the terminal, run the command python3 grade-evaluator.py or python grade-evaluator.py
3. The prompt requires you to enter a file name, and that is grades.csv

Expected output: The student’s final grade, GPA, and status. For instance, passed, failed,..

How to run the bash script:

First, the script must be made executable using the command chmod +x organizer.sh
Then run the script using the command  ./organizer.sh 

Expected output: The bash script archives the current CSV file,  automatically creates a new and empty one, and also logs the operation.

For better testing:

One can use different datasets in a CSV file to test error handling and valid and invalid inputs.
Run the bash script to check if logs are appended, a new CSV file is created, i.e., emptying the current CSV file, and that files are created in the archive folder

Features of the Python application grade-evaluator.py

Validating the scores that are within the range of 0 to 100
Ensuring that formatives and summatives are 60 and 40, respectively, making it a sum of 100.
Identifying and determining the assignments that are suitable for retake and resubmission.
Calculating the final grade and GPA of the student, as well as determining the status of the student, according to the academic performance.

Features of the bash script organizer.sh

Renaming and moving the already existing grades.csv using the timestamp
Creating an archive directory if it doesn’t exist 
After archiving, a new and empty grades.csv file is created
All operations are logged in organizer.log for proper tracking



