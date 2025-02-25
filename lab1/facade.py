"""
    Реалізація патерну Фасад (Facade) на прикладі брогювання кімнати в готелі
"""

class RoomBooking:
    """Бронювання кімнати"""
    def book_room(self, room_type):
        return f"Room '{room_type}' has been booked."

class PaymentProcessing:
    """Оброблення оплати"""
    def process_payment(self, amount):
        return f"Payment of ${amount} has been processed."

class CustomerService:
    """Підтвердження бронювання"""
    def send_confirmation(self, customer_email):
        return f"Confirmation email sent to {customer_email}."

# Facade Class
class HotelBooking:
    def __init__(self):
        self.room_booking = RoomBooking()
        self.payment_processing = PaymentProcessing()
        self.customer_service = CustomerService()

    def book_hotel(self, room_type, amount, customer_email):
        results = [
            self.room_booking.book_room(room_type),
            self.payment_processing.process_payment(amount),
            self.customer_service.send_confirmation(customer_email)
        ]
        return "\n".join(results)


if __name__ == "__main__":
    hotel_facade = HotelBooking()
    print(hotel_facade.book_hotel("Standart", 50, "customer@example.com"))
