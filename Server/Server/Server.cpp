// Server.cpp : Defines the entry point for the console application.
// Author: Lei Wang (Wilson)
// Created on: 1.18.2018

#include "stdafx.h"
#include <iostream>
#include <windows.h>
#include <sql.h>
#include <sqltypes.h>
#include <sqlext.h>
#include <string>
#include "User.h"
#include "Info_Exchange.h"


int main()
{
	User *newUser = new User();
	User *newUser2 = new User("Admin", "Wilson");
	std::string name = newUser2->getUserName();
	newUser2->updateQuery("New query");


	std::cout << name << std::endl;

	delete newUser;
	delete newUser2;


    #define SQL_RESULT_LEN 240
    #define SQL_RETURN_CODE_LEN 1000

	//define handles and variables
	SQLHANDLE sqlConnHandle;
	SQLHANDLE sqlStmtHandle;
	SQLHANDLE sqlEnvHandle;
	SQLWCHAR retconstring[SQL_RETURN_CODE_LEN];

	//initializations
	sqlConnHandle = NULL;
	sqlStmtHandle = NULL;

	//allocations
	if (SQL_SUCCESS != SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &sqlEnvHandle))
		goto COMPLETED;

	if (SQL_SUCCESS != SQLSetEnvAttr(sqlEnvHandle, SQL_ATTR_ODBC_VERSION, (SQLPOINTER)SQL_OV_ODBC3, 0))
		goto COMPLETED;

	if (SQL_SUCCESS != SQLAllocHandle(SQL_HANDLE_DBC, sqlEnvHandle, &sqlConnHandle))
		goto COMPLETED;

	//output
	std::cout << "Attempting connection to SQL Server...";
	std::cout << "\n";

	//connect to SQL Server	
	//I am using a trusted connection and port 14808
	//it does not matter if you are using default or named instance
	//just make sure you define the server name and the port
	//You have the option to use a username/password instead of a trusted connection
	//but is more secure to use a trusted connection
	switch (SQLDriverConnect(sqlConnHandle,
		NULL,
		(SQLWCHAR*)L"DRIVER={SQL Server};SERVER=localhost, 1433;DATABASE=master;UID=sa;PWD=Wilson;",
		//(SQLWCHAR*)L"DRIVER={SQL Server};SERVER=localhost, 1433;DATABASE=AKI;Trusted=true;",
		SQL_NTS,
		retconstring,
		1024,
		NULL,
		SQL_DRIVER_NOPROMPT)) {

	case SQL_SUCCESS:
		std::cout << "Successfully connected to SQL Server";
		std::cout << "\n";
		break;

	case SQL_SUCCESS_WITH_INFO:
		std::cout << "Successfully connected to SQL Server";
		std::cout << "\n";
		break;

	case SQL_INVALID_HANDLE:
		std::cout << "Could not connect to SQL Server: SQL_INVALID_HANDLE";
		std::cout << "\n";
		goto COMPLETED;

	case SQL_ERROR:
		std::cout << "Could not connect to SQL Server: SQL_ERROR";
		std::cout << "\n";
		goto COMPLETED;

	default:
		break;
	}

	//if there is a problem connecting then exit application
	if (SQL_SUCCESS != SQLAllocHandle(SQL_HANDLE_STMT, sqlConnHandle, &sqlStmtHandle))
		goto COMPLETED;

	//output
	std::cout << "\n";
	std::cout << "Executing T-SQL query...";
	std::cout << "\n";

	//if there is a problem executing the query then exit application
	//else display query result
	if (SQL_SUCCESS != SQLExecDirect(sqlStmtHandle, (SQLWCHAR*)L"SELECT @@VERSION", SQL_NTS)) {
		std::cout << "Error querying SQL Server";
		std::cout << "\n";
		goto COMPLETED;
	}
	else {

		//declare output variable and pointer
		SQLCHAR sqlVersion[SQL_RESULT_LEN];
		SQLINTEGER ptrSqlVersion;

		while (SQLFetch(sqlStmtHandle) == SQL_SUCCESS) {

			SQLGetData(sqlStmtHandle, 1, SQL_CHAR, sqlVersion, SQL_RESULT_LEN, &ptrSqlVersion);

			//display query result
			std::cout << "\nQuery Result:\n\n";
			std::cout << sqlVersion << std::endl;
		}
	}

	//close connection and free resources
    COMPLETED:
	    SQLFreeHandle(SQL_HANDLE_STMT, sqlStmtHandle);
	    SQLDisconnect(sqlConnHandle);
	    SQLFreeHandle(SQL_HANDLE_DBC, sqlConnHandle);
	    SQLFreeHandle(SQL_HANDLE_ENV, sqlEnvHandle);

	//pause the console window - exit when key is pressed
	std::cout << "\nPress any key to exit...";
	getchar();

	return 0;
}

