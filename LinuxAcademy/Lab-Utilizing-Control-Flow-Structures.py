todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    
def take_first(todos):
    """
    take_first receives a list of todos and removes the first todo
    and returns that todo and the remaining todos in a tuple

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
    >>> todos
    [{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todos = []
    >>> take_first(todos)
    (None, [])
    """
    if todos:
        todo = todos.pop(0)
        return (todo, todos)
    else:
        return (None, todos)

print(take_first(todos))

todo = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'},
{'name': 'Task 3', 'body': 'Third task', 'points': '5'}]

def sum_points(todo):
    """
    sum_points receives two todo dictionaries and returns the sum of their `point` values.

    >>> todo = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'},
    ... {'name': 'Task 3', 'body': 'Third task', 'points': '5'}]
    >>> sum_points(todos)
    10
    """
    total = 0
    for item in todo:
        total += int(item['points'])
    return total

print(sum_points(todo))