# DW_Challenge


### Project Structure

├── README.md          <- The top-level README for developers using this project.           
├── quickstart.py      <- quickstart guide for Gmail API                                    
├── credentials.json   <- aunthefication file for  API | not shared in GIT                  
├── token.json         <- aunthefication file for  API | not shared in GIT  
│                                                                                           
├── data                                                                                    
│   ├── external       <- Junior_DE_Task/    # task files for the challenge                
│   ├── downloaded     <- downloaded .csv files via Gmail API                                                 
│   └── processed      <- processed data                      
│                                                                                           
├── notebooks          <- Anya_DE.ipynb         # main notebook that calls functions from /src             
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
│   ├── api_functions.py           <-  functions for Gmail API                              
│   └── postgres_functions.py      <-  functions to manage postgres databases  
│                                                                                           
└── venvDE/            <- folder with virtual environment | not shared in GIT                       

### Installing development requirements
------------

    1. pip3 install -r requirements.txt
    2. follow steps to download aunthefication file with credentials from  https://developers.google.com/gmail/api/quickstart/python
    2a. rename the credentials file to credentials.json
    3. run script python3 quickstart.py to create token.json
    4. run Anya_DE.ipynb  as jupyter notebook to see my solutions 

### Challenges
    - setting up environment (choices of software for local setup. 
        Gmail API: 
            General info: (https://developers.google.com/gmail/api/guides) 
            Quick start: (https://developers.google.com/gmail/api/quickstart/go) 
        PostgreSQL local installation following (https://www.codecademy.com/article/installing-and-using-postgresql-locally) 
        Postgres app to build database: (https://postgresapp.com/) 
        PgAdmin (https://www.postgresql.org/ftp/pgadmin/pgadmin4/v7.1/macos/) )

    - Uploading data to Postgres database from csv file with columns containing commas
        Possible solutions: 
            1) with delimiter / format csv depending on version of postgres (I  have version 15) (https://stackoverflow.com/questions/10001651/importing-csv-with-commas-in-string-values) 

            2) upload full data without separation into columns and later split them (https://stackoverflow.com/questions/59588107/is-there-a-way-to-load-text-data-to-database-in-postgresql)

            3) use varchar format for exporting data from csv (https://www.google.com/amp/s/arctype.com/blog/import-data-postgres/amp/)
        solution 1) worked
    
    - Downloading attachments from email using Gmail API
        Problem: 
            When emails were sent using Mac native Mail agent with security signature, Gmail Api could only download smime.p7s attachment instead of real ones.
        Solution: 
            I sent emails from other mailbox to dwdechallenge@gmail.com and attachments became available

    - Unpacking json in column post_video_view_time_by_age_bucket_and_gender
        Problem: could not use apply solutions found on internet to the data (i.e. https://ftisiot.net/postgresqljson/how-to-extract-field-from-json-postgresql/ )

### Further Ideas
    - exploratory data analysis could be expanded endlessly, I focused only on video 

### References

project structure is based on [Cookiecutter project](http://drivendata.github.io/cookiecutter-data-science/)