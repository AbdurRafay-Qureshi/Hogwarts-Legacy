
# Bakery Management System

This Bakery Management System is a Python program designed to help manage orders and track customer information in a bakery setting. It provides a user-friendly interface using the Tkinter library for creating GUI applications.

## Features

- **Place an Order**: Allows the user to enter the customer name and the items ordered. The order is then added to the system with a unique order ID.

- **Export to Excel**: Enables the user to export the order data to an Excel file (.xlsx). This feature helps in keeping track of orders and generating reports.

- **Most Ordered Items (Graphical)**: Displays a graphical representation of the top three most ordered items. It uses the Matplotlib library to create a bar chart showing the quantity of each item.

- **Get Order by Order ID**: Allows the user to search for a specific order using its unique order ID. The program displays the order details, including the customer name, items ordered, and the date of the order.

- **View All Orders**: Displays a table of all the orders placed in the system. It uses the Pandas library to format and present the order data in a tabular format.

- **Exit**: Closes the program.

## Prerequisites

- Python 3.x
- Tkinter library
- Pandas library
- Matplotlib library
- Tabulate library

## How to Run

1. Clone the repository to your local machine.

2. Install the required libraries using the following command:
   ```
   pip install pandas matplotlib tabulate
   ```

3. Run the program using the following command:
   ```
   python bakery_management_system.py
   ```

## Screenshots

![alt text](<Screenshot (62).png>)
 


## Converted Into Executable (.exe)

- The program can be converted into an executable (.exe) file using a tool like PyInstaller.

- After running PyInstaller, two additional folders will be created:
  - `dist`: Contains the executable file and any necessary dependencies.
  - `build`: Contains intermediate build files generated during the conversion process.

- To run the executable, navigate to the `dist` folder and double-click the "Bakery.exe" file.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

## Acknowledgements

- The program utilizes the Tkinter library for creating the graphical user interface.
- Pandas library is used for data manipulation and tabular formatting.
- Matplotlib library is used for data visualization.
- Tabulate library is used for formatting the order data in table format.

Feel free to customize and expand upon this README file based on your specific project requirements and additional information you would like to provide to your users.