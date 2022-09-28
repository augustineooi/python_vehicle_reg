class Vehicle:
    
    # The Vehicle class has three subclasses - Car, Van and Truck.
    # It is responsible for maintaining a vehicle's type, it's VIN and its reservation status
    # (1) miles per gallon, (2) VIN
    # There are 3 subtypes of vehicles (inherited from the vehicle class):
    # (a) Car type: stores (1) max number of passengers, (2) number of doors
    # (b) Van type: stores (1) max number of passengers
    # (c) Truck type: stores (1) length, (2) no. of rooms of storage 
    
    # Attributes:
    def __init__(self, mpg, vin):
        self._mpg = mpg
        self._vin = vin
        self.reserved = False
        self._vtype = "Unknown Vehicle"
        
    # property getter only (mpg)
    @property
    def mpg(self):
        return self._mpg
            
    # property getter only (vin)
    @property
    def vin(self):
        return self._vin
    
    # property getter (reserved)
    @property
    def reserved(self):
        return self._reserved
    
    # property setter (reserved)
    @reserved.setter
    def reserved(self, value):
        if isinstance(value, bool):
            self._reserved = value
    
    # property getter (type)
    @property
    def vtype(self):
        return self._vtype
           
    
    # methods
    
    
    def get_type(self):
        return self.vtype
    
    
    def get_vin(self):
        return self.vin

            

class Car(Vehicle):
    # Car is a sub_type of the Vehicle class
    
    def __init__(self, desc, mpg, passengers, doors, vin):
        super().__init__(mpg, vin)
        self._desc = desc  # description of the vehicle
        self._passengers = passengers # number of passengers
        self._doors = doors # number of doors
        self._vtype = "Car" # Vehicle type is "Car"
            
    # property getter (desc)
    @property
    def desc(self):
        return self._desc
    
    # property getter (passengers)
    @property
    def passengers(self):
        return self._passengers
    
    # property getter (doors)
    @property
    def doors(self):
        return self._doors
    
    # property getter (type)
    @property
    def vtype(self):
        return self._vtype

    

class Van(Vehicle):
    def __init__(self, desc, mpg, passengers, vin):
        super().__init__(mpg, vin)
        self._desc = desc  # description of the vehicle
        self._passengers = passengers # number of passengers
        self._vtype = "Van" # Vehicle type is "Van"
            
    # property getter (desc)
    @property
    def desc(self):
        return self._desc
    
    # property getter (passengers)
    @property
    def passengers(self):
        return self._passengers
    
    # property getter (type)
    @property
    def vtype(self):
        return self._vtype



class Truck(Vehicle):
    def __init__(self, mpg, desc, rooms_storage, vin):
        super().__init__(mpg, vin)
        self._desc = desc  # make/model of the truck
        self._rooms_storage = rooms_storage # number of rooms of storage
        self._vtype = "Truck" # Vehicle type is "Truck"
            
    # property getter (length)
    @property
    def desc(self):
        return self._desc
    
    # property getter (rooms_storage)
    @property
    def rooms_storage(self):
        return self._rooms_storage
    
    # property getter (type)
    @property
    def vtype(self):
        return self._vtype
           
    # def get_type(self):
    #     return self.vtype



