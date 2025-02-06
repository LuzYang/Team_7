Rakaranta UI
Team 7 
Team Members – 
i.	Ji Xing		- Project Manager 
ii.	Yang Yingying
iii.	Thanuja Mawela
iv.	Susan Pandey
v.	Sanjeev Chaudhary

Project Plan: Smart Reservation & Sensor Application System
1. Project Scope & Goals
This project focuses on developing an integrated reservation and sensor data management system. The key objectives are:
•	Cabin Reservation System: Integrate a reservation module into an existing public website, ensuring interoperability with other booking applications.
•	Customer Extranet: Develop a user-friendly platform for booking amenities like saunas, laundry rooms, and gyms.
•	Company Intranet: Provide internal stakeholders with access to sensor analytics, customer information, and reservation management tools.
•	Sensor Application Demos: Organize a hackathon to develop and showcase sensor applications for wood storage measurement, water leakage detection, and other innovative use cases.

2. Milestones & Deadlines
Milestone	Deadline
Define project requirements	Week 1
Research and select technologies	Week 2
Design system architecture	Week 3-4
Develop reservation system	Week 5-8
Develop customer extranet	Week 6-9
Implement company intranet	Week 7-10
Develop sensor applications	Week 8-11
Integrate and test components	Week 12-13
Hackathon for sensor applications	Week 14
Final testing and security audits	Week 15
Deployment and launch	Week 16


3. Team Roles & Responsibilities
•	Project Manager:  Oversee project timelines, coordination, and reporting.
•	All team members act as Developers, UI/UX Designers, Sensor Experts, QA Testers, Security Analysts and Hackathon Facilitators.
-	Developers: Implement reservation system, intranet, and extranet.
-	UI/UX Designers: Design user interfaces for accessibility and ease of use. 
-	Sensor Experts: Research and integrate sensor applications.
-	QA Testers: Ensure system reliability and security.
-	Security Analysts: Implement security protocols and ensure compliance.
-	Hackathon Facilitators: Organize and support student innovation.
4. Communication Tools & Platforms
•	Microsoft Teams, WhatsApp: Real-time communication and collaboration. Document storage and knowledge sharing.
•	GitHub: Version control and code repository.
5. Research Areas
Sensor Technologies: Investigate IoT devices for wood storage measurement, water leakage detection, etc.
i.	Measuring Firewood Volume (Using Depth Camera)
Requirement Description:
Use a depth camera to scan the firewood pile, build a 3D model, and calculate its volume.
Feasibility Analysis:
Depth cameras (such as Intel RealSense or similar devices) have 3D data capture capabilities, making them suitable for measuring the volume of irregularly shaped objects.
Computer vision techniques can process depth data to calculate the accumulated volume.
Data Analysis Methods: Explore analytics tools for reservation insights. 
Security Protocols: Define encryption and authentication mechanisms.



ii.	Measuring Firewood Weight (Using Integrated Floor Scale)
Requirement Description:
Install an integrated floor scale on the storage room floor to measure the total weight of the firewood pile in real time.
Feasibility Analysis:
Floor scales can provide high-accuracy real-time weight measurement, ideal for monitoring the weight of materials in a fixed storage environment.
Combined with volume measurement results, the average density of the firewood can also be calculated.
•	Steps:
1.	Device Installation:
Embed or place the floor scale on the storage room floor, ensuring its measurement capacity covers the maximum weight of the firewood pile.
2.	Data Collection:
Connect the floor scale to a data acquisition module to record weight changes in real time.
3.	Data Calibration:
Periodically check the accuracy of the floor scale and eliminate external interference (e.g., weight not related to firewood).
4.	Result Output:
Upload real-time weight data to the application.
iii.	Measuring Storage Room Humidity (Using Humidity Sensor)
Requirement Description:
Install humidity sensors inside the storage room to monitor changes in the storage environment's humidity in real time, and assess the moisture content of the wood.
Feasibility Analysis:
Humidity sensors are suitable for long-term monitoring of the storage room's humidity, which is closely related to changes in the wood's moisture content.
By using a relationship model between environmental humidity and wood moisture content, the moisture level of the firewood can be indirectly inferred.
•	Steps:
1.	Device Installation:
Select representative locations within the storage room to install humidity sensors, avoiding direct sunlight or interference from ventilation outlets.
2.	Data Collection:
Record the relative humidity (%RH) in the storage room in real time using the humidity sensors.
3.	Data Analysis:
Use historical humidity data from the storage room to predict trends in the wood's moisture content.
4.	Alarm Mechanism:
Set a humidity threshold (e.g., above 80%). If the humidity exceeds this level, automatically issue an alert.
5.	Result Output:
Output humidity data and calculated wood moisture content to the application.

6. Documentation & Development Setup
•	Document system requirements, user stories, and technical specifications.
•	Ensure development tools (IDEs, databases, cloud services) are installed and configured.
7. Testing & Quality Assurance
•	Unit Testing: Validate individual components.
•	Integration Testing: Ensure system modules interact correctly.
•	Security Testing: Conduct vulnerability assessments.
•	User Acceptance Testing: Collect feedback from end-users.
By following this structured plan, the project will ensure successful implementation and delivery within the set timeline.

