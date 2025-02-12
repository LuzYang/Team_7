-- Step 1: Create Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY ,
    DepartmentName VARCHAR(100) NOT NULL
);

-- Step 2: Create Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY ,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Step 3: Insert Sample Data into Departments
INSERT INTO Departments (DepartmentID,DepartmentName) VALUES 
(1,'Human Resources'),
(2,'IT'),
(3,'Finance');

-- Step 4: Insert Sample Data into Employees
INSERT INTO Employees (Name, Email, DepartmentID) VALUES 
('Alice Johnson', 'alice.johnson@example.com', 1),
('Bob Smith', 'bob.smith@example.com', 2),
('Charlie Brown', 'charlie.brown@example.com', 3),
('Diana Prince', 'diana.prince@example.com', 2);

-- Step 5: Retrieve Employees with Their Department Names
SELECT *FROM Employees;

