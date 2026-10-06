import re


# text = "My number is 0816029844"

# result = re.search(r"081", text)

# # print(result)
# if result:
#     print(result.group())
#     print(result.start())
#     print(result.end())
#     print(result.span())
    
# text = "My number is 08160298440081"

# result = re.match(r"081", text)

# # print(result)
# if result:
#     print(result.group())
#     print(result.start())
#     print(result.end())
#     print(result.span())    


# text = "My number is 08160298440081"

# result = re.findall(r"081", text)

# # print(result)
# if result:
#     print(result.group())
#     print(result.start())
#     print(result.end())
#     print(result.span())    

# text = "My number is 08160298440081"

# results = re.finditer(r"081", text)

# for result in results:
#     print(result)
    
# text = "I love dogs. I pet my dog every day. Dogs are the best"
# pattern = r"[Dd]og"

# corrected = re.sub(pattern, "cat", text)
# print(corrected)

# menu = "Jollof,Fried,Coconut,Ofada"

# items = re.split(r",", menu)
# print(items)

# text = "hat hot hit hut h9t"

# print(re.findall(r"h.t", text))

# re.match(r"^World", "Hello World")

# print(re.findall(r"Jollof|Fried|Coconut", "I Love Jollof rice and Coconut rice"))

# text = "ac abc abbc abbbc"

# print(re.findall(r"ab*c", text))

# text = "color and colour"

# print(re.findall(r"colou?r", text))

# text = "PIN: 1234, Code: 56789"

# print(re.findall(r"\d{4}", text))

# print(re.findall(r"\d{2,4}", "1 22 33 44"))

re.findall(r"#[0-9A-Fa-f]{6}", "")