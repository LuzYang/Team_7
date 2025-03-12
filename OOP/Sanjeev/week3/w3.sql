-- Creating Equipment Table
CREATE TABLE Equipment (
    equipment_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    model NVARCHAR(100),
    manufacturer NVARCHAR(255),
    purchase_date DATE
);

-- Creating Maintenance Table
CREATE TABLE Maintenance (
    maintenance_id INT IDENTITY(1,1) PRIMARY KEY,
    equipment_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    description NVARCHAR(MAX),
    cost DECIMAL(10,2),
    technician NVARCHAR(255),
    next_due_date DATE,
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id) ON DELETE CASCADE
);

-- Inserting Sample Data into Equipment Table
INSERT INTO Equipment (name, model, manufacturer, purchase_date)
VALUES 
    ('Air Compressor', 'AC-500', 'Atlas Copco', '2022-05-15'),
    ('CNC Machine', 'CNC-X200', 'Haas Automation', '2021-08-10'),
    ('Forklift', 'FL-3000', 'Toyota', '2020-11-20');

-- Inserting Sample Data into Maintenance Table
INSERT INTO Maintenance (equipment_id, maintenance_date, description, cost, technician, next_due_date)
VALUES 
    (1, '2023-06-01', 'Oil change and filter replacement', 150.00, 'John Doe', '2024-06-01'),
    (2, '2023-09-15', 'Software update and calibration', 300.00, 'Jane Smith', '2024-09-15'),
    (3, '2023-12-10', 'Battery replacement and safety check', 500.00, 'Mike Johnson', '2024-12-10');
