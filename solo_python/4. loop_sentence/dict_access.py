# 딕셔너리 선언
dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "orgin":"필리핀"
}

# 출력
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())
print("name", dictionary["name"])
print("type", dictionary["type"])
print("ingredient", dictionary["ingredient"])
print("orgin", dictionary["orgin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])


name = "이름"
dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}
print(dict_key)