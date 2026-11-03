class ParkingPermit:
    """Store information shared by every type of parking permit"""

    def __init__(self, owner_name: str, months: int, fee_schedule: dict[str, float]) -> None:
        """Create a permit for owner for the given number of months.
            
            Preconditions: months is not negative and fee_schedule contains proices needed
            by particular permit subclass"""

        if months < 0:

            raise ValueError("Months cannot be negative")

        self.owner_name   = owner_name
        self.months       = months
        self.fee_schedule = fee_schedule.copy()

    def cost (self) -> float:
        """Return permits cost
        
            Subclasses must override this method as eash permit
            has different pricing"""

        raise NotImplementedError("Each permit type must calculate its own cost")

    def __str__(self) -> str:
        """Return readable description of permit"""

        return f"{self.owner_name}: {self.months} month(s), cost = ${self.cost(): .2f}"

    def __repr__(self) -> str:
        """Return programmer-styled decsription of permit"""

        return (f"{type(self).__name__}({self.owner_name!r}, {self.months!r}, "
                f"{self.fee_schedule!r})")

class StudentPermit(ParkingPermit):
    """Parking permit for a student and one or more registered vehicles"""

    def __init__(self, owner_name: str, months: int, fee_schedule: dict[str, float], vehicles: int) -> None:
        """Create student permit with indicated number of vehicles
        
            Preconditions: at least 1 vehicle. fee_schedule must have 'monthly_cost' 
            and 'extra_vehicle_fee' entries"""

        super().__init__(owner_name, months, fee_schedule)
        if vehicles < 1:

            raise ValueError("Student permit requires at least one vehicle")
        
        self.vehicles = vehicles

    def cost(self) -> float:
        """Return monthly cost plus fees for vehicles after the first"""

        return (self.months * self.fee_schedule["monthly_cost"] +
                (self.vehicles - 1) * self.fee_schedule["extra_vehicle_fee"])

    def str(self) -> str:
        """Return readable description of student permit"""

        return (f"Student permit for {self.owner_name}: {self.months} month(s), "
                f"{self.vehicles} vehicle(s), cost = ${self.cost(): .2f}")

    def __repr__(self) -> str:
        """Return programmer-styled description of student permit"""

        return (f"StudentPermit({self.owner_name!r}, {self.months!r}, "
                f"{self.fee_schedule!r}, {self.vehicles!r})")

class FacultyPermit(ParkingPermit):
    """Parking Permit for a faculty member, with optional garage access"""

    def __init__(self, owner_name: str, months: int, fee_schedule: dict[str, float], 
                 garage_access: bool) -> None:
        """Create faculty permit with or without garage access

            Preconditions: fee_schedule has 'monthly_cost' and 
            'garage_monthly_cost' entries"""

        super().__init__(owner_name, months, fee_schedule)
        self.garage_access = garage_access

    def cost(self) -> float:
        """Return cost, included garage fees when access is selected"""

        total = self.months * self.fee_schedule["monthly_cost"]
        if self.garage_access:

            total += self.months * self.fee_schedule["garage_monthly_cost"]

        return total

    def __str__(self) -> str:
        """Return readable description of faculty permit"""

        return (f"Faculty permit for {self.owner_name}: {self.months} month(s), "
                f"garage access = {self.garage_access}, cost = ${self.cost(): .2f}")

    def __repr__(self) -> str:
        """Return programmer-styled description of faculty permit"""

        return (f"FacultyPermit({self.owner_name!r}, {self.months!r}, "
                f"{self.fee_schedule!r}, {self.garage_access!r})")

def summarize_list(permits: list[ParkingPermit]) -> float:
    """Print each permit and return combined cost of all permits
    
        Parameter permits is a list containing StudentPermit 
        and/or FacultyPermit objects"""

    total = 0.0
    for permit in permits:
        print(str(permit))
        total += permit.cost()
    return total

def main() -> None:
    """Create permits and demonstrate string and cost methods"""

    student_fees = {"monthly_cost": 25.0, "extra_vehicle_fee": 10.0}
    faculty_fees = {"monthly_cost": 50.0, "garage_monthly_cost": 100.0}

    permits: list[ParkingPermit] = [
        StudentPermit("Ava Patel", 4, student_fees, 2),
        FacultyPermit("Dr. Lee", 4, faculty_fees, True),
        StudentPermit("Noah Kim", 2, student_fees, 1)
    ]

    print("objects (using repr):")
    for permit in permits:
        print(repr(permit))

    print("\nPermit summary (using str):")
    total = summarize_list(permits)
    print(f"Total revenue: ${total: .2f}")

if __name__ == "__main__":
    main()