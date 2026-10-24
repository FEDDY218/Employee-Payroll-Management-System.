# Employee Payroll Management System

## Project Description
The Employee Payroll Management System is a Python project that manages employee information, calculates salaries, and simulates salary payment processing. It uses Object-Oriented Programming (OOP) to represent different employee roles and manage their payroll records.

## Features
- Store employee names, IDs, and basic salaries.
- Calculate manager salaries, including bonuses.
- Store developer programming languages.
- Calculate employee salary payments.
- Process payments and prevent duplicate processing.
- Validate salaries before processing payments.
- Track payment status.
- Display payroll summaries.

## Technologies Used
- Python
- Object-Oriented Programming (OOP)

## Classes
- **Employee:** Stores common employee information and calculates basic salary.

Manager: Inherits from Employee and includes a bonus in salary calculations.

Developer: Inherits from Employee and stores their programming language.

Payroll: Calculates salary payments, manages payment status, and displays payroll summaries.

Example

The project creates two employees:

Manager: Basic salary of KSh 80,000 and bonus of KSh 15,000, giving a total salary of KSh 95,000.

Developer: Basic salary of KSh 60,000.

The system processes salary payments, prevents a payment from being processed twice, and displays the manager's payroll summary.

Concepts Practiced

Classes and objects

Inheritance

The super() function

Method overriding

Encapsulation and private attributes

Conditional statements

String formatting

Object composition

How to Run

Install Python on your computer.

Clone or download this repository.

Open the project folder in VS Code.

Run the following command in the terminal:

python main.py

Purpose

This project was created to practice Python Object-Oriented Programming using a practical employee payroll scenario.

Note: Payment processing is simulated for educational purposes. The project does not transfer actual money.