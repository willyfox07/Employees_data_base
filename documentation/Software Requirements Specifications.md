# Employee Manager

## Vision

"Employee Manager" is a web application designed for the management of employees and departments with these employees.

Application should provide:

- Storing information about employees in a database;
- Display list of employees;
- Updating list of employees(adding,editing,removing);
- Display list of departments;
- Updating list of depatrments(adding,editing,removing);
- Filtering by departments for employees;
- Filtering by date of birth for employees;

## 1.Employees

### 1.1 Display list of employees

The mode is designed to view the list of employees.

**Main scenario**

- User select item "Employees";
- Application displays list of Employees.

![Main menu](/documentation/image/Start.png)
Pic.1.1 View the list of employees.

**The list displays the following columns:**

- Name - Name of employees;
- Surname - Surname of employees;
- Hiring date - date when employee was hired;
- Position held - what position employee does;
- Department - which department does the employee belong to.

**Filtering by date:**

- In the list of employees mode, the user sets a date filter and presses the refresh list button

### 1.2 Add employee

**Mais scenario:**

- User clicks the "Add" button in the list of employees view mode;
- Application displays form to enter data about employee;
- User enters data about employee and presses "Save" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is additing to database;
- If error occurs, then error message is displaying;
- If new data about employee is succesfully added, then list of employees with added records is displaying.

**Add error scenario:**

- User clicks the “Add” button in the list of employee view mode;
- Application displays form to enter employee data;
- User enters employee data and presses "save" button;
- The new entered employee data are compared with the existing ones,if the employee's data entered already exists in the database, a pop-up window for adding error and asking you to enter new correct data, entered data is not saved.

![add_error](/documentation/image/error_adding_employee.png)

**Cancel operation scenario:**

- User clicks the “Add” button in the list of employee view mode;
- Application displays form to enter employee data;
- User enters employee data and presses “Cancel” button;
- Data don’t save in data base, then list of employees records is displaying to user.
- If the user selects the menu item "EMployees”, ”Departments”, the data will not be saved to the database and the corresponding form with updated data will be opened.

![Add employee](/documentation/image/add_employee.png)

**When adding a employee, the following details are entered:**

- Employee name;
- Employee surname;
- Hiring date - date when employee was hired;
- Position held - what position employee does;
- Department - which department does the employee belong to.

### 1.3 Edit employee

**Main scenario:**

- User clicks the "Edit" button in the employee list view mode;
- Application displays form to enter employee data;
- User enters employee data and presses "Cancel" button;
- Data don't save in data base, then list of employees records is displaying to user;
- If the user select the menu item "Employees", "Departments", the data will not be saved to the database and the corresponding form with updated data will be opened.

**Edit error scenario:**

- User clicks the “Edit” button in the list of employee view mode;
- Application displays form to edit employee data;
- If new entered data is incorrect, a pop-up window for editing error and asking you to enter new correct data, edited data is not saved.

![edit_error](/documentation/image/error_edit_employee.png)

**Cancel operation scenario:**

- User clicks the “Edit” button in the employee list view mode;
- Application displays form to enter employee data;
- User enters employee data and presses “Cancel” button;
- Data don’t save in data base, then list of employee records is displaying to user.
- If the user selects the menu item "Employees”, ”Departments”, the data will not be saved to the database and the corresponding form with updated data will be opened.

![Edit employee](/documentation/image/edit_employee.png)

**When editing a employee, the following details are entered:**

- Employee name;
- Employee surname;
- Hiring date - date when employee was hired;
- Position held - what position employee does;
- Department - which department does the employee belong to.

**Constrains for data validation:**

- Employee name - maximum length of 90 characters;
- Employee surname - maximum length of 90 characters;
- Hiring date - format dd/mm/yyyy;
- Position held - maximum length of 90 characters;
- Department - maximum length of 90 characters.

### 1.4 Removing employee

**Main scenario:**

