# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

The final dashboard is deployed on Heroku [here](https://volunteer-covid-clinical-trial.herokuapp.com/).

## Dashboard Description

This dashboard summarizes and re-categorizes the information of 1266 on-going clinical trials related to COVID-19 treatment across the United States till April 26th 2021. The pie chart displays the percentage and number of clinical trails related to Covid diseases by city using certain criterias. Meanwhile, detailed information about the reference number, recruiting status, study topic, location authority and link is shown in the following table.

The main motivations for this dashboard is to:
 - Provide an easy-to-access pathway for people who are willing to be volunteers for COVID-19 clinical trial  to search recruiting information filtered by location, gender and clinical phase and finally help them to make the best decision.
and also can give an overview about how the research process of the clinical trials is going and which city is conducting heavy clinical trials. 

### Data Sources

- Data is collected from this [website](https://clinicaltrials.gov/) which is supporting to download csv file directly. 
- The dataset includes 1266 studies originally and in the 7625 rows of data are taking into analyzed due to complex location information. Cities,states and authorities are combined in location column and there are multiple combined locations which make sense because some clinical trials are collaborated across multiple companied and universities or even across countries. So location data cleaning is through the following way:
   1. Split multiple combined locations into separated ones and then split the city, state and authority within each location.
   2. Countries outside the America are excluded since the dashboard visualization is only about local conutry. 
   3. Each clinical trial may take count more than once due to collaboration.
- Missing values are detected in column Phase which represents the process of the clinical trial. Some trials don't split into diffrent phases, so we replace the null value with no defined phase.
- Recategorize the 12 kinds of recruting status information into 3 mains ( recruiting, potential recruiting and no recruiting) based on the recruiting status explanation from the website.
- All codes work analysis is based on cleaned pickle file.

### Further study
- Add the clickable link to each row of data to become more user friendly.
- Extract more data such as the specific category for each clinical study and provide the rough direction of the most recent clinical studies.
- Visualize the total number of each state, city and authority to which one is in the top level of research.

