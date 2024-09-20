class InvalidMarksException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

def get_percentage():
    try:
        marks = float(input("Enter your marks in percentage: "))
        
        if marks < 0 or marks > 100:
            raise InvalidMarksException("Marks should be between 0 and 100.")
        
        print(f"You entered: {marks}%")
    
    except ValueError:
        print("Invalid input! Please enter a  value.")
    except InvalidMarksException as ABC:
        print(ABC)

if __name__ == "__main__":
    get_percentage()
