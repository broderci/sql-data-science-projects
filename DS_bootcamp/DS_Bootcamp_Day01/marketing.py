import sys

def get_sets():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                   'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                   'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    
    return set(clients), set(participants), set(recipients)

def call_center():
    clients, _, recipients = get_sets()
    return clients - recipients

def potential_clients():
    clients, participants, _ = get_sets()
    return participants - clients

def loyalty_program():
    clients, participants, _ = get_sets()
    return clients - participants

def main():
    if len(sys.argv) != 2:
        return
    
    task = sys.argv[1]
    tasks = {
        'call_center': call_center,
        'potential_clients': potential_clients,
        'loyalty_program': loyalty_program
    }
    
    try:
        result = tasks[task]()
        print('\n'.join(sorted(result)))
    except KeyError:
        raise ValueError("Invalid task name. Use: call_center, potential_clients, loyalty_program")

if __name__ == '__main__':
    main()