- The user, while in the list of employees, presses the "Delete" button in the selected employee line;
- If the employee can be removed, a confirmation dialog is displayed;
- The user confirms the removal the employee;
- Record is delected from database;
- If error occurs, then error message displays;
- If employee data is succesfully deleted, then list of employee without delected data is displaying.

![Edit employee](/documentation/image/delete_order.png)

**Cancel operation scenario:**

- User in display mode of employees list and press "Delete" button;
- Application displays confirmation dialog "Please confirm ";
- User press "Cancel" button;
- List of employees without changes is displaying.

## Departments

### 2.1 Display list of Departments

This mode is intended for viewing and editing the departments list.

**Main scenario:**

- User selects item "Departments";
- Application displays list of departments;

![Edit department](/documentation/image/Departments.png)

**The list displays the following columns:**

- Department - department name;
- The number of employees - how mane employees in this dapetment;
- Head - head of department;
- Location - where this department located.

**Filtering by location:**

- In the clients list view mode, the user sets a location filter and presses the refresh list button.

**Filtering by number of employees:**

- In the clients list view mode, the user sets  the range from minimum to maximum number of employees and presses the refresh list button.

### 2.2 Add department

**Main scenario:**

- User clicks the "Add" button in the list of departments view mode;
- Application displays form to enter data about department;
- User enters data about department and presses "Save" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is additing to database;
- If error occurs, then error message is displaying;
- If new data about department is succesfully added, then list of department with added records is displaying.

**Cancel operation scenario:**

- User clicks the “Edit” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Cancel” button;
- Data don’t save in data base, then list of department records is displaying to user.
- If the user selects the menu item "Employees”, ”Departments”, the data will not be saved to the database and the corresponding form with updated data will be opened.

![add department](/documentation/image/add_department.png)

**Add error scenario:**

- User clicks the “Add” button in the list of department view mode;
- Application displays form to enter department data;
- User enters department data and presses "save" button;
- The new entered department data are compared with the existing ones,if the departments data entered already exists in the database, a pop-up window for adding error and asking you to enter new correct data, entered data is not saved.

![add_error](/documentation/image/error_add_department.png)

**When adding a department, the following details are entered:**

- Department;
- Number of employees - how many people work in the department;
- Head -  head of department;
- Location - where this department located.

**Constrains for data validation:**

- Department - maximum length for 45 characters;
- Number of employees - maximum length for 30 characters;
- Head - maximum length for 45 characters;
- Location - maximum length for 45 characters;

### 2.3 Edit department

**Main scenario:**

- User clicks the "Edit" button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses "Cancel" button;
- Data don't save in data base, then list of department records is displaying to user;
- If the user select the menu item "Employees", "Departments", the data will not be saved to the database and the corresponding form with updated data will be opened.

**Cancel operation scenario:**

- User clicks the “Edit” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Cancel” button;
- Data don’t save in data base, then list of department records is displaying to user.
- If the user selects the menu item "Employees”, ”Departments”, the data will not be saved to the database and the corresponding form with updated data will be opened.

![Edit department](/documentation/image/edit_department.png)

**Edit error scenario:**

- User clicks the “Edit” button in the list of employee view mode;
- Application displays form to edit department data;
- If new entered data is incorrect, a pop-up window for editing error and asking you to enter new correct data, edited data is not saved.

![edit_error](/documentation/image/edit_error_department.png)

### 2.4 Removing department

**Main scenario:**

- The user, while in the list of department, presses the "Delete" button in the selected department line;
- If the department can be removed, a confirmation dialog is displayed;
- The user confirms the removal the department;
- Record is delected from database;
- If error occurs, then error message displays;
- If department data is succesfully deleted, then list of department without delected data is displaying, also in list of employees all data about the remote department will be deleted.


![Delete department](/documentation/image/delete_department.png)

**Cancel operation scenario:**

- User in display mode of department list and press "Delete" button;
- Application displays confirmation dialog "Please confirm ";
- User press "Cancel" button;
- List of department without changes is displaying.
