def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print("Nothing: None", type(object))
        case float() if object != object:
            print("Cheese: nan", type(object))
        case 0 if object is int():
            print("Zero: 0", type(object))
        case '':
            print("Empty:", type(object))
        case False:
            print("Fake: False", type(object))
        case _:
            print("Type not found")
            return 1
    return 0