class Vehicles:
# The Vehicles class is an aggregator of Vehicle class objects
# It stores the vehicles in a list of vehicle objects
# and contains methods:
# (1) add vehicle objects to the list
# (2) find the list of available vehicles to rent
# (3) reserve and unreserve a particular vehicle within the list of vehicles
    
    def __init__(self):
        # initializing a list to store all available vehicles
        self._vehicles = []
        
    # getter function (vehicles)
    @property
    def vehicles(self):
        return self._vehicles
    
    
    # methods:
    
        
    def get_vehicle_types(self):
        # returns all the types of vehicles stored within the Vehicles object
        vehicle_types = []
        for vehicle in self.vehicles:
            v_type = vehicle.get_type()
            if v_type not in vehicle_types:
                vehicle_types.append(v_type)
        return vehicle_types
    
    
    def get_vehicle(self, vin):
        # check every vehicle's vin
        # if the vin matches, return that vehicle instance
        for vehicle in self.vehicles:
            if vehicle.get_vin() == vin:
                return vehicle
    
        
    def add_vehicle(self, new_vehicle):
        # add a new vehicle to vehicles list
        # assume no duplicate is added
        if isinstance(new_vehicle, Vehicle):
            self.vehicles.append(new_vehicle)
    
    
    def num_avail_vehicles(self, vehicle_type):
        # returns the number of available vehicle given a vehicle type
        counter = 0
        for vehicle in self.vehicles:
            if (vehicle.get_type() == vehicle_type) and (not vehicle.reserved):
                counter += 1
        return counter
    
    
    def get_avail_vehicles(self, vehicle_type):
        # returns a lsit of available vehicles available for rent, given a vehicle type
        avail_vehicles = []
        for vehicle in self.vehicles:
            if (vehicle.get_type() == vehicle_type) and (not vehicle.reserved):
                avail_vehicles.append(vehicle)
        return avail_vehicles


    def reserve_vehicle(self, vin):
        # change reservation status of a vehicle (given the vin) to True
        # within the list of vehicles
        vehicle = self.get_vehicle(vin)
        vehicle.reserved = True

    
    def unreserve_vehicle(self, vin):
        # change the reservation status of a vehicle (given the vin) to False
        # within the list of vehicles
        vehicle = self.get_vehicle(vin)
        vehicle.reserved = False
    
    
    def gen_vehicles_stock_list(self, vehicle_file):
        # this function generates a list of vehicles
        # based on vehicle_file, which is a text (or CSV) file outlining the details of vehicles available for rent
        # this function should be called during the initialization phase of the program
        # to populate the list Vechicles with all available vehicles for rent
        # note that this assumes that at the start of the program, all Reservation statuses of the vehicles are False 
        # (i.e. all are available for rental)
        
        vehicles_raw = []

        f = open(vehicle_file, "r")
        for line in f:
            v = line.strip().split(",")
            vehicles_raw.append(v)
        f.close()

        v_header = vehicles_raw[0]
        v_stock = vehicles_raw[1:]

        # define indices to access vehicle details from the file
        # Vehicle class are defined as follows:
        #      Car(desc, mpg, passengers, doors, vin)
        #      Van(desc, mpg, passengers, vin))
        #      Truck(mpg, desc, rooms_storage, vin)

        type_i = v_header.index("Vehicle Type")
        desc_i = v_header.index("Make/Model")
        mpg_i = v_header.index("Miles per Gallon")
        passengers_i = v_header.index("Num Passengers")
        doors_i = v_header.index("Num Doors")
        rooms_storage_i = v_header.index("Cargo Space")
        vin_i = v_header.index("VIN")

        # populate the vehicles into a Vehicles object
        for v in v_stock:
            if v[type_i] == "Car":
                new_vehicle = Car(v[desc_i], v[mpg_i], v[passengers_i], v[doors_i], v[vin_i])
            elif v[type_i] == "Van":
                new_vehicle = Van(v[desc_i], v[mpg_i], v[passengers_i], v[vin_i])
            elif v[type_i] == "Truck":
                new_vehicle = Truck(v[mpg_i], v[desc_i], v[rooms_storage_i], v[vin_i])

            self.add_vehicle(new_vehicle)
    
    
    def clear_list(self):
        # clear lists for testing purposes only
        self._vehicles = []


                
class VehicleCost:
    # The VehicleCost class defines the cost of a type of Vehicle
    # and includes methods to return each of these cost components 
    
    def __init__(self, daily_rate, weekly_rate, weekend_rate, free_miles, per_mile_chrg, insur_rate):
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate
        self._weekend_rate = weekend_rate
        self._free_miles = free_miles
        self._per_mile_chrg = per_mile_chrg
        self._insur_rate = insur_rate
    
    # setting property getters for vehicle cost attributes
    
    @property
    def daily_rate(self):
        return self._daily_rate
    
    @property
    def weekly_rate(self):
        return self._weekly_rate
    
    @property
    def weekend_rate(self):
        return self._weekend_rate
    
    @property
    def free_miles(self):
        return self._free_miles
    
    @property
    def per_mile_chrg(self):
        return self._per_mile_chrg
    
    @property 
    def insur_rate(self):
        return self._insur_rate
    
    
    # methods
    
    
    def get_daily_rate(self):
        return self.daily_rate
    
    
    def get_weekly_rate(self):
        return self.weekly_rate
    
    
    def get_weekend_rate(self):
        return self.weekend_rate
    
    
    def get_free_miles(self):
        return self.free_miles
    
    
    def get_per_mile_chrg(self):
        return self.per_mile_chrg
    
    
    def get_insur_rate(self):
        return self.insur_rate



