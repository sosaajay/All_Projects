import csv
from datetime import datetime
import os

try:
    import pandas as pd
except Exception:
    pd = None

try:
    import numpy as np
except Exception:
    np = None

import matplotlib.pyplot as plt

def positive_float(x, name="value"):
    try:
        v = float(x)
    except Exception:
        raise ValueError(f"{name} must be a number.")
    if v < 0:
        raise ValueError(f"{name} must be non-negative.")
    return v

def positive_int(x, name="value"):
    try:
        v = int(float(x))
    except Exception:
        raise ValueError(f"{name} must be an integer.")
    if v < 0:
        raise ValueError(f"{name} must be non-negative.")
    return v

class Bookstore:
    def __init__(self):
        self.inventory = []   
        self.sales = []       

    def find_book_index(self, title):
        for i, b in enumerate(self.inventory):
            if b["title"].lower() == title.lower():
                return i
        return -1

    def add_book(self, title, author, genre, price, qty):
        if self.find_book_index(title) != -1:
            raise ValueError("Book already exists. Use update_book to change quantity/price.")
        price = positive_float(price, "Price")
        qty = positive_int(qty, "Quantity")
        book = {"title": title, "author": author, "genre": genre, "price": price, "qty": qty}
        self.inventory.append(book)
        print(f"Added '{title}' (qty={qty}, price={price})")

    def update_book(self, title, price=None, qty=None):
        idx = self.find_book_index(title)
        if idx == -1:
            raise ValueError("Book not found.")
        if price is not None:
            self.inventory[idx]["price"] = positive_float(price, "Price")
        if qty is not None:
            self.inventory[idx]["qty"] = positive_int(qty, "Quantity")
        print(f"Updated '{title}' -> price={self.inventory[idx]['price']}, qty={self.inventory[idx]['qty']}")

    def remove_book(self, title):
        idx = self.find_book_index(title)
        if idx == -1:
            raise ValueError("Book not found.")
        removed = self.inventory.pop(idx)
        print(f"Removed '{removed['title']}' from inventory.")

    def list_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("\nInventory:")
        print(f"{'Title':30} {'Author':15} {'Genre':10} {'Price':>6} {'Qty':>4}")
        print("-"*72)
        for b in self.inventory:
            print(f"{b['title'][:30]:30} {b['author'][:15]:15} {b['genre'][:10]:10} {b['price']:6.2f} {b['qty']:4d}")
        print()

    def record_sale(self, title, qty, date=None):
        idx = self.find_book_index(title)
        if idx == -1:
            raise ValueError("Book not in inventory.")
        qty = positive_int(qty, "Quantity sold")
        if qty > self.inventory[idx]["qty"]:
            raise ValueError("Not enough copies in stock.")
        price = self.inventory[idx]["price"]
        revenue = price * qty
        self.inventory[idx]["qty"] -= qty
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        sale = {"date": date, "title": self.inventory[idx]["title"], "qty": qty, "revenue": revenue}
        self.sales.append(sale)
        print(f"Recorded sale: {qty} x '{title}' (revenue {revenue:.2f})")

    def generate_report(self):
        total_stock = sum(b["qty"] for b in self.inventory)
        total_books = len(self.inventory)
        total_revenue = sum(s["revenue"] for s in self.sales)
        total_sold = sum(s["qty"] for s in self.sales)
        print("\n==== Simple Report ====")
        print(f"Books in catalog: {total_books}")
        print(f"Total units in stock: {total_stock}")
        print(f"Total units sold: {total_sold}")
        print(f"Total revenue: {total_revenue:.2f}")
        
        if self.sales:
            counts = {}
            for s in self.sales:
                counts[s["title"]] = counts.get(s["title"], 0) + s["qty"]
            top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
            print("Top sellers:")
            for t, q in top:
                print(f" - {t}: {q} copies")
        print("=======================\n")

    def total_revenue_numpy(self):
        if np is None:
            print("NumPy not installed; skip this metric.")
            return None
        revenues = np.array([s["revenue"] for s in self.sales], dtype=float)
        total = float(np.sum(revenues)) if revenues.size else 0.0
        print(f"(NumPy) Total revenue = {total:.2f}")
        return total

    def save_inventory_csv(self, filename="inventory.csv"):
        if pd is not None:
            df = pd.DataFrame(self.inventory)
            df.to_csv(filename, index=False)
        else:
            with open(filename, "w", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["title","author","genre","price","qty"])
                writer.writeheader()
                writer.writerows(self.inventory)
        print(f"Saved inventory to {filename}")

    def save_sales_csv(self, filename="sales.csv"):
        if pd is not None:
            df = pd.DataFrame(self.sales)
            df.to_csv(filename, index=False)
        else:
            with open(filename, "w", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["date","title","qty","revenue"])
                writer.writeheader()
                writer.writerows(self.sales)
        print(f"Saved sales to {filename}")

    def load_inventory_csv(self, filename="inventory.csv"):
        if not os.path.exists(filename):
            print(f"No {filename} found; starting with empty inventory.")
            return
        if pd is not None:
            df = pd.read_csv(filename)
            self.inventory = []
            for _, row in df.iterrows():
                self.inventory.append({
                    "title": str(row.get("title", row.get("Title", ""))),
                    "author": str(row.get("author", row.get("Author", ""))),
                    "genre": str(row.get("genre", row.get("Genre", ""))),
                    "price": float(row.get("price", row.get("Price", 0.0))),
                    "qty": int(row.get("qty", row.get("Quantity", 0)))
                })
        else:
            with open(filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.inventory = []
                for row in reader:
                    self.inventory.append({
                        "title": row.get("title",""),
                        "author": row.get("author",""),
                        "genre": row.get("genre",""),
                        "price": float(row.get("price",0.0)),
                        "qty": int(float(row.get("qty",0)))
                    })
        print(f"Loaded inventory from {filename}")

    def load_sales_csv(self, filename="sales.csv"):
        if not os.path.exists(filename):
            print(f"No {filename} found; starting with empty sales history.")
            return
        if pd is not None:
            df = pd.read_csv(filename)
            self.sales = []
            for _, row in df.iterrows():
                self.sales.append({
                    "date": str(row.get("date", row.get("Date", ""))),
                    "title": str(row.get("title", row.get("Title", ""))),
                    "qty": int(row.get("qty", row.get("Quantity Sold", 0))),
                    "revenue": float(row.get("revenue", row.get("Total Revenue", 0.0)))
                })
        else:
            with open(filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.sales = []
                for row in reader:
                    self.sales.append({
                        "date": row.get("date",""),
                        "title": row.get("title",""),
                        "qty": int(float(row.get("qty",0))),
                        "revenue": float(row.get("revenue",0.0))
                    })
        print(f"Loaded sales from {filename}")

    def plot_monthly_sales(self, filename="monthly_sales.png"):
        if not self.sales:
            print("No sales to plot.")
            return
        agg = {}
        for s in self.sales:
            try:
                d = datetime.strptime(s["date"], "%Y-%m-%d")
            except Exception:
                continue
            key = d.strftime("%Y-%m")
            agg[key] = agg.get(key, 0.0) + s["revenue"]
        months = sorted(agg.keys())
        values = [agg[m] for m in months]
        plt.figure(figsize=(8,4))
        plt.plot(months, values, marker="o")
        plt.title("Monthly Revenue")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Saved monthly sales plot to {filename}")

    def plot_genre_revenue_bar(self):
        if not self.sales:
            print("No sales data available.")
            return
        if pd is None:
            print("Pandas not installed.")
            return

        df_sales = pd.DataFrame(self.sales)
        df_inv = pd.DataFrame(self.inventory)

        merged = df_sales.merge(df_inv, on="title")
        genre_rev = merged.groupby("genre")["revenue"].sum()

        plt.figure(figsize=(8, 4))
        plt.bar(genre_rev.index, genre_rev.values)
        plt.title("Revenue by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.show()

    def plot_revenue_pie_chart(self):
        if not self.sales:
            print("No sales data available.")
            return
        if pd is None:
            print("Pandas not installed.")
            return

        df = pd.DataFrame(self.sales)
        rev = df.groupby("title")["revenue"].sum()

        plt.figure(figsize=(7, 7))
        plt.pie(rev, labels=rev.index, autopct="%1.1f%%")
        plt.title("Revenue Distribution by Book")
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self):
        if not self.sales:
            print("No sales data available.")
            return
        if pd is None:
            print("Pandas not installed.")
            return

        df = pd.DataFrame(self.sales)
        corr = df[["qty", "revenue"]].corr()

        import seaborn as sns
        plt.figure(figsize=(5, 4))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()


def create_sample_data(store: Bookstore):
    store.inventory = [
        {"title":"Atomic Habits","author":"James Clear","genre":"Self-Help","price":11.0,"qty":40},
        {"title":"The Alchemist","author":"Paulo Coelho","genre":"Fiction","price":9.99,"qty":50},
        {"title":"Deep Work","author":"Cal Newport","genre":"Productivity","price":14.25,"qty":20},
    ]
    store.sales = [
        {"date":"2025-09-01","title":"Atomic Habits","qty":3,"revenue":33.0},
        {"date":"2025-09-15","title":"The Alchemist","qty":5,"revenue":49.95},
        {"date":"2025-10-02","title":"Atomic Habits","qty":7,"revenue":77.0},
    ]
    print("Sample data created (3 inventory items, 3 sales records).")


def main():
    store = Bookstore()
    store.load_inventory_csv() 
    store.load_sales_csv()

    while True:
        print("\n--- Simple Bookstore Menu ---")
        print("1) Show inventory")
        print("2) Add book")
        print("3) Update book")
        print("4) Remove book")
        print("5) Record sale")
        print("6) Generate report")
        print("7) Save data to CSV")
        print("8) Create sample data")
        print("9) Plot monthly sales (PNG)")
        print("10) Plot Genre Revenue Bar")
        print("11) Plot Revenue Pie Chart")
        print("12) Plot Correlation Heatmap")
        print("0) Exit")
        choice = input("Choose option: ").strip()

        try:
            if choice == "1":
                store.list_inventory()
            elif choice == "2":
                t = input("Title: ").strip()
                a = input("Author: ").strip()
                g = input("Genre: ").strip()
                p = input("Price: ").strip()
                q = input("Quantity: ").strip()
                store.add_book(t, a, g, p, q)
            elif choice == "3":
                t = input("Title to update: ").strip()
                p = input("New price (leave blank to skip): ").strip()
                q = input("New qty (leave blank to skip): ").strip()
                store.update_book(t, price=(p if p else None), qty=(q if q else None))
            elif choice == "4":
                t = input("Title to remove: ").strip()
                store.remove_book(t)
            elif choice == "5":
                t = input("Title sold: ").strip()
                q = input("Quantity sold: ").strip()
                d = input("Date (YYYY-MM-DD) [leave blank = today]: ").strip()
                d = d if d else None
                store.record_sale(t, q, date=d)
            elif choice == "6":
                store.generate_report()
                store.total_revenue_numpy()
            elif choice == "7":
                store.save_inventory_csv()
                store.save_sales_csv()
            elif choice == "8":
                create_sample_data(store)
            elif choice == "9":
                store.plot_monthly_sales()
            elif choice == "10":
                store.plot_genre_revenue_bar()
            elif choice == "11":
                store.plot_revenue_pie_chart()
            elif choice == "12":
                store.plot_correlation_heatmap()
            elif choice == "0":
                print("Goodbye — thanks for trying the beginner program!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
