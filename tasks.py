import csv
from datetime import datetime, date

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class llist:
    def __init__(self):
        self.head = None
        self.head = None

    def push(self, data):
        node = Node(data, self.head)
        self.head = node
        

    def print_list(self):
        pointer = self.head
    
        count = 1
        while pointer:
            #have inside of loop so next node will point to data
            data = pointer.data
            print(f"{count}.")
            for key, value in data.items():
                print(f"{key}: {value}")
            
            print("\n")
            pointer = pointer.next
            count += 1


        print("\n")


    def get_len(self):
        counter = 0
        pointer = self.head

        while pointer:
            counter += 1
            pointer = pointer.next

        return counter

    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty. Nothing to delete")
            return
        
        if position == 1:
            self.head = self.head.next
            return
        
        pointer = self.head
        counter = 1
        prev = None
        while pointer and counter < position:
            prev = pointer
            pointer = pointer.next
            counter += 1

        if pointer is None:
            print("Invalid psition. Task not found.")

        prev.next = pointer.next
        self.save_file()


    def mark_as_complete(self, position):
        if self.head == None:
            print("You have no tasks currently")
            return
        
        if position == 1:
            self.head.data['Completion'] = 'Completed'
            return
        
        pointer = self.head
        counter = 1

        while pointer and counter < position:
            pointer = pointer.next
            counter +=1 

        pointer.data["Completion"] = 'Completed'
        

    def save_file(self):
        if self.get_len() <= 0:
            print("You have no tasks to be saved, Please try again!\n")
        else:

            with open("tasks.csv", 'w', newline='') as file:
                field_names = ['Title', 'Description', 'Due_date', 'Days_till_due', 'Completion']
                csv_writer = csv.DictWriter(file, fieldnames=field_names)

                csv_writer.writeheader()

                pointer = self.head

                while pointer:
                    csv_writer.writerow(pointer.data)
                    pointer = pointer.next
                
                print("---------------")
                print("Your tasks have been saved")
                print('---------------')


    def load_file(self):
        with open('tasks.csv', 'r', newline='') as file:
            read = csv.DictReader(file)
            for rows in read:
                due_date_format = date.fromisoformat(rows['Due_date'])
                rows['Days_till_due'] = abs(due_date_format - date.today()).days
                linked_list.push(rows)

    def notify_user(self):
        if self.head == None:
            return
        
        pointer = self.head
        while pointer:
            for key, value in pointer.data.items():
                if pointer.data['Days_till_due'] <= 3:
                    print(f"{key}: {value}")

            print("\n")
            pointer = pointer.next

    def sort_by_date(self):
        #if the list is empty or if there is only one node inside
        if not self.head or not self.head.next:
            return

        #the dummy node will make it easy to sort the list
        dummy = Node(0, self.head)
        prev, cur = self.head, self.head.next

        while cur:
            if cur.data['Days_till_due'] >= prev.data['Days_till_due']:
                prev, cur = cur, cur.next
                continue

            temp = dummy

            while temp.next and cur.data['Days_till_due'] > temp.next.data['Days_till_due']:
                temp = temp.next

            prev.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prev.next

        self.head = dummy.next




if __name__ == "__main__":
        linked_list = llist()
        today = date.today() 
        while True:
            print("------------------")
            print("1. Add Task")
            print("2. Remove Tasks")
            print("3. View Tasks")
            print("4. Mark Task as Complete")
            print("5. Load To-Do List")
            print("6. Exit")
            print("------------------")
            choice = int(input("Enter your choice: "))
            print("\n")

            if choice == 1:
                title = input("Enter the title of the task: ")
                description = input("Enter the description: ")
                due_date = input("Enter the due data (YYYY-MM-DD): ")
                print('\n')
                date_format =  '%Y-%m-%d'
                while True:
                    try:
                        date_object = datetime.strptime(due_date, '%Y-%m-%d')
                        due_date_format = date.fromisoformat(due_date)
                        data = {
                        "Title": title,
                        "Description": description,
                        "Due_date": due_date,
                        "Days_till_due": abs(due_date_format - today).days,
                        "Completion": "Incomplete"
                        
                        }
                        linked_list.push(data)
                        linked_list.save_file()
                        break
                    except ValueError:
                        print("Incorrect date format, should be YYYY-MM-DD\n")

            if choice == 2:
                print("Here are your tasks")
                linked_list.print_list()
                print("which Task would you like to delete?")
                delete = int(input("Pick a number: \n"))
                linked_list.delete_by_position(delete)
                print("Task has been deleted")


            if choice == 3:

                if linked_list.get_len() == 0:
                    print("There are currently no tasks to view.\n")

                else:
                    linked_list.print_list()
            
            if choice == 4:
                linked_list.print_list()
                complete = int(input("Enter which task you would like to Complete: "))
                linked_list.mark_as_complete(complete)

            if choice == 5:
                linked_list.load_file()
                linked_list.sort_by_date()
                print("These tasks are due very soon!!\n")
                linked_list.notify_user()


                
            if choice == 6:
                quit()


