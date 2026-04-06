import pandas as pd
fruit = ["mangos", "bananas", "hastag", "fruit"]
marke = ["tengelmann", "dm", "edeka", "rewe"]
frische = [0, 5, 7, 2]
df = pd.DataFrame({
    "Früchte" : fruit,
    "marke" : marke,
    "frischeskala" : frische

})
