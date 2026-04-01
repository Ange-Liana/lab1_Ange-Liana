import csv
import sys
import os

def load_csv_data():
    # ask user for the file name to process
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    # check if the file actually exists before trying to open it
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        # open the file and read each row as a dictionary
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # convert score and weight into numbers so we can calculate with them
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        # handle any unexpected issue when reading the file
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")
    
    # handle case where file is empty
    if not data:
        print("No data found.")
        return
    
    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    
    total_grade = 0
    formative_total = 0
    summative_total = 0
    
    failed_formatives = []
    
    # go through each assignment and process values
    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']
        
        # make sure score is within valid range
        if score < 0 or score > 100:
            print("Invalid score detected.")
            return
        
        total_weight += weight
        
        # separate logic depending on assignment type
        if group == "Formative":
            formative_weight += weight
            formative_total += score * (weight / 100)
            
            # track failed formative assignments
            if score < 50:
                failed_formatives.append(item)
                
        elif group == "Summative":
            summative_weight += weight
            summative_total += score * (weight / 100)
    
        # accumulate overall grade
        total_grade += score * (weight / 100)
    
    # validate weight distribution rules
    if total_weight != 100 or formative_weight != 60 or summative_weight != 40:
        print("Invalid weight distribution.")
        return
    
    # compute category percentages
    formative_percent = (formative_total / formative_weight) * 100 if formative_weight else 0
    summative_percent = (summative_total / summative_weight) * 100 if summative_weight else 0
    
    # calculate GPA based on final grade
    gpa = (total_grade / 100) * 5.0
    
    # determine final result
    status = "PASSED" if formative_percent >= 50 and summative_percent >= 50 else "FAILED"
    
    print(f"Final Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")
    
    # if failed, suggest which formative assignments can be redone
    if status == "FAILED" and failed_formatives:
        max_weight = max(item['weight'] for item in failed_formatives)
        resubmit = [item['assignment'] for item in failed_formatives if item['weight'] == max_weight]
        
        print("Resubmission Assignments:")
        for r in resubmit:
            print(r)

if __name__ == "__main__":
    # load data from file
    course_data = load_csv_data()
    
    # evaluate and display results
    evaluate_grades(course_data)
