# DW_Challenge


### Project Structure

├── README.md          <- The top-level README for developers using this project.           
├── quickstart.py      <- quickstart guide for Gmail API                                    
├── credentials.json   <- aunthefication file for  API | not shared in GIT                  
├── token.json         <- aunthefication file for  API | not shared in GIT                   
├── data                                                                                    
│   ├── external       <- Junior_DE_Task/    # task files for the challenge                
│   ├── downloaded     <- downloaded .csv files via Gmail API                                                 
│   └── processed      <- The final, canonical data sets for modeling.                      
│                                                                                           
├── notebooks          <- Anya_DE.ipynb         # main notebook with solutions              
│                      <- Anya_DE_draft.ipynb   # drafts                                    
│                      <- SQL_query             # SQL scripts                               
│                                                                                           
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.                      
│   └── figures        <- Generated graphics and figures to be used in reporting            
│                                                                                           
├── requirements.txt   <- The requirements file for reproducing the analysis environment,   
│                         generated with `pip freeze > requirements.txt`                    
│                                                                                           
│── src                <- Source code for use in this project.                              
│   ├── api_functions.py           <- Scripts for Gmail API                              
│   └── postgres_functions.py      <- Scripts to manage postgres databases  
│                                                                                           
└── venvDE/            <- filder with environment (not shared in GIT)                       

### Installing development requirements
------------

    1. pip3 install -r requirements.txt
    2. follow steps to download aunthefication file with credentials from  https://developers.google.com/gmail/api/quickstart/python
    2a. rename the credentials file to credentials.json
    3. run script python3 quickstart.py to create token.json
    4.

### References

project structure is based on [Cookiecutter project](http://drivendata.github.io/cookiecutter-data-science/)