mappings = [
        {"Merry":["Mistletoe","Elf","Blitzer","Chesnuts"]},
        {"Red":["Frosty","Goose","Stockings","CandyCane","Mistletoe","Pine","Cedar","Fir","Rudolph","Chesnuts"]},
        {"Green":["Greetings","Goose","CandyCane","Elf","Chesnuts"]},
        {"Wassailing":["Bells","Frosty","Goose","Scrooge","Fruitcake","Pine","Cedar","Fir","Elf","Blitzer","Comet","Cupid","Prancer","Vixen","Chesnuts"]},
        {"Yuletide":["Bells","Candles","Frosty","Goose","Scrooge","Stockings","Fruitcake","Pine","Fir","Lights","Chimney","Comet","Prancer","Vixen","Chesnuts","Cider"]},
        {"Jolly":["Bells","Goose","Scrooge","Stockings","Mistletoe","Pine","Cedar","Icicle","Lights","Elf","Blitzer","Rudolph","Prancer","Vixen","Chesnuts"]},
        {"Reindeer":["Bells","Goose","Stockings","Tidings","Lights","Sleigh","Rudolph","Chesnuts"]},
        {"Caroling":["Bells","Frosty","Goose","Scrooge","Stockings","CandyCane","Fruitcake","Pine","Cedar","Fir","Lights","Elf","Blitzer","Rudolph","Comet","Cupid"]},
        {"Gingerbread":["Holiday","Scrooge","CandyCane","Fruitcake","Pine","Icicle","Chimney","Sleigh"]},
        {"Eggnog":["Frosty","Icicle","Lights","Elf","Prancer","Vixen","Cider"]},
        {"Evergreen":["Bells","Candles","Frosty","Holiday","Goose","Scrooge","Tidings","Fruitcake","Mistletoe","Pine","Cedar","Fir","Elf","Sleigh","Blitzer","Dancer","Dasher","Donner","Prancer","Vixen","Chesnuts","Cider"]}]

def generate_codename(name):
    namehash = hash(name)

    d = mappings[namehash % len(mappings)]
    first = d.keys()[0]
    second = d[first][namehash % len(d[first])]
    
    return first + " " + second
