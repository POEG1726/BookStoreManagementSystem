
# Bookstore Management System

## Project Overview

The Bookstore Management System is a comprehensive platform designed to facilitate the browsing, searching, and purchasing of books for users. It also enables administrators to efficiently manage inventory, orders, and customer information.

## Features

### User Features
- **Browse Books**: View a wide range of books available in the store.
- **Search Books**: *Function not yet implemented.*
- **Shopping Cart**: Add books to the shopping cart and proceed to checkout.
- **User Authentication**: Sign up, log in, and manage user accounts.
- **Order Processing**: Handle the complete checkout process including payment.

### Admin Features
- **Inventory Management**: Add, update, and delete book information.
- **Order Management**: View and process customer orders.
- **User Management**: Manage customer information and order history.

## Project Structure

### Frontend
- **Screens**: Implements user interfaces for browsing books, searching, displaying book details, and handling the checkout process.
- **Responsiveness**: Ensures the user interface is responsive and accessible.

### Backend
- **Book Management**: Handles CRUD operations for books.
- **User Authentication**: Manages user sign-up, login, and authentication.
- **Cart Management**: Manages items in the user's shopping cart.
- **Integration**: Ensures seamless interaction between the frontend and backend.

### Database Management
- **Schema Design**: Implements a relational database schema to store book information, customer data, orders, and transactions.
- **Data Storage**: Ensures efficient retrieval and storage of data.

## Technologies Used
- **Programming Language**: Python 3.9
- **Framework**: PySide6 for frontend development
- **UI Enhancement**: PySide6-Fluent-Widgets
- **Data Storage**: JSON for data storage
- **Modules**: Listed in `requirements.txt`

## Usage
1. **Install requirements**
   ```pip install -r requirements.txt```
2. **Run the Application**:
    ```sh
    python MainWindow.py
    ```
3. **Access the application** through the GUI to browse, search, and manage books.

## Project Files

### Frontend
- `MainWindow.py`: Main window of the application
- `Home.py`: Home screen for browsing books
- `Cart.py`: Shopping cart interface
- `CartCard.py`: Cart item component
- `BookCard.py`: Book item component
- `Management.py`: Admin interface for managing inventory and orders
- `PopupBox.py`: Utility for displaying popup messages

### Backend
- `Backend.py`: Handles backend logic for book management, user authentication, and order processing

### Others
- `requirements.txt`: List of dependencies

## Documentation
- **System Design**: Detailed explanation of system architecture.
- **Flowcharts**: Visual representation of system processes.
- **Pseudocode**: High-level code logic for critical functionalities.
- **Database Schema**: Design of the database structure.

## Data Structures

### Books
```json
{
    "8-digit uuid": {
        "name": "Book Name 1",
        "author": "Author 1",
        "price": 2-decimal float,
        "desc": "Description",
        "id": "8-digit uuid",
        "cover": path | null
    },
    "8-digit uuid": {
        "name": "Book Name 2",
        "author": "Author 2",
        "price": 2-decimal float,
        "desc": "Description",
        "id": "8-digit uuid",
        "cover": path | null
    }
}
```

### Users
```json
{
    "8-digit uuid": {
        "name": "User Name 1",
        "email": "eg@eg.com",
        "uniqID": "8-digit uuid",
        "pwd": "md5 string",
        "cart": {
            "8-digit uuid": Quantity,
            "8-digit uuid": Quantity,
            "8-digit uuid": Quantity
        },
        "permission": "admin"
    },
    "8-digit uuid": {
        "name": "User Namer 2",
        "email": "eg@eg.com",
        "uniqID": "8-digit uuid",
        "pwd": "md5 string",
        "cart": {},
        "permission": "user"
    }
}
```

## Contributors
- **POEG1726**: Project Lead, Developer
- **Contributor Name**: Developer
