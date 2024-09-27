from datetime import datetime

def calculate_fine(book_id, due_date, return_date):
  

  # Convert due_date and return_date to datetime objects
  due_date = datetime.strptime(due_date, "%Y-%m-%d")
  return_date = datetime.strptime(return_date, "%Y-%m-%d")

  # Calculate the days overdue
  days_overdue = (return_date - due_date).days

 
  if days_overdue <= 7:
    fine_rate = 20
  elif days_overdue <= 14:
    fine_rate = 50
  else:
    fine_rate = 100

  
  fine_amount = days_overdue * fine_rate

  
  return {
    "book_id": book_id,
    "due_date": due_date.strftime("%Y-%m-%d"),
    "return_date": return_date.strftime("%Y-%m-%d"),
    "days_overdue": days_overdue,
    "fine_rate": fine_rate,
    "fine_amount": fine_amount
  }


book_id = input("Enter the book ID: ")
due_date = input("Enter the due date (YYYY-MM-DD): ")
return_date = input("Enter the return date (YYYY-MM-DD): ")


result = calculate_fine(book_id, due_date, return_date)


print("Book ID:", result["book_id"])
print("Due Date:", result["due_date"])
print("Return Date:", result["return_date"])
print("Days Overdue:", result["days_overdue"])
print("Fine Rate:", result["fine_rate"])
print("Fine Amount:", result["fine_amount"])
