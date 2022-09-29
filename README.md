# Automated Code Review Feedback Generator
A streamlit webapp that automatically grades student submissions out of 10 and provides relevant feedback.


### Diagrammatic Overview

![image](https://user-images.githubusercontent.com/77835877/193010934-8b6e6443-5413-4941-9744-5ce0b79e1734.png)


### Dataset and Feature Extraction

* [Original Dataset Link](https://figshare.com/articles/dataset/_5_Million_Python_Bash_Programming_Submissions_for_5_Courses_Grades_for_Computer-Based_Exams_over_3_academic_years_/12610958?file=23681627)
* Four programming tasks (Selection Sort, First Negative Element in a list, Largest Element in a list, Unique Character Count) were selected from the dataset mentioned above. The submissions were not graded - hence it required annotation of scores for each submission.
* 120 program submissions for each programming task were graded manually out of 10 to get the final annotated dataset which can be found in the folder 'Data'.
* Multiple features were extracted for each program submission either from direct source code or from AST representation of source code.
* The 'ast' module in python was used to extract features from ast representation of the source code.
* Some of the features extracted from direct source code:
  * loop    - Count of ’for’ and ’while’ loops in the code
  * cond    - Count of conditional operators in the code
  * arith   - Count of arithmetic operators in the code
  * assign  - Count of assignment operators in the code
* Some of the features extracted from AST representation of source code:
  * #fun    - Count of function definitions in the code
  * #fcall  - Count of function calls in the code
  * globals - Count of globals variables in the code
  * #lst    - Count of lists and tuples in the code
* For each task only best features are based on how well they are correlated with the target variable. F-statistic was used.

### Machine Learning models

* Three models were trained for each programming task dataset. The models were
  * Support Vector Regressor
  * Multi Layer Perceptron Regressor
  * Random Forest Regressor
* It was found that Random Forest Regressor outperforms the other two models overall.

### Feedback Generation 

#### Golden Feature Vector
* Programs with a score of 10 are considered as ’excellent’ programs.
* The average feature vector of the excellent programs is computed and is called as the ’Golden Feature Vector’.

#### Automatic Grading and Personalised Feedback
* After feature extraction, the regression model outputs a score out of 10.
* If score is lesser than 10, feedback is provided.
* A particular feature value x of the program’s feature vector is replaced with the corresponding feature X of golden vector and is fed back to the model.
* If the model outputs a better score and
  * if x > X : Feedback to increase that particular feature is advised.
  * if x > X : Feedback to decrease that particular feature is advised.
* The process is repeated for all features in the feature vector.

Results:

![image](https://user-images.githubusercontent.com/77835877/193029377-17ea839b-2c3c-470b-9f70-c887766c4067.png)

 






### Executing the Source Code

  * Streamlit installation: pip install streamlit
  
  * Pandas installation: pip install pandas
  
  * Scikit-learn installation: pip install scikit-learn
  
  * Clone this repository or download zip and extract the files.

  * Open terminal and move to the directory where 'app.py' is located.

  * Now, run the command 'streamlit run app.py'.

  * The student code submission portal web app will be available at port 8501 ( http://localhost:8501/ ).
  
  * Signup with a username and password and then login.
  
  * Select the task you would want to attempt and submit code following the hints and instructions.
  
  * Score and relevant feedback will be generated.
  * There is also provision to view best program submission for each task.
  
  ### Sample
  
  #### Sample code submission and feedback for selection sort
  
  ![image](https://user-images.githubusercontent.com/77835877/193031145-abbbb254-8ad5-48ea-a829-c05a987f4d73.png)

 #### Sample best code submission
 
 ![image](https://user-images.githubusercontent.com/77835877/193031533-9dd16810-e809-408b-82a0-72d4ebb95314.png)

