package main

import (
	"database/sql"
	"fmt"
	"strings"

	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "admin"
	password = "Admin123!"
	dbname   = "sales_models"
)

func main() {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	//defer db.Close()

	var id string
	var col1 string
	var col2 string

	sql1 := "SELECT * from rsm_country;"
	rows, err := db.Query(sql1)
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	//check columns
	columnNames, err := rows.Columns()
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	println("Column names :" + strings.Join(columnNames, " "))

	for rows.Next() {
		err = rows.Scan(&id, &col1, &col2)
		if err != nil {
			panic(err)
		}
		fmt.Println(id)
		fmt.Println(col1)
	}
	err = rows.Err()
	if err != nil {
		panic(err)
	}

}
