from database import (
    add_staff,
    get_all_staff,
    get_staff_by_id,
    update_staff,
    delete_staff
)

def create_staff(name,email,salary,role,department):
    if not name or not email:
        raise ValueError("Name and email are required.")
    if float(salary)<0:
        raise ValueError("Salary cannot be negative.")
    return add_staff(name,email,float(salary),role,department)

def list_staff():
    return get_all_staff()

def get_staff(staff_id):
    staff = get_staff_by_id(staff_id)

    if not staff:
        return None

    return staff            
def edit_staff(staff_id,name,email,role,salary,department):
    if float(salary) < 0:
        raise ValueError("Invalid salary")
    return update_staff(staff_id,name,email,role,float(salary),department)        

def remove_staff(staff_id):
    staff = get_staff_by_id(staff_id)
    if not staff:
        raise ValueError("Staff not found")
    return delete_staff(staff_id)



