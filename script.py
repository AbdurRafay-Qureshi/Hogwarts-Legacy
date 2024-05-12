import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

orders = []

def place_order():
    customer_name = input_dialog("Enter customer name:")
    items_input = input_dialog("Enter ordered items (comma-separated):")
    
    items = items_input.split(", ") if items_input else []

    order = {
        "order_number": len(orders) + 1,
        "customer_name": customer_name,
        "items": items,
        "date": pd.to_datetime("today"),
    }
    orders.append(order)

    show_info_message(f"Order placed successfully. Order ID: {order['order_number']}")

def export_to_excel():
    filename = input_dialog("Enter the filename to export to (e.g., bakery_orders.xlsx):")
    
    df = pd.DataFrame(orders)
    df.drop(columns=["date"]).to_excel(filename, index=False)

    show_info_message(f"Data exported to {filename} successfully.")

def most_ordered_items():
    if not orders:
        show_info_message("No orders placed yet.")
    else:
        all_items = [item for order in orders for item in order["items"]]
        item_counts = pd.Series(all_items).value_counts()
        top_items = item_counts.head(3)

        plt.bar(top_items.index, top_items.values, color='skyblue')
        plt.title('Most Ordered Items')
        plt.xlabel('Items')
        plt.ylabel('Quantity')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def get_order_by_order_id():
    order_id = int(input_dialog("Enter Order ID:"))
    order = next((o for o in orders if o["order_number"] == order_id), None)
    
    if order:
        display_order_details(order_id, order)
    else:
        show_info_message(f"No order found for Order ID {order_id}.")

def display_order_details(order_id, order):
    order_details = f"Order Details for Order ID {order_id}:\n" \
                    f"Customer Name: {order['customer_name']}\n" \
                    f"Items: {order['items']}\n" \
                    f"Date: {order['date']}"
    show_info_message(order_details)

def view_all_orders():
    if not orders:
        show_info_message("No orders placed yet.")
    else:
        orders_table = tabulate(orders, headers="keys", tablefmt="pretty")
        show_info_message(orders_table)

def exit_program():
    root.destroy()

def input_dialog(prompt):
    return simpledialog.askstring("Input", prompt)

def show_info_message(message):
    messagebox.showinfo("Information", message)

root = tk.Tk()
root.title("Bakery Management System")
root.geometry("800x600")
root.configure(bg="#FFF2E6")

# Title
title_label = tk.Label(root, text="Bakery Management System", font=("Arial", 24, "bold"), bg="#FFF2E6", fg="#5C3317")
title_label.pack(pady=20)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#FFF2E6")
buttons_frame.pack()

button_style = {"font": ("Arial", 14, "bold"), "bg": "#FF7043", "fg": "#FFFFFF", "width": 30, "height": 2, "bd": 0}

tk.Button(buttons_frame, text="Place an Order", command=place_order, **button_style).pack(pady=10)
tk.Button(buttons_frame, text="Export to Excel", command=export_to_excel, **button_style).pack(pady=10)
tk.Button(buttons_frame, text="Most Ordered Items (Graphical)", command=most_ordered_items, **button_style).pack(pady=10)
tk.Button(buttons_frame, text="Get Order by Order ID", command=get_order_by_order_id, **button_style).pack(pady=10)
tk.Button(buttons_frame, text="View All Orders", command=view_all_orders, **button_style).pack(pady=10)
tk.Button(buttons_frame, text="Exit", command=exit_program, **button_style).pack(pady=10)

root.mainloop()