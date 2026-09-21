import csv

def add_user(sn, username, fullname):
    """Adds new user to social network"""

    try: 
        if username in sn: #if username already in use
            return False

        sn[username] = (fullname, []) # new user with no friends
        return True

    except:
        print("Username already taken.")
        raise

def add_friend(sn, user1, user2):
    """Adds mutual friend link between users"""

    try:
        if user1 not in sn or user2 not in sn: #if either user not in network
            return False

        if user1 == user2: #stop user from adding themself as friend
            return False

        if user2 not in sn[user1][1]: # add user2 to user1 friend list
            sn[user1][1].append(user2)

        if user1 not in sn[user2][1]: #add user1 to user2 friend list
            sn[user2][1].append(user1)

        return True

    except:
        print("Username not found in network.")
        raise

def get_friends(sn, user1, distance):
    """Return users friends within given distance"""

    try:
        if user1 not in sn or distance <= 0: #if user not in network or distance is negative
            return []

        friends       = []      #list of friends within distance
        visited       = [user1] #users already visited
        current_level = [user1] #users at current distance

        for level in range(distance): # search for friends within distance
            next_level = []

            for user in current_level:      #for each user at current distance, get friends
                for friend in sn[user][1]:  #check each friend of user

                    if friend not in visited: #add to friends list if not visited
                        visited.append(friend)
                        friends.append(friend)
                        next_level.append(friend)

            current_level = next_level

            if len(current_level) == 0: #stop if no more users
                break

        return friends

    except: 
        print("An error occurred while finding friends.")
        raise

def save_network(filename, sn):
    """Saves network to a CSV file"""

    try: 
        with open(filename, "w", newline="") as file: #open file for writing
            writer = csv.writer(file)

            for username in sn:             #write each user and their friends to the file
                fullname = sn[username][0]
                friends  = sn[username][1]

                row = [username, fullname]  

                for friend in friends:
                    row.append(friend)

                writer.writerow(row)

    except:
        print("Error occurred while saving network.")
        raise

def load_network(filename):
    """Loads network from csv file"""

    try:
        sn = {} #dictionary to hold social network data

        with open(filename, "r", newline="") as file: #open file for reading
            reader = csv.reader(file)

            for row in reader:      #read each row from file
                username = row[0]
                fullname = row[1]

                friends  = []      #store friends in list 

                for i in range(2, len(row)):
                    friends.append(row[i])

                sn[username] = (fullname, friends) #add user and friends to social network

        return sn

    except:
        print("Error occurred loading network")
        raise

def main():

    try:
        # example sn from assignment
        sn = {
            'alice': ('Alice Smith', ['maria']),
            'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
            'joe': ('Joseph Adams', ['maria', 'eve']),
            'eve': ('Evelyn Cooper', ['joe']),
            'david': ('David Benson', ['maria'])
        }

        #testing
        print("Original network:\n", sn, "\n") #original network

        #add user test
        print(add_user(sn,"bob", "Bobby Brown"),"\n", sn, "\n")

        #test duplicated user and names
        print(add_user(sn,"alice", "Alice Smith"),"\n", sn, "\n")

        #test add friend
        print(add_friend(sn, "bob", "alice"), "\n", sn, "\n")

        #test friend distance
        print("Alice friend distance at distance 1: ")
        print(get_friends(sn, "alice", 1), "\n")
        print("Alice friend distance at distance 2: ")
        print(get_friends(sn, "alice", 2), "\n")

        #test invalid username
        print(get_friends(sn, "unknown", 2), "\n")

        #save test
        print("Saving network...")
        save_network("social_network.csv", sn)
        print("Network saved.")

        #load test
        print("Loading Network...")
        loaded_network = load_network("social_network.csv")
        print("Network Loaded", "\n")

    except:
        print("Error occurred while testing network features.")
        raise

main()