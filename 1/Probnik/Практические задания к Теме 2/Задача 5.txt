str1 = "Я не могу решить эту сложную задачу"
print(str1.replace("не","").replace("  "," "))
a = str1.split()
print(a[6].replace("у","а").replace("з","З"), a[1], a[5].replace("ую","ая"))