txt = input("Ingrese un texto: ")
let_1 = input("Ingrese la primera letra: ")
let_2 = input("Ingrese la segunda letra: ")
let_3 = input("Ingrese la tercera letra: ")

txt_low = txt.lower()
let_1_low = let_1.lower()
let_2_low = let_2.lower()
let_3_low = let_3.lower()

ocurr_let_1 = txt_low.count(let_1_low)
ocurr_let_2 = txt_low.count(let_2_low)
ocurr_let_3 = txt_low.count(let_3_low)

print(f"La letra {let_1} aparece en el texto {ocurr_let_1} veces.")
print(f"La letra {let_2} aparece en el texto {ocurr_let_2} veces.")
print(f"La letra {let_3} aparece en el texto {ocurr_let_3} veces.")

len_txt = len(txt)
print(f"El texto tiene {len_txt} caracteres incluyendo espacios.")

list_txt = txt.split()
len_list_txt = len(list_txt)
print(f"El texto tiene {len_list_txt} palabras.")

print(f"Primera letra del texto: {txt[0]}.")
print(f"Ultima letra del texto: {txt[-1]}.")

reversed_txt_list = list_txt[::-1]
reversed_txt_str = " ".join(reversed_txt_list)
print(f"El texto revertido: \"{reversed_txt_str}\".")

sub_str = "Python"
if sub_str in txt_low:
    print("La palabra \"Python\" esta en el texto.")
else:
    print("La palabra \"Python\" no fue encontrada en el texto.")
