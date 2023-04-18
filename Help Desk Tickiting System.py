class Ticket:
    # Static field for the counter
    counter = 2000

    # Constructor to initialize the ticket attributes
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1

    # Method to generate a new password for password change requests
    def generate_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = "New password: " + new_password
            self.status = "Closed"

    # Method to update the ticket response
    def update_response(self, response):
        self.response = response

    # Method to resolve the ticket
    def resolve_ticket(self):
        if self.status == "Open":
            self.status = "Closed"

    # Method to reopen the ticket
    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"

    # Method to print the ticket information
    def print_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Name of Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Contact Email:", self.contact_email)
        print("Description of Issue:", self.description)
        print("Response from IT Department:", self.response)
        print("Ticket Status:", self.status)

    # Static method to get ticket statistics
    @staticmethod
    def get_ticket_stats(ticket_list):
        num_tickets = len(ticket_list)
        num_open_tickets = 0
        num_closed_tickets = 0

        for ticket in ticket_list:
            if ticket.status == "Open":
                num_open_tickets += 1
            elif ticket.status == "Closed":
                num_closed_tickets += 1

        print("Number of Tickets Submitted:", num_tickets)
        print("Number of Open Tickets:", num_open_tickets)
        print("Number of Closed Tickets:", num_closed_tickets)


def create_ticket():
    # Get ticket information from user input
    staff_id = input("Enter Staff ID: ")
    creator_name = input("Enter Ticket Creator Name: ")
    contact_email = input("Enter Contact Email: ")
    description = input("Enter Description of Issue: ")

    # Create ticket instance
    ticket = Ticket(staff_id, creator_name, contact_email, description)

    # Generate new password for password change request
    ticket.generate_password()

    return ticket


def main():
    # Create list to store tickets
    ticket_list = []

    # Create ticket instances
    ticket1 = create_ticket()
    ticket2 = create_ticket()
    ticket3 = create_ticket()

    # Add tickets to list
    ticket_list.append(ticket1)
    ticket_list.append(ticket2)
    ticket_list.append(ticket3)

    # Print ticket information
    print("\nTicket Information:")
    for ticket in ticket_list:
        ticket.print_ticket()

    # Update ticket response
    ticket1.update_response("Restart your computer and try again")

    # Resolve some tickets
    ticket1.resolve_ticket()
    ticket2.resolve_ticket()

    # Reopen some resolved tickets
    ticket1.reopen_ticket()

    # Print ticket information and statistics
    print("\nTicket Information:")
    for ticket in ticket_list:
        ticket.print_ticket()

    print("\nTicket Statistics:")
    Ticket.get_ticket_stats(ticket_list)

main()