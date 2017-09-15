ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 14,
    },{
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    },{
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan,darja]
def AdultKids(emp):
    for i in emp:
        for j in i["children"]:
            if j["age"]>18:
                print (i["name"])
                break
AdultKids(emps)