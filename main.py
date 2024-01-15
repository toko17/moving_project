from tabulate import tabulate

lists = []

to_do_col = {
    "headers": ["To Do", "Færdig"],
    "data": [
        ["Sorter til loft/kælder", "I jysk og andet"],
        ["Vend badeforhæng", ""],
        ["Sæt billeder op i køkken", ""],
        ["Mål vinduer i soveværelset", ""],
        ["Opsætning af router d.26-27", ""]
    ]
}
lists.append(to_do_col)

shopping_list_col = {
    "headers": ["Shopping List", "Færdig"],
    "data": [
        ["Ledning til lampe 5m", "Virkelig mange dutter"],
        ["Mørklægnings gardiner", "Toilet Børste"],
        ["Tøjskabe", "Badeforhæng"],
        ["Bademåtte", "Opvaske stativ"],
        ["", "Bagepapir"],
        ["", "Bordlampe"],
        ["", "Internet"]
    ]
}
lists.append(shopping_list_col)

#display table

for list in lists:
    print(tabulate(list["data"], headers=list["headers"], tablefmt="fancy_grid"))