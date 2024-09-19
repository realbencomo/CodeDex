class Restaurant:
    name = ""
    typeof = ""
    ratingavg = 0.0
    delivery = True

bobs_burguers = Restaurant()
bobs_burguers.name = "Bob's Burguers"
bobs_burguers.typeof = "American Diner"
bobs_burguers.ratingavg = 4.7
bobs_burguers.delivery = False

krustykrab = Restaurant()
krustykrab.name = "Krusty Krab"
krustykrab.typeof = "Nuclear hellscape - Also a burguer joint"
krustykrab.ratingavg = 1.7
krustykrab.delivery = False

mesontaco = Restaurant()
mesontaco.name = "El mesón del Taco"
mesontaco.typeof = "Taco godsent place"
mesontaco.ratingavg = 5
mesontaco.delivery = "True" 


print(vars(bobs_burguers))
print(vars(krustykrab))
print(vars(mesontaco))