class VehicleCosts:
    # The VehicleCosts is an aggregator of the VehicleCost class
    # The different vehicle costs are stored as a list of VehicleCost objectsd
    # It contains methods to add to the VehiclecCosts dictionary, retrieve the cost of a specific vehicle type
    # It also contains a method to caclculate the rental cost based on different input parameters
    # It als includes a method to generate the list of vehicle costs from a flat file (cost_file), which is a text (or csv) file with
    # details separated by commas
    
    
    def __init__(self):
        # initializing a dictionary to store the costs of different vehicle types
        self.vehicle_costs = {}
    
    
    def get_vehicle_cost(self, vehicle_type):
        # returns the cost of a type of vehicle
        # returns the cost as type VehicleCost
        return self.vehicle_costs[vehicle_type]
    
    
    def add_vehicle_cost(self, vehicle_type, vehicle_cost):
        self.vehicle_costs[vehicle_type] = vehicle_cost
    
    
    def calc_rental_cost(self, vehicle_type, rental_period, rental_time, want_insurance, miles_driving):
        v_cost = self.vehicle_costs[vehicle_type]
        
        if rental_period == "Daily":
            rate = v_cost.get_daily_rate()
            rental_days = rental_time
        elif rental_period == "Weekly":
            rate = v_cost.get_weekly_rate()
            rental_days = rental_time * 7
        elif rental_period == "Weekend":
            rate = v_cost.get_weekend_rate()
            rental_days = rental_time
        
        insur_rate = want_insurance * v_cost.get_insur_rate()
        free_miles = v_cost.get_free_miles()
        mileage_rate = v_cost.get_per_mile_chrg()
        chargeable_miles = max(0, miles_driving - free_miles)
        
        rental_cost = rate * rental_time
        insur_cost = insur_rate * rental_days
        mileage_cost = chargeable_miles * mileage_rate
        total_cost = rental_cost + insur_cost + mileage_cost
        
        return (rental_cost, insur_cost, mileage_cost, total_cost, free_miles, mileage_rate)
    
    
    def gen_vehicles_cost_list(self, cost_file):
        # generates the full list of cost files (for all vehicle types)
        
        # list to store the cost details from cost_file
        # cost_file items are separated by commas
        costs_raw = []
        
        f = open(cost_file, "r")
        for line in f:
            c = line.strip().split(",")
            costs_raw.append(c)
        f.close()
        
        c_header = costs_raw[0]
        c_items = costs_raw[1:]
        
        for item in c_items:
            vehicle_type = item[0]
            cost_details = [float(i) for i in item[1:]]        # converting cost details from string to float
            vehicle_cost = VehicleCost(*cost_details)          # create a VehicleCost Class (using the splat function)
            self.add_vehicle_cost(vehicle_type, vehicle_cost) 
    
        
    def clear_list(self):
        # clears the list of costs, for testing purposes only
        self.vehicle_costs = {}
        
        

class Reservation:
    # The Reservation class stores the details of a single customer
    # who has reserved a vehicle
    # Methods within this class returns respective class attributes
    
    def __init__(self, name, address, credit_card, vin):
        self._name = name
        self._address = address
        self._credit_card = credit_card
        self._vin = vin
    
    # getter functions for attributes:
    
    @property
    def name(self):
        return self._name
    
    @property
    def address(self):
        return self._address
    
    @property
    def credit_card(self):
        return self._credit_card
    
    @property
    def vin(self):
        return self._vin
    
    
    # methods
    
    
    def get_name(self):
        return self.name
    
    
    def get_address(self):
        return self.address
    
    
    def get_credit_card(self):
        return self.credit_card
    
    
    def get_vin(self):
        return self.vin



