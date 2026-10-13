# ============================================================
# SMART DIGITAL PERMIT AND LICENSE MANAGEMENT SYSTEM
# PROG211 - OBJECT-ORIENTED PROGRAMMING 1
# ============================================================


class Citizen:
    def __init__(self, citizen_id, name, phone, email):
        self.citizen_id = citizen_id
        self.name = name
        self.phone = phone
        self.email = email

    def display_details(self):
        print("Citizen ID:", self.citizen_id)
        print("Applicant:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)


class PermitApplication:
    total_applications = 0

    def __init__(self, application_id, applicant, permit_type, application_date):
        self.application_id = application_id
        self.applicant = applicant
        self.permit_type = permit_type
        self.application_date = application_date
        self.status = "Pending"
        self.permit_number = "Not Issued"

        PermitApplication.total_applications += 1

    def display_application(self):
        print("\n----------------------------------------")
        print("APPLICATION DETAILS")
        print("----------------------------------------")
        print("Application ID:", self.application_id)
        self.applicant.display_details()
        print("Permit Type:", self.permit_type)
        print("Application Date:", self.application_date)
        print("Status:", self.status)
        print("Permit Number:", self.permit_number)
        print("----------------------------------------")

    def update_status(self, new_status):
        self.status = new_status

        if new_status == "Approved":
            self.generate_permit_number()

    def generate_permit_number(self):
        if self.permit_type == "Business License":
            code = "BUS"
        elif self.permit_type == "Building Permit":
            code = "BLD"
        elif self.permit_type == "Event Permit":
            code = "EVT"
        elif self.permit_type == "Trading License":
            code = "TRD"
        else:
            code = "PER"

        self.permit_number = code + "-" + self.application_id

    @classmethod
    def get_total_applications(cls):
        return cls.total_applications

    @staticmethod
    def validate_permit_type(permit_type):
        if permit_type == "Business License":
            return True
        elif permit_type == "Building Permit":
            return True
        elif permit_type == "Event Permit":
            return True
        elif permit_type == "Trading License":
            return True
        else:
            return False


class PermitSystem:
    def __init__(self):
        # One dictionary is used to store multiple PermitApplication objects.
        self.applications = {}

    def submit_application(self):
        print("\n========================================")
        print("SUBMIT NEW APPLICATION")
        print("========================================")

        citizen_id = input("Enter Citizen ID: ")
        name = input("Enter Full Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        citizen = Citizen(citizen_id, name, phone, email)

        print("\nSelect Permit or License Type")
        print("1. Business License")
        print("2. Building Permit")
        print("3. Event Permit")
        print("4. Trading License")

        choice = input("Enter choice: ")

        if choice == "1":
            permit_type = "Business License"
        elif choice == "2":
            permit_type = "Building Permit"
        elif choice == "3":
            permit_type = "Event Permit"
        elif choice == "4":
            permit_type = "Trading License"
        else:
            print("\nInvalid permit selection.")
            return

        if PermitApplication.validate_permit_type(permit_type):
            number = PermitApplication.get_total_applications() + 1
            application_id = "APP" + str(number).zfill(3)

            application_date = input("Enter Application Date: ")

            application = PermitApplication(
                application_id,
                citizen,
                permit_type,
                application_date
            )

            self.applications[application_id] = application

            print("\n========================================")
            print("APPLICATION SUBMITTED SUCCESSFULLY")
            print("========================================")
            print("Application ID:", application_id)
            print("Applicant:", citizen.name)
            print("Permit Type:", permit_type)
            print("Status:", application.status)

    def search_application(self):
        print("\n========================================")
        print("SEARCH APPLICATION")
        print("========================================")

        application_id = input("Enter Application ID: ").upper()
        application = self.applications.get(application_id)

        if application:
            application.display_application()
        else:
            print("\nApplication not found.")

    def update_application_status(self):
        print("\n========================================")
        print("UPDATE APPLICATION STATUS")
        print("========================================")

        application_id = input("Enter Application ID: ").upper()
        application = self.applications.get(application_id)

        if application:
            print("\nCurrent Status:", application.status)
            print("\n1. Approve")
            print("2. Reject")

            choice = input("Enter choice: ")

            if choice == "1":
                application.update_status("Approved")
                print("\nApplication approved successfully.")
                print("Permit Number:", application.permit_number)

            elif choice == "2":
                application.update_status("Rejected")
                print("\nApplication rejected successfully.")

            else:
                print("\nInvalid selection.")
        else:
            print("\nApplication not found.")

    def display_all_applications(self):
        print("\n========================================")
        print("ALL APPLICATIONS")
        print("========================================")

        if len(self.applications) == 0:
            print("No applications available.")
        else:
            for application_id in self.applications:
                application = self.applications[application_id]
                application.display_application()

    def display_total_applications(self):
        total = PermitApplication.get_total_applications()

        print("\n========================================")
        print("TOTAL APPLICATIONS")
        print("========================================")
        print("Total Applications:", total)


def main():
    system = PermitSystem()

    while True:
        print("\n================================================")
        print("      DIGITAL PERMIT & LICENSE MANAGEMENT")
        print("================================================")
        print("1. Submit New Application")
        print("2. Search Application")
        print("3. Update Application Status")
        print("4. Display All Applications")
        print("5. Display Total Applications")
        print("6. Exit")
        print("================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.submit_application()

        elif choice == "2":
            system.search_application()

        elif choice == "3":
            system.update_application_status()

        elif choice == "4":
            system.display_all_applications()

        elif choice == "5":
            system.display_total_applications()

        elif choice == "6":
            print("\n========================================")
            print("Thank you for using the system.")
            print("Program closed.")
            print("========================================")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()