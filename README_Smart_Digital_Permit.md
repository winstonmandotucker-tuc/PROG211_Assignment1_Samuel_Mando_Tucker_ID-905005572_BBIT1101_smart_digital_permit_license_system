# Smart Digital Permit and License Management System

## Overview
The Smart Digital Permit and License Management System is a simple console-based Python application developed for the PROG211 Object-Oriented Programming 1 assignment.

The system demonstrates how Object-Oriented Programming (OOP) can be used to solve a real-world government-related problem. It allows permit and license applications to be created, stored, searched, displayed, approved, or rejected.

## Project Domain
**Government**

## Main Features
- Submit a new permit or license application
- Record citizen information
- Select a permit or license type
- Automatically generate a unique application ID
- Search for an application by ID
- Update an application status
- Approve or reject an application
- Generate a permit number for approved applications
- Display all stored applications
- Display the total number of applications created

## Permit and License Types
- Business License
- Building Permit
- Event Permit
- Trading License

## Application Status
- Pending
- Approved
- Rejected

## Object-Oriented Programming Concepts Used
- Classes
- Objects
- Attributes
- Instance methods
- Class method
- Static method
- Object interaction

## Classes

### 1. Citizen
The `Citizen` class represents the person applying for a permit or license.

Attributes:
- `citizen_id`
- `name`
- `phone`
- `email`

Main method:
- `display_details()`

### 2. PermitApplication
The `PermitApplication` class represents a permit or license application.

Attributes:
- `application_id`
- `applicant`
- `permit_type`
- `application_date`
- `status`
- `permit_number`

Main methods:
- `display_application()`
- `update_status()`
- `generate_permit_number()`
- `get_total_applications()`
- `validate_permit_type()`

### 3. PermitSystem
The `PermitSystem` class manages the application records.

Main methods:
- `submit_application()`
- `search_application()`
- `update_application_status()`
- `display_all_applications()`
- `display_total_applications()`

## Python Data Structure
The project uses one Python dictionary to store multiple `PermitApplication` objects.

```python
self.applications = {}
```

Applications are stored using the application ID as the key.

```python
self.applications[application_id] = application
```

## Object Interaction
A `Citizen` object is created and passed into a `PermitApplication` object.

```python
citizen = Citizen(citizen_id, name, phone, email)

application = PermitApplication(
    application_id,
    citizen,
    permit_type,
    application_date
)
```

The `PermitSystem` object then stores and manages the application object.

## Method Types

### Instance Method
```python
def display_application(self):
```

### Class Method
```python
@classmethod
def get_total_applications(cls):
    return cls.total_applications
```

### Static Method
```python
@staticmethod
def validate_permit_type(permit_type):
```

## Digital Public Goods Alignment

### Open Source
The source code is made available through GitHub so that it can be viewed, studied, and improved.

### Inclusive and Accessible Design
The system uses a simple numbered console menu and clear text instructions.

### Privacy-Respecting Design
The system stores only basic information needed for the permit application demonstration and does not request unnecessary sensitive information.

### Modular and Reusable Design
The program separates responsibilities into different classes, making the code easier to understand, maintain, and reuse.

## SDG Alignment
The project supports **Sustainable Development Goal 16: Peace, Justice and Strong Institutions** by promoting more organized, transparent, and efficient public service delivery.

## Requirements
- Python 3

No external libraries are required.

## How to Run
1. Download or clone the repository.
2. Open the project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

## Example Usage
```text
================================================
      DIGITAL PERMIT & LICENSE MANAGEMENT
================================================
1. Submit New Application
2. Search Application
3. Update Application Status
4. Display All Applications
5. Display Total Applications
6. Exit
```

Example successful submission:

```text
Application submitted successfully.
Application ID: APP001
Applicant: Samuel Tucker
Permit Type: Business License
Status: Pending
```

Example approval:

```text
Application approved successfully.
Permit Number: BUS-APP001
```

## Repository Structure
```text
smart-digital-permit-license-system/
│
├── main.py
├── README.md
└── screenshots/
```

## Author
Samuel Mando Tucker

## Course
**PROG211 - Object-Oriented Programming 1**

Limkokwing University of Creative Technology - Sierra Leone
