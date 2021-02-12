<h1 align = 'center'>Project 5: Washington, DC Public Schools</h1>
<h4 align = 'center'>AUTHORS</h4>
<center>John Bruscella, Keith Kruelskie, Rebecca Wright</center>

 <br><hr><br>

### Problem Statement
> Can we predict a school's STAR rating based on features relating to each school?

### Executive Summary
> This project aims to evaluate metrics used to evaluate schools in the DC Public School system.  Which factors had the biggest influence on DC public school STAR ratings?  What areas for improvement can be identified to better serve the educational needs of DC students.  Are there finfluencial factors that exist outside of those currently considered by the DC Board of Education in their current calculation model for STAR ratings?

### What ARE STAR Ratings?
> The STAR Framework provides an overall school performance rating from 1 to 5 stars based on an overall school performance score (with 1 STAR being the lowest and five being the highest). 
STAR calculates an overall school performance rating using measures of academic achievement, student growth, school environment, English language proficiency, and graduation rates for student groups in the school.
The STAR Framework first measures a school’s performance for all students for each of the applicable metrics and then measures performance for students with disabilities, students who are at-risk, English learners, and each racial/ethnic group in the school with more than ten students.
Schools that serve exclusively adults, exclusively students in grades PK3 thru grade 2, schools that are new, and schools that serve small numbers of students (below the threshold for student data privacy protections) do not receive STAR ratings. <br>
[*source*](https://edscape.dc.gov/sites/default/files/dc/sites/edscape/publication/attachments/EdScape%20Beta%20Chapter%204%20Summary%20for%20Download%20-%20December%202019%20updates.pdf "DC Public Education Landscape - page 4.15")

 <br><hr><br>

## File Directory / Table of Contents

1. Data folder
    - original_data
        * FY16_budget_school.xlsx
        * FY16_budgeted_erollment_school.xlsx
        * FY17_budget_allocation_school.xlsx
        * SY17-18 School Feeder Patterns.pdf
        * SY17-18_school_feeder.xlsx
        * SY18-19 School Feeder Patterns.pdf
        * SY18-19_school_feeder.xlsx
        * cluster_data_3.csv
        * cluster_student_counts.csv
        * distance_cluster_school-choice_SY16-19.xlsx
        * distance_school-choice_SY16-19.xlsx
        * distance_ward_school-choice_SY16-19.xlsx
        * enrollment_school_dcps.xlsx
        * enrollment_school_facility.xlsx
        * enrollment_school_facility_dcps.xlsx
        * school_attendance.xlsx
        * school_attendance_updated.xlsx
        * school_df_clean.csv
        * school_graduation_data.xlsx
        * schools_by_cluster.csv
        * schools_cleaned.xlsx
        * schools_w_cluster_data.csv
        * star_by_cluster.csv
        * ward_enrollment_distance_star-rating.xlsx
    - cleaned_data
        * school_df_v1.csv
        * school_df_v2.csv
        * school_df_v3.csv
        * school_df_v4.csv
        * school_df_v6.csv
        
        
2. Code folder
    - 01_creating_dataframes
        * create_school_df_v1.ipynb
        * create_school_df_v2.ipynb
        * create_school_df_v3.ipynb
    - 02_eda
        * 01_eda.ipynb
        * 02_supplemental_eda.ipynb
    - 03_modeling
        * a_regression_models_and_eval.ipynb
        * b_regression_models_2017-2018.ipynb
        * c_regression_models_2018-2019.ipynb
        * d_regression_models_mixed_years.ipynb
        * e_cluster_models.ipynb
        * f_neural_network.ipynb
    - 04_templated_codeblocks
        * code_snippets_group.ipynb


3. Figures folder
    - notebook_figures folder
        * contains archival plots and graphs generated during execution of EDA and modeling process
    - presentation_figures folder
        * contains plots and graphs utilized during project presentation


4. App folder
    - archive
    - assets
    - data
    - static
    - templates
    - app.py

 <br><hr><br>
 
### Data Dictionaries

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**code**|*float*|school_df_v6|School code|
|**name**|*object*|school_df_v6|School name| 
|**grade_band**|*object*|school_df_v6|School grades| 
|**enrollment_SY1718**|*float*|school_df_v6|Student enrollment 2017-2018| 
|**enrollment_SY1819**|*float*|school_df_v6|Student enrollment 2018-2019| 
|**star_score_SY1718**|*float*|school_df_v6|School star score 2017-2018| 
|**star_score_SY1819**|*float*|school_df_v6|School star score 2018-2019|
|**star_rating_SY1718**|*float*|school_df_v6|School star rating 2017-2018|
|**star_rating_SY1819**|*float*|school_df_v6|School star rating 2018-2019|
|**capacity_SY1718**|*float*|school_df_v6|School capacity 2017-2018|
|**capacity_SY1819**|*float*|school_df_v6|School capacity 2018-2019|
|**latitude**|*float*|school_df_v6|School latitude|
|**longitude**|*float*|school_df_v6|School longitude|
|**cluster**|*float*|school_df_v6|School cluster|
|**ward**|*float*|school_df_v6|School ward|
|**count_any_SY1819**|*float*|school_df_v6|count of students with any absences per school 2018-2019|
|**count_0_SY1819**|*float*|school_df_v6|count of students with zero absences per school 2018-2019|
|**pct_0_SY1819**|*float*|school_df_v6|percent student population with zero absences per school 2018-2019|
|**count_1-5_SY1819**|*float*|school_df_v6|count of students with 1-5 absences per school 2018-2019|
|**pct_1-5_SY1819**|*float*|school_df_v6|percent student population with 1-5 absences per school 2018-2019|
|**count_6-10_SY1819**|*float*|school_df_v6|count of students with 6-10 absences per school 2018-2019|
|**pct_6-10_SY1819**|*float*|school_df_v6|percent student population with 6-10 absences per school 2018-2019|
|**count_11-20_SY1819**|*float*|school_df_v6|count of students with 11-20 absences per school 2018-2019|
|**pct_11-20_SY1819**|*float*|school_df_v6|percent student population with 11-20 absences per school 2018-2019|
|**count_20+_SY1819**|*float*|school_df_v6|count of students with 20+ absences per school 2018-2019|
|**pct_20+_SY1819**|*float*|school_df_v6|percent student population with 20+ absences per school 2018-2019|
|**count_any_SY1718**|*float*|school_df_v6|count of students with any absences per school 2017-2018|
|**count_0_SY1718**|*float*|school_df_v6|count of students with zero absences per school 2017-2018|
|**pct_0_SY1718**|*float*|school_df_v6|percent student population with zero absences per school 2017-2018|
|**count_1-5_SY1718**|*float*|school_df_v6|count of students with 1-5 absences per school 2017-2018|
|**pct_1-5_SY1718**|*float*|school_df_v6|percent student population with 1-5 absences per school 2017-2018|
|**count_6-10_SY1718**|*float*|school_df_v6|count of students with 6-10 absences per school 2017-2018|
|**pct_6-10_SY1718**|*float*|school_df_v6|percent student population with 6-10 absences per school 2017-2018|
|**count_11-20_SY1718**|*float*|school_df_v6|count of students with 11-20 absences per school 2017-2018|
|**pct_11-20_SY1718**|*float*|school_df_v6|percent student population with 11-20 absences per school 2017-2018|
|**count_20+_SY1718**|*float*|school_df_v6|count of students with 20+ absences per school 2017-2018|
|**pct_20+_SY1718**|*float*|school_df_v6|percent student population with 20+ absences per school 2017-2018|
|**budgeted_amount_FY16**|*float*|school_df_v6|Monetary budgeted amount to school by District overall for fiscal year 2016|
|**budgeted_enrollment_FY16**|*float*|school_df_v6|Monetary budgeted amount to school by District based on enrollment for fiscal year 2016|
|**budgeted_amount_FY17**|*float*|school_df_v6|Monetary budgeted amount to school by District overall for fiscal year 2017|
|**budgeted_enrollment_FY17**|*float*|school_df_v6|Monetary budgeted amount to school by District based on enrollment for fiscal year 2017|
|**pct_meet_exceed_math_SY1718**|*float*|school_df_v6|avg percent students to meet/exceed expectation in math 2017-2018|
|**pct_meet_exceed_ela_SY1718**|*float*|school_df_v6|avg percent students to meet/exceed expectation in english 2017-2018|
|**pct_meet_exceed_math_SY1718**|*float*|school_df_v6|avg percent students to meet/exceed expectation in math 2018-2019|
|**pct_meet_exceed_ela_SY1718**|*float*|school_df_v6|avg percent students to meet/exceed expectation in english 2018-2019|

 <br><hr><br>
 
### Data Collection
> The majority of the data was collected from [OpenData DC](https://opendata.dc.gov/ "OpenData DC Portal") and the [District of Columbia Public Schools.](https://dcps.dc.gov/ "DCPS Portal")

### Data Cleaning
> * Schools were keyed primarily off of school_code, a unique identifier assigned to each school by the DC board of education.
> * School_code value used during merging of data sources into cleaned school dataframes.
> * Numpy infinite values were converted to numpy nan values.
> * Null values were initially replaced by -1 to prevent dtype conflict errors, and eventually converted back to NANs and/or fully dropped during modeling phase.

### EDA
> * Primary EDA examined distribution of schools by STAR rating using the following metrics:
>       - locations
>       - rates of absenteeism
>       - budgets
>       - enrollements
>       - capacities

> * Features were engineered from existing data to represent:
>       - percent of enrollment capacity filled
>       - percent of student population with certain amounts of truancy

> * Second phase EDA introduced comparative analysis on overall averaged student performance on standardized exams in the subjects of English Language Arts and Math.  Feature engineering was used to create single average values for school testing perfomances in each subject, isolating evaluations to the percentage of student who tested at the level of "at or exceeding expectations".

 <br><hr><br>

### Modeling
#### Null Model

>The null model for our dataset will be an accuracy of 32% as the most-frequent value in our target (star rating) is 3-stars and is approximately 32% of our target variable. The values in our target are as follows:
>- 1 Star: 13%
>- 2 Star: 26%
>- **3 Star: 32%**
>- 4 Star: 15%
>- 5 Star: 13%

>Our models incorperated data relating to enrollment numbers and school capacities, locations of schools, student truancy, budget amounts, and student standardized testing data. These features were used to predict the school star rating for 2017-2018 school year. We tried many different regression models but ultimately found the Ridge Model to most accurately predict our target variable.

>Models that performed well:
>- Ridge Model
>- Decision Trees
>- KNN
>- Random Forest Model
>- Neural Network

>Models that did not perform well:
>- Lasso Model
>- Elastic Net Modelnet_pipe
>- Bagging Regressor
>- Adaboost & Gradientboost
>- SVR

#### Ridge Model

>The Ridge Model performed the best of the models tested. The Ridge pipeline was built using standardScaler and gridsearched over alpha values and normalizeation on/off. The r2 value of this model was approximately 0.73 and it had a mean squared error of 0.66. We found this model to perform particularly well due to its added regularization and this model explained approximately 73% of the variabiliy in the data. During the modeling process, we found many of the models to have high variance and variability within the models. The Ridge model's default l2-regularization did well to help model this data.

#### Random Forest

>The Random Forest model also performed fairly well on our dataset and had an r2 value of 65% on the test set and an mse of 0.75. This model was fit in a pipeline and gridsearched over the parameters for n_estimators, 'criterion', min_samples_split, and ccp_alpha. This model was overfit as it had a higher r2 value for the training set than on the testing set. This model was also able to identify the overall trend in our data but did not perform as well as the Ridge Model.

#### Feature Importance
>When looking at the feature importance in the models, the best indicators of our model predicting well had to do with student testing schools, particularly 'percent of students who performed at or exceeding expectations' in the math and ELA standardized testing. This indicates how large of a role testing performance is weighted in determining a school's STAR rating. Attendance rates were also important features to consider in our model. In addition, school capacity and enrollment were not the best indicators of our model predicting well.

#### Future Work
>Additional modeling and research may increase the performance of the models after additional data is collected. Demographic and external factors that affect testing data, enrollment, and attendance may be interesting to look at in future work.

<br><hr><br>

### Interactive App
> The app is an extension of the EDA and a way to quickly visualize multiple graphs side by 
side, at the user's discretion along with an interactive choropleth overlay on the D.C.
region.
<br>
> The app was developed in Flask, and runs on a local server activated by the app.py file.
The app.py file draws its data from the school_df_v6.csv and cluster_map.csv file to 
populate the graphs and choropleth. Once a user has navigated to the app, a number of drop
downs control what each graph shows, and another dropdown controls the overlay on the D.C.
metro area.
<br>
> Clicking Update Dashboard refreshes the page with the new graphs and maps.
Future app integrations might include additional tooltips and data on the schools that 
populate on the map, and perhaps an interactive layer to allow for selection of
neighborhood clusters to look at data about the cluster in detail.

<br><hr><br>

### Conclusions and Recomendations
> While academic performance proved quite telling in the determination of a school’s STAR rating, we believe that school attendance is the key takeaway from our analysis.  The more a student is present in class, the higher their academic performance is expected to be.  If schools want to increase their STAR rating, which indicates that they have brought out a higher level of educational performance from their students, then care should be made in enacting initiatives to increase school attendance.

**Research on Existing Barriers to Student Attendance**  
> Students miss school for many reasons, and excessive absences may indicate deeper underlying issues. It’s been noted that common causes of absenteeism include student health (physical and mental), transportation, parent health, housing, academics, safety and childcare.  Further research into DC educational policy initiative shows that the DC department of Education as already taken a major interest in the issue of chronic absenteeism, beginning back in 2018.  Mayor Muriel Bowser of DC has an ongoing education initiative titled **“Student Attendance: Every Day Counts”**.  Information on this initiative and additional DC educational policy initiatives can be found through the main portal for DC Public Schools at https://dcps.dc.gov and through policy briefs on the DC Policy Center website at https://dcpolicycenter.org.

<br><hr><br>

### Sources
> **Star Calculations for DC Schools:** <br> https://osse.dc.gov/sites/default/files/dc/sites/osse/page_content/attachments/STAR%20Framework%20At-A-Glance_vFinal.pdf<br>
**EDScape:**<br>
https://edscape.dc.gov/<br>
**DC Neighborhoood Cluster Demographics**<br>
https://data.world/codefordc/dc-neighborhood-cluster-demographics<br>
**DCPS Attendance Reports:**<br>
https://dcps.dc.gov/publication/dcps-data-set-attendance<br>
**DCPS Enrollment Reports:**<br>
https://dcps.dc.gov/node/1018342<br>
**DCPS Student Readiness Exam Reports:**<br>
https://dcps.dc.gov/publication/dcps-data-set-parcc<br>
**EDScape Beta: DC Public Education Landscape (Dec 18, 2019)**<br>
https://edscape.dc.gov/sites/default/files/dc/sites/edscape/publication/attachments/EdScape%20Beta%20Chapter%204%20Summary%20for%20Download%20-%20December%202019%20updates.pdf