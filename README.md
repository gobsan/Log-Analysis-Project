
# Log analysis project

Internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install psycopg2.

```bash
pip install psycopg2


```Postgresql
Download databse file from (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Attach newsdata.sql to your database

## Usage

```python
import psycopg2

connection = psycopg2.connect(user="user name",
                                  password="password",
                                  host="host adress",
                                  port="port number",
                                  database="Database Name")

