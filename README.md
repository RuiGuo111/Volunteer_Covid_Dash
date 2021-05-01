# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

The final dashboard is deployed on Heroku [here](https://volunteer-covid-clinical-trial.herokuapp.com/).

## Dashboard Description

This dashboard summarizes and re-categorizes the information of 1266 on-going clinical trials related to COVID-19 treatment across the United States till April 26th 2021. The pie chart displays the percentage and number of clinical trails related to Covid diseases by city using certain criterias. Meanwhile, detailed information about the reference number, recruiting status, study topic, location authority and link is shown in the following table.

The main motivations for this dashboard is to:
 - Provide an easy-to-access pathway for people who are willing to be volunteers for COVID-19 clinical trials to search recruiting information filtered by location, gender and clinical phase and help them to make the best decision.
 - Give an overview about how the research process of the clinical trials is going and which cities/states/compan/universities are conducting heavy clinical trials. 

### Data Sources

- Data is collected from this [website](https://clinicaltrials.gov/) which is supporting to download csv file directly. 
- 7625 observations are extracted from 1266 studies because of the complexity of the location information. Multiple pairs of cities, states and authorities are stacked in one column which can be explained that some clinical trials are collaborated across multiple companies and universities or even across countries. So the location data is cleaned  through the following approach:
   1. Seperate multiple combined locations into individual location shown as multiple rows and then split the city, state and authority information into 3 new columns within each row.
   2. Countries outside U.S. are excluded since the dashboard visualization is only focus on local country. 
- Missing values are detected in column Phase which represents the process of the clinical trial. Some trials don't split into single phase, so we replace the null value with no defined phase.
- Recategorize the 12 kinds of recruting status information into 3 main category including recruiting, potential recruiting and no recruiting based on the recruiting status explanation from the website.
- All codes work is based on cleaned pickle file.

### Further study
- Be more user-friendly by creating the clickable link for each row.
- Dig more data such as the specific disease category for each clinical study and forecast the hottest research direction of clinical studies in post COVID19 times.
- Visualize the total number of each state, city and authority to compare which one has more interest on research.