class Reservations:
    # The Reservations class connects reservations to the list of vehicles
    # allows reservations to be made (and added to list of reservation customers)
    # and reservations to be cancelled (removed from the list of reservation customers)
    # as well as finding details of the reservation
    # assumptions:
    #     (1) a credit card can only make one reservation
    #     (2) a person can only make one reservation
    
    
    def __init__(self, vehicles):
        self.vehicles = vehicles   # initialize the class with the existing stock of vehicles
        self.reservations = []     # use a list to track all reservations
        
        
    def get_vin_for_reserve(self, credit_card):
        for resv in self.reservations:
            if resv.credit_card == credit_card:
                return resv.get_vin()
        
            
    def add_reservation(self, new_resv):
        if isinstance(new_resv, Reservation):
            credit_cards_list = self.get_credit_card()
            if new_resv not in credit_cards_list:
                reserved_vin = new_resv.get_vin()           # get the VIN of the newly reserved vehicle
                self.vehicles.reserve_vehicle(reserved_vin) # reserve this vehicle in the vehicles list
                self.reservations.append(new_resv)          # add this reservation to the list of reservations
            else:
                print("A reservation has already been made under this credit card number.")
    
    
    def get_credit_card(self):
        # generates list of credit_cards (this is a 1:1 mapping with the self.reservations list)
        credit_cards_list = []
        for resv in self.reservations:
            credit_cards_list.append(resv.credit_card)
        return credit_cards_list
    
    
    def find_reservation(self, name, addr):
        # retrieve a reservation based on name and address info
        for resv in self.reservations:
            if resv.get_name() == name and resv.get_address() == addr:
                return resv


    def find_reservation_cc(self, credit_card):
        # retrieve a reservation based on credit card info
        for resv in self.reservations:
            if resv.get_credit_card() == credit_card:
                return resv

            
    def cancel_reservation(self, credit_card):
        # function returns None if credit card information is not found in the reservations list
        # we start the check from the end of the list of reservations 
        # (to accommodate the possibility to add multiple bookings from the same credit card in the future)
        credit_cards_list = self.get_credit_card()
        if credit_card in credit_cards_list:
            for (r_index, resv) in enumerate(self.reservations[::-1]):
                if resv.credit_card == credit_card:
                    # if credit card is in the reservation list,
                    # remove this vehicle from reservations list
                    # and update the vehicles list and unreserve this vehicle
                    cancelled_resv = self.reservations.pop(len(self.reservations) - r_index -1)   
                    cancelled_vehicle_vin = cancelled_resv.get_vin()
                    self.vehicles.unreserve_vehicle(cancelled_vehicle_vin)
            return cancelled_resv



class SystemInterface:    
    # the SystemInterface class combines the Vehicles, VehiclesCosts and Reservations Objects
    # and through the RentalAgencyUI, passes inputs to these objects
    # and passes outputs from these objects back to the RentalAgencyUI
    
    def __init__(self):
        self._vehicles = Vehicles()
        self._vehicle_costs = VehicleCosts()
        self._reservations = Reservations(self.vehicles)
    
    # getter functions
    
    @property
    def vehicles(self):
        return self._vehicles
    
    @property
    def vehicle_costs(self):
        return self._vehicle_costs
    
    @property
    def reservations(self):
        return self._reservations
    
    
    # methods
    
    
    def init_SI(self, vehicle_file, cost_file):
        # this function sets up the vehicle stock list and the cost list
        self.vehicles.gen_vehicles_stock_list(vehicle_file)
        self.vehicle_costs.gen_vehicles_cost_list(cost_file)



