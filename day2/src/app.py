"""Application entry point for the day2 customer demo."""

from store.customerstore import CustomerStore
from view.customerview import CustomerView

def main():
    """Initialize the customer store and display the customer list."""
    customer_store = CustomerStore(100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()

if __name__ == "__main__":
    main()