# Exercise

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame.  

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.  

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:  

## Example 1:

INPUT:  
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00  
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  

OUTPUT:  
ASTRID-RENE: 2  
ASTRID-ANDRES: 3  
RENE-ANDRES: 2  

## Example 2:

INPUT:  
RENE=MO10:15-12:00,TU10:00-12:00,TH013:00-13:15,SA14:00-18:00,SU20:00-21:00  
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  

OUTPUT:  
RENE-ASTRID: 3  


# Solution
The problem was solved by following the following steps:
1. Reading the file and obtaining the information it contained.  
2. Group the information in a structure that makes it easy to calculate what you are looking for.  
3. Obtain the table that relates two employees and the frequency with which they met at work.  

The Mediator design pattern was used. In this way, the BusinesLogic class that is in charge of obtaining the frequency table does not have to depend on the Employee and WorkDay classes but only on the EmployeeWorkDays class. 

The classes used focus on compliance with the SOLID principles as their single responsibility, since no class has responsibilities that are not within its competence.

# Execution
To run the program, the only requirement is to pass as an argument the name of the file that contains the information on the hours worked by the different employees.

>python main.py \<filename>  

ejemplo:  
>python main.py .\data\data1.txt  


The unit tests were carried out with the unittest framework.  
To run the tests you must run the command:  
>python .\test\test.py  


