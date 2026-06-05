def get_objects() -> list[tuple[int, int]]:
    number_of_objects = int(input())
    values_and_weights = [(0, 0)]
    for i in range(number_of_objects):
        input_line = input()
        value, weight = [int(i) for i in input_line.split(" ")]
        values_and_weights.append((value, weight))

    return values_and_weights


def get_clients() -> list[int]:
    number_of_clients = int(input())
    clients_capacity = []
    for i in range(number_of_clients):
        client_capacity = int(input())
        clients_capacity.append(client_capacity)

    return clients_capacity


def get_max_values_table(objets_values_and_weights: list[tuple[int, int]], max_capacity: int) -> list[list[int]]:
    number_of_objects = len(objets_values_and_weights)        
    values_memory = [[0 for u in range(max_capacity+1)] for i in range(number_of_objects)]

    for object_index in range(1, number_of_objects, 1):
        for w in range(1, max_capacity+1, 1):
            object_value, object_weight = objets_values_and_weights[object_index]

            values_memory[object_index][w] = values_memory[object_index-1][w]
            if object_weight <= w:
                new_value = values_memory[object_index-1][w-object_weight] + object_value
                can_add_value = new_value > values_memory[object_index][w]
                if can_add_value:
                    values_memory[object_index][w] = new_value
    return values_memory


def get_max_value(objets_values_and_weights: list[tuple[int, int]], clients_capacity: list[int]):
    max_capacity = max(clients_capacity)
    max_values_per_weight = get_max_values_table(objets_values_and_weights, max_capacity)
    max_value = 0
    for c in clients_capacity:
        max_value += max_values_per_weight[-1][c]

    return max_value


def sale():
    objets_values_and_weights = get_objects()
    clients_capacity = get_clients()
    max_sale_value = get_max_value(objets_values_and_weights, clients_capacity)
    print(max_sale_value)


if __name__ == "__main__":
    number_of_sales = int(input())
    for i in range(number_of_sales):
        sale()
