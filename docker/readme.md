Get the mysql image
`docker pull mysql`

Run it - create a container using the mysql image
`docker run --name cs415-mysql -e MYSQL_ROOT_PASSWORD=mysqlPass -dp 3306:3306 mysql`

Command line from Docker:
- In Docker Desktop go to running container and under container actions select "open in terminal"

- At terminal prompt type
`mysql -pmysqlPass`

Run Commands from own terminal:
- At your local terminal type:
`docker exec -it cs415-mysql mysql mysql -pmysqlPass`

Now you are in the mysql command interface

1. create the database
2. create the api user
3. create the tables
4. add data to the tables