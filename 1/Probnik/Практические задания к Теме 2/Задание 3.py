str2 = ("Я.внима?тельноне_слушал учителя.и?не_понял.всё!!!")
a = str2.replace("_"," ").replace(".", " ").replace("?","").replace("!!!","!").replace("!!!","!").replace("ине","и не")
print(a)