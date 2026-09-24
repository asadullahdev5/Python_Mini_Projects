
# Class for Medicines
class Medicines:
    def __init__(self, name, company, quantity, expiry_date, price, batch_no):
        self.name = name
        self.company = company
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.price = price
        self.batch_no = batch_no

# List to store medicines

Store = []
# Function to add medicines
def add_medicine():
    m_name = input("Enter Medicine Here: ")
    m_company = input("Enter Company Here: ")
    m_quantity = input("Enter Quantity Here: ")
    m_expiry = input("Enter Expiry_Date Here: ")
    m_price = input("Enter Price Here: ")
    m_batch = input("Enter Batch_No Here: ")


    new_medicines = Medicines(m_name, m_company, m_quantity, m_expiry, m_price, m_batch)
    Store.append(new_medicines)
    with open("data.txt", "a") as f:
        Convert = str(m_name + "," + m_company + ","+ m_expiry + ","+ m_price + ","+ m_batch + ","+ m_quantity)
        f.write(Convert)
    print("Medicines has Been Added")

    return Store

# Call the function to add medicines
c = add_medicine()
print(c)