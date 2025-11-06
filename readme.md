# DotDairy - Backend
![DotDairy](./assets/images/logo.png)

## Description
DotDiary is a website that allow users to create FocusLogs and track it over time. The FocusLog contains a focus tag such as (working, studying, reading, writing, etc.), session timer, to-do list, distractions list and after stop the FocusLog, a rate and notes are required to review the session. Also, a weekly report visualize the week progress, sessions by date to help the user get understandable data and learn their focus pattren to increase productivity and time management. Using Django Rest Framework (DRF) for the backend, with React for the frontend, and postgreSQL for the DB creates a valuable application with enhanced functionalities.

## Tech stack
* Django Rest Framework
* React
* PostgreSQL
* VS Code

## Front-End Repo Link
https://github.com/iijumanaAhmed/DotDiary-Frontend

## ERD diagram
![ERD Digram](./assets/images/ERD%20Digram.png)

## Routing Table
| Method  | URL Pattern | Header  | Action |
| ------------- | ------------- | ------------- | ------------- |
| GET  | /focusLog  | getAllFocusLogs  | Retrieve all the user's FocusLog session |
| POST  | /focusLog  | addFocusLog  | Create new FocusLog |
| GET  | /focusLog/:id  | displayFocusLog  | Display specific FocusLog session |
| PUT  | /focusLog/update/:id  | updateFocusLog  | Update exsiting FocusLog |
| DELETE  | /focusLog/delete/:id  | deleteFocusLog  | Delete exsiting FocusLog |
| POST  | /focusLog/:id/assignTag/:id  | assignTag  | Assign tag to the FocusLog session |
| POST  | /focusLog/:id/assignToDoList/:id  | assignToDoList  | Assign ToDoList to the FocusLog session |
| POST  | /focusLog/:id/assignDistraction/:id  | assignDistraction  | Assign distraction to the FocusLog session |
| PATCH  | /focusLog/:id/unassignDistraction/:id  | unassignDistraction  | Unassign distraction to the FocusLog session |
| GET  | /toDoList  | getAllToDoList  | Retrieve all the user's ToDoList |
| POST  | /toDoList  | addToDoList  | Create new ToDoList |
| GET  | /toDoList/:id  | displayToDoList  | Display specific ToDoList |
| PUT  | /toDoList/update/:id  | updateToDoList  | Update exsiting ToDoList |
| DELETE  | /toDoList/delete/:id  | deleteToDoList  | Delete exsiting ToDoList |
| POST  | /toDoList/:id/addTask/:id  | addTask  | Add task to a specific ToDoList |
| DELETE  | /toDoList/:id/removeTask/:id  | removeTask  | Remove task to a specific ToDoList |

## IceBox Features
1. Forgot Password
2. Admin Dashboard & Management Pages
3. FocusLogs Searching by Title