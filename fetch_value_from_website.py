def fetch_value_from_website(state):
    URL = "https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html"
    import gazpacho
    html = gazpacho.get(URL)
    soup = gazpacho.Soup(html)
    tables = soup.find("table")
    rows = tables[0].find("tr",mode="all")
    table = tables[0]
    tax_rates = {}

    for row in table.find("tr", mode="all")[1:]:
        columns = row.find("td" , mode="all")
        province = columns[0].text
        taxPerc = columns[1].text
        #print(f"{province} -> {Tax}")
        tax_rates[province] = taxPerc  # Add to dictionary
        
    #print(tax_rates)

    #if province == "Alberta":
    # If the state exists in the dictionary, return its tax rate
    if state in tax_rates:
        return tax_rates[state]
    return None
            
#print(fetch_value_from_website("Alberta"))