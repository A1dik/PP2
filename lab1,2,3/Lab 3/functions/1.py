def grams_to_unc(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = 100 #наше число грам

result = grams_to_unc(grams)

print("{} grams is equal to {} unces".format(grams, result))