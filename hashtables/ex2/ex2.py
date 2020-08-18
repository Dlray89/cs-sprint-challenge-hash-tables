class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    memory = {}
    route = [None] * length

    for i in tickets:
        memory[i.source] = i.destination

    next = "NONE"
    for x in range(length):
        if x == 0:
            route[x] = memory[next]
            next = memory[route[x]]
            continue

        route[x] = next
        next = memory[route[x]]

    return route


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

ticket_arr = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(ticket_arr, 8))