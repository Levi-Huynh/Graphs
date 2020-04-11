import time
import random
from util import Stack, Queue
"""
nodes: users
edges: friendships
undirected: friends relationship 2 way.. Cyclic
shortest path being asked,  BFT/BFS

hint:
-Think relationships/adj list
-avg: total number for friendships / total users
    - 10 users, 2 friends each ==> 20 total friendships
"""


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):  # loooks like adjacency list
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            # undirectional. add friends_id here to this user_id key in friendship set
            self.friendships[user_id].add(friend_id)
            # adds friends/ user_id to this friend_id key in friendships set
            self.friendships[friend_id].add(user_id)
            # this is why we half, were creatingin bidrection for this function/ creating 2 friendships
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        # in set of self.users key is user_id, value is Username
        self.users[self.last_id] = User(name)
        # in set friendships, create a new set for the [user_id] key
        self.friendships[self.last_id] = set()

    # writing var more explicitly helps see new maneuvers
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(num_users):
            self.add_user(f"User{i+1}")  # add a user for len of num_user arg
        possible_friendshps = []
        for user_id in self.users:  # for each id in self.user set {}
            # self.user set {} has last_id as [key]
            # 1-2, 1-3, 1-4, 1-5, 1-6, ... 1-10 ,// 2-3, 2-5, 2-6, 2-7 ..//3-4, 3-5, 3-6, 2-7
            # #becomes half of list, and one num later in range. for permutations we dont need repeats, start at next num
            # for every user_id in self.users set{}, range starts at the next user id (dont need duplicates), and range ends at the last_id +1 (since index starts 0)
            for friend_id in range(user_id + 1, self.last_id+1):
                # append the user id for each user in self.users (all users) set {}, & append its friend_id to possible
                possible_friendshps.append((user_id, friend_id))
                # ^ this is literally every possible friendship
        print("unrandom all possible", possible_friendshps)
        # random distribution, 1 users with no or few, 1 users with many
        # O(n) for shuffle
        random.shuffle(possible_friendshps)
        print("randommized order", possible_friendshps)
        # slice off right amount/ half
        # everytime creating friendship (you're creating 2 friendships)
        # slice off first 10 from list
        # create n friendships where n = avg_friendships * num_users //2
        # avg _friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users

        # half b/c for each add frienship operation we created bidirectional/2 friendships  #range here is is the average
        for i in range(num_users * avg_friendships // 2):
            # set temp var to possibl_frienships[i] (as iterates through this list)
            friendship = possible_friendshps[i]
            # add frienship(element[0], element[1]) to actualy __create__ the friendships
            self.add_friendship(friendship[0], friendship[1])
        print("halved possible random", possible_friendshps)

        # n * (n/2) = .5 * n^2 = O(n^2)

        # Add users
        # write a for loop that calls create user the right amount of times
        # Create friendships
        # create list of all poss firendship combinations
        # shuffle the list, then grab the first N elements from the list
        # youll need to import random to shuffle

    """
    stretch: O(n) for populate graph 
    """

    def pop_graph_linear(self, num_users, avg_friendships):
        # pick random user
        # pick another random user
        # try to create the friendship
        # if it works increment the counter
        # if not, try again

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(num_users):
            self.add_user(f"User{i+1}")  # add a user for len of num_user arg

        target_friendships = num_users * avg_friendships

        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, num_users)
            friend_id = random.randint(1, num_users)

            if self.add_friendship(user_id, friend_id):
                # if it works, increment counter
                total_friendships += 2
            else:
                collisions += 1
        print(
            f"Total frienships {total_friendships}, total collisions {collisions}")

    def get_all_social_paths(self, user_id):
        """

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.


        BFS

        The key is the friend's ID and the value is the path.

        visited[user_id] : [path to 1] #user_id
        """

        visited = {}
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            print("path", path)
            user = path[-1]
            print("user", user)
            if user not in visited.keys():
                visited[user] = path
                print("visited", visited)
            for friend in self.friendships[user]:
                # * lets you put anything in & copies what was path above
                newPath = [*path, friend]
                print("newpath", newPath, "friend", friend, "user", user)
                # only add to ENQUEUE if friend of user is not in visited key
                if friend not in visited.keys():
                    q.enqueue(newPath)
                    print("its ok to not use everything in queue", q)
                elif len(newPath) < len(visited[friend]):
                    print(
                        f"added new path for {friend} to {visited} using {newPath}")
                    visited[friend] = newPath
        return visited


if __name__ == '__main__':
    num_users = 2000
    # doubling num of friendships should quadruple len of quad pop, and only double linear
    avg_friendships = 5
    # sparse = very low num of edges to nodes  (LINEAR WILL PERFORM FASTER THAN QUADRATIC)
    # dense = high or equal num of edges to nodes (LINEAR WILL PERFORM SLOWER THAN QUAD, which may actually grow linearly,
    # )
    # ^ when num of friendships and num of users are close (due to friendship collision)
    # when downside to randdom with dense graphs may have lots of collision
    # linear can be twenty times more than Quad if completely dense
    # randomness may not be deterministic
    # sometimes instead of racking brain, try?
    sg = SocialGraph()
    start_time = time.time()
    sg.pop_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    print(f"O(n^2) quadratic pop: {end_time- start_time} secs")
    print("----")

    start_time = time.time()
    sg.pop_graph_linear(10, 2)
    end_time = time.time()
    print(f"Linear pop: {end_time- start_time} secs")
    #print("friend", sg.friendships)
    #connections = sg.get_all_social_paths(1)
    #print("friendships", sg.friendships)
    # print(connections)


# stretch create O(n) solution to populate_graph() which is currently O(n^2)

# O(n) solution risks longer (or infinite) runtime when number of friendships d number of users are close
# (due to the friendship collision)

# can do a check for density then perform quad, versus linear graph population
