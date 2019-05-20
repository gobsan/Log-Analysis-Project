
# Log analysis project

Internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Questions
1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
1. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
1. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
## Used Tools
1. Python 3.7.3
1. PostgresSQL
## Download The Data
1. Download the database file from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.
1. Unzip the data to get the newsdata.sql file.
## Import The Data
1. Using PostgresSQL create new database and name it *"news"*
1. Use `psql -d news -f newsdata.sql` command to import data to PostgressSQL 

## Database Structure
The databse contains the following three tables: 
1. **articles** - contains every author's articles.  
1. **authors** - contains all author's information.
1. **log** - contains all recieved requests to the site.

## Code Design
1. `import psycopg2` imports DB API to connet to PostgresSQL