class RentalAgencyUI:
    # Create the user facing RentalAgencyUI object
    # This object connects with the SystemInterface
    # and contains various methods to retrieve, calculate and display info to the user
    # based on the requirements of the project
    
    # define length (number of characters) of display menu and banners
    menu_length = 80
    banner_length = 100
    
    # set up a dictionary to track reservations and vehicle details
    resv_dict = {}

    
    def __init__(self, vehicle_file, cost_file):
        self._SI = SystemInterface()
        self._SI.init_SI(vehicle_file, cost_file)    # setting up the system with vehicle stock, and vehicle cost data
    
    @property
    def SI(self):
        return self._SI
    
    
    # methods
    
    
    def display_agency_banner(self):
        print("*" * self.menu_length)
        print("*" + "Welcome to Hertzz Rental Agency".center(self.menu_length - 2) + "*".rjust(1))
        print("*" * self.menu_length)
        
    
    def display_menu(self):
        menu = ["Display vehicle types",
               "Check rental costs",
               "Check available vehicles",
               "Get cost of specific rental",
               "Make a reservation",
               "Cancel a reservation",
               "Quit"]
        
        print("<<< MAIN MENU >>>")
        for num, item in enumerate(menu):
            print("{} - {}".format((num + 1), item))
        print("")
    
    
    def new_user_start(self):
        self.display_agency_banner()
        self.start()
    
    
    def start(self):
        
        # steps:
        # 1. Show main menu
        # 2. keep going between different modules within the main menu
        #    until the user decides to Quit
        # 3. Bonus: save the updated vehicles stock list to the file
        
        self.display_menu()
        user_input = input("Enter: ")
        if user_input.isdigit() and int(user_input) in range(1, 8):
            if user_input == "1":
                self.display_veh_types()
            elif user_input == "2":
                self.check_rental_costs()
            elif user_input == "3":
                self.check_avail_veh()
            elif user_input == "4":
                self.get_cost_of_rental()
            elif user_input == "5":
                self.make_reservation()
            elif user_input == "6":
                self.cancel_reservation()
            elif user_input == "7":
                self.quit_UI()
        else:
            print("\nPlease enter a valid choice from the menu below: \n")
            self.start()


    def get_user_v_type_input(self):
        v_types = self.SI.vehicles.get_vehicle_types()
        print("Enter type of vehicle")
        for num, item in enumerate(v_types):
            print("{} - {}".format((num+1), item))
        print("")
        user_input = input("Enter: ")

        if not user_input.isdigit() or int(user_input) not in range(1, 4):
            print("Please enter a valid choice\n")
            self.start()
            return None
        else:
            vehicle = v_types[int(user_input)-1]
            return vehicle
    
    
    def display_veh_types(self):
        banner_txt = " Type of Vehicles Available for Rent "
        filler_len = (self.banner_length - len(banner_txt))//2
        banner = "-" * filler_len + banner_txt + "-" * filler_len
        print(banner)
        
        v_types = self.SI.vehicles.get_vehicle_types()
        for num, item in enumerate(v_types):
            print("{} - {}".format((num+1), item))
        
        
        print("-" * len(banner) + "\n")
        self.start()
    
    
    def check_rental_costs(self):
        
        vehicle = self.get_user_v_type_input()
        
        if vehicle != None:
            # get cost data from the vehicle type
            v_cost = self.SI.vehicle_costs.get_vehicle_cost(vehicle)
            daily = v_cost.get_daily_rate()
            weekly = v_cost.get_weekly_rate()
            weekend = v_cost.get_weekend_rate()
            free_miles = v_cost.get_free_miles()
            per_mile_chrg = v_cost.get_per_mile_chrg()
            daily_insur = v_cost.get_insur_rate()
            
            # print banner
            banner_txt = " Rental Charges for {}s ".format(vehicle)
            filler_len = (self.banner_length - len(banner_txt))//2
            banner = "-" * filler_len + banner_txt + "-" * filler_len
            print(banner)
            
            # print the header
            print("{:15}{:15}{:15}{:15}{:15}{:15}"
                  .format("Daily","Weekly","Weekend","Free Miles", "Per Mile Chrg","Daily Insur."))
            # print the cost data
            print("{:<15.2f}{:<15.2f}{:<15.2f}{:<15.0f}{:<15.2f}{:<15.2f}"
                 .format(daily, weekly, weekend, free_miles, per_mile_chrg, daily_insur))
    
            print("-" * len(banner) + "\n")
            self.start()
    
    
    def avail_veh_info(self, vehicle_type):
        # This function generates a list of text
        # outlining the information of available vechicles
        # based on the different attributes of each vehicle type

        avail_vehicles = self.SI.vehicles.get_avail_vehicles(vehicle_type)
        
        avail_v_list = []
        for v in avail_vehicles:
            model = v.desc
            mpg = v.mpg
            vin = v.vin
            if vehicle_type == "Car":
                passengers = v.passengers
                doors = v.doors
                avail_v_list.append("{:25} passengers: {:4} doors: {:4} mpg: {:5} vin: {}"
                                    .format(model, passengers, doors, mpg, vin))
            elif vehicle_type == "Van":
                passengers = v.passengers
                avail_v_list.append("{:25} passengers: {:4} mpg: {:5} vin: {}"
                                    .format(model, passengers, mpg, vin))
            elif vehicle_type == "Truck":
                storage = v.rooms_storage
                avail_v_list.append("{:25} cargo space: {:4} mpg: {:5} vin: {}"
                                    .format(model, storage, mpg, vin))
        
        return avail_v_list
        
    
    def check_avail_veh(self):
        
        vehicle_type = self.get_user_v_type_input()
        
        if vehicle_type != None:
            avail_vehicles = self.SI.vehicles.get_avail_vehicles(vehicle_type)
    
            # print banner
            banner_txt = " Available {}s ".format(vehicle_type)
            filler_len = (self.banner_length - len(banner_txt))//2
            banner = "-" * filler_len + banner_txt + "-" * filler_len
            print(banner)
            
            # print info on available vehicles
            avail_v_list = self.avail_veh_info(vehicle_type)
            for v in avail_v_list:
                print(v)
            print("")
            
            self.start()
        
    
    def get_cost_of_rental(self):
        
        vehicle_type = self.get_user_v_type_input()
        
        if vehicle_type != None:
            
            # get the desired rental period from user:
            rental_p_l = ["Daily", "Weekly", "Weekend"]
            print("\nEnter the rental period:")
            print("{:15}{:15}{:15}\n".format("1 - Daily", "2 - Weekly", "3 - Weekend"))
            rental_period = input("Enter: ")
            if not rental_period.isdigit() or int(rental_period) not in range(1, 4):
                print("Please enter a valid choice\n")
                self.start()
                return
            else:
                rental_period = rental_p_l[int(rental_period) - 1]
            
            if rental_period in ["Daily", "Weekend"]:
                rental_time = input("\nHow many day(s) do you need the vehicle? ")
            elif rental_period == "Weekly":
                rental_time = input("\nHow many weeks do you need the vehicle? ")
            
            if not rental_time.isdigit():
                print("Please enter valid number of day(s)\n")
                self.start()
                return
            else:
                rental_time = int(rental_time)
                
            want_insurance = input("\nWould you like the insurance? (y/n) ")
            if want_insurance not in ["y", "n"]:
                  print("Please type 'y' or 'n' to indicate if you'd like insurance")
                  self.get_cost_of_rental()
                  return
            else:
                if want_insurance == "y":
                      want_insurance = True
                else:
                      want_insurance = False
                
            miles_driving = input("\nNumber of expected driving miles? ")
            if not miles_driving.isdigit():
                print("Please enter valid number of miles")
                self.get_cost_of_rental()
                return
            else:
                miles_driving = int(miles_driving)
            
            # calculate various costs using the cal_rental_cost() method in vehicle_costs object
            cost = self.SI.vehicle_costs.calc_rental_cost(
                vehicle_type, rental_period, rental_time, want_insurance, miles_driving)
            
            rental_cost = cost[0]
            insur_cost = cost[1]
            mileage_cost = cost[2]
            total_cost = cost[3]
            free_miles = cost[4]
            mileage_rate = cost[5]
            
            # display the cost components
            
            banner_txt = f" Estimated {vehicle_type} Rental Cost "
            filler_len = (self.banner_length - len(banner_txt))//2
            banner = "-" * filler_len + banner_txt + "-" * filler_len
            print("")
            print(banner)
            
            if rental_period == "Daily":
                  r_p_display  = "Day(s)"
            elif rental_period == "Weekly":
                  r_p_display = "Week(s)"
            elif rental_period == "Weekend":
                  r_p_display = "weekend(s)"
                  
            if want_insurance:
                  print(f"{rental_period} rental for {rental_time} {r_p_display} is {rental_cost:,.2f}.")
                  print(f"There is insurance charges of {insur_cost:,.2f}.")
            else:
                  print("* You have opted out of the daily insurance.")
                  print("")
                  print(f"{rental_period} rental for {rental_time} {r_p_display} is {rental_cost:,.2f}.")
            
            print("")
            print(f"Your total cost with an estimated mileage of {miles_driving:,} would be ${total_cost:,.2f}")
            print(f"which include {free_miles:,} free miles and a charge of {mileage_rate:.2f} per mile")
            
            print("-" * len(banner) + "\n")
                  
            self.start()
    
    
    def make_reservation(self):
        # this function allows the user to make a reservation
        # 
        vehicle_type = self.get_user_v_type_input()
        
        if vehicle_type != None:
            
            if self.SI.vehicles.num_avail_vehicles(vehicle_type) == 0:
                # if all vehicles have been reserved
                # stop the reservation process
                print("All {}s have been reserved and there is currently none available for rent.\n".format(vehicle_type))
                self.start()
                return
    
            avail_vehicles = self.SI.vehicles.get_avail_vehicles(vehicle_type)
            
            # display the cost components
            banner_txt = f" Available {vehicle_type}s "
            filler_len = (self.banner_length - len(banner_txt))//2
            banner = "-" * filler_len + banner_txt + "-" * filler_len
            print("")
            print(banner)
            
            # print info on available vehicles
            avail_v_list = self.avail_veh_info(vehicle_type)
            for i, v in enumerate(avail_v_list):
                print("{} - {}".format(i+1, v))
            print("{} *- Back to Main Menu".format(len(avail_vehicles) + 1))
            print("")
    
            
            # get user to select the vehicle to reserve        
            user_resv = input("Enter the number of the vehicle to reserve: ")
            if not user_resv.isdigit() or int(user_resv) not in range(1, len(avail_vehicles) + 2):
                print("Please enter a valid choice\n")
                self.make_reservation()
                return
            else:
                user_resv = int(user_resv)
                
                if user_resv == len(avail_vehicles) + 1:
                    # user has chosen to go back to main menu
                    self.start()
                    return
                
                # print the user's selection
                user_resv_display = avail_v_list[user_resv - 1]
                print(user_resv_display)
                print("")
                
                # get the user's details
                name = input("Enter first and last name: ")
                address = input("Enter address: ")
                credit_card = input("Enter credit card number: ")
                
                # reserve the vehicle selected by the user
                resv_vehicle = avail_vehicles[user_resv - 1]
                resv_vin = resv_vehicle.get_vin()
                self.SI.vehicles.reserve_vehicle(resv_vin)
                
                # create a new reservation object
                new_resv = Reservation(name, address, credit_card, resv_vin)
                
                # add this reservation to the list of reservations
                self.SI.reservations.add_reservation(new_resv)
                self.resv_dict[credit_card] = user_resv_display
                print("\n* Reservation Made *\n")
            
                self.start()
        
        
    def cancel_reservation(self):
        
        print("Cancelling your reservation...")
        cancelled_cc = input("Please enter your credit card number: " )
        
        # get the reservation associated with the credit card
        cancelled_resv = self.SI.reservations.find_reservation_cc(cancelled_cc)
        
        # check to see if reservation under the credit card exists
        if cancelled_resv == None:
            print("Credit card not found.")
            print("Your reservation has not been cancelled.\n")
        else: 
            # if reservation exists, get the relevant info
            cancelled_name = cancelled_resv.get_name()
            cancelled_address = cancelled_resv.get_address()
            cancelled_veh = self.resv_dict[cancelled_cc]
            
            # display the info
            print("")
            print("RESERVATION INFORMATION")
            print(f"Name: {cancelled_name}")
            print(f"Addres: {cancelled_address}")
            print(f"Vehicle: {cancelled_veh}")
            print("")
            
            confirm_cancel = ""
            while confirm_cancel not in ["y", "n"]:
                confirm_cancel = input("Confirm Cancellation (y/n): ")
            
            if confirm_cancel == "y":
                cancelled_resv = self.SI.reservations.cancel_reservation(cancelled_cc)
                cancelled_veh = self.resv_dict.pop(cancelled_cc)
                print("* Reservation Cancelled *\n")
            elif confirm_cancel == "n":
                print(" Cancellation of reservation aborted.")
                print("Returning to main menu.\n")
    
        self.start()

    def quit_UI(self):
        print("")
        print("Thank you for using Hertzz Rental Agency")
        
    
UI = RentalAgencyUI("VehiclesStock.txt", "RentalCost.txt")
UI.new_user_start()
