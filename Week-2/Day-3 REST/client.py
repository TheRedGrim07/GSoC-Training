import requests
BASE_URL = "http://127.0.0.1:5001/students"

def add_data(name,score):
    data={'name':name,'score':score}
    response=requests.post(BASE_URL,json=data)
    print( {"Report":response.status_code,"Response":response.json()})


def delete_name(name):
    data={'name':name}
    response=requests.delete(BASE_URL,json=data)
    print( {"Report":response.status_code,"Response":response.json()})


def get_score(name):
    payload={'name':name}
    response=requests.get(BASE_URL,params=payload)
    print( {"Report":response.status_code,"Response":response.json()})

def verify_deleted(name):
    payload={'name':name}
    response=requests.get(BASE_URL,params=payload)
    if response.status_code==404:
        print(f"Deleated {name} successfully")
    else:
        print("Not Deleted")

if __name__=="__main__":
    add_data("Ayush",86)
    add_data("Bismay",36)
    add_data("tEJAS",46)
    add_data("RoHit",46)
    add_data("tEJAS",66)
    add_data("aYUSH",76)
    add_data("tEJAS",56)
    add_data("tEJAS",66)
    add_data("RoHit",16)

    get_score("tejas")
    delete_name("Tejas")
    verify_deleted("Tejas")
    get_score("Tejas")
    