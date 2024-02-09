#Basic calculation of the annual inflation rate using the CPI (Consumer Price Index)
#The day I'm posting this on github is 2/9/2024...
# Current CPI = 3.4% | One year ago today CPI = 6.5% 

def calculate_inflation_rate(current_cpi, previous_cpi):
    """
    Our Parameters:
    current_cpi (float): The current CPI value.
    previous_cpi (float): The previous CPI value.
    
    Return:
    (float): The annual inflation rate.
    """
    #Rate of Inflation= (CPIx+1 – CPIx ) / CPIx x100
    #In Python that would look like...
    inflation_rate = ((current_cpi - previous_cpi) / previous_cpi) * 100   
    
    return inflation_rate

# Today's CPI as an example
current_cpi = 3.4
previous_cpi = 6.5

inflation_rate = calculate_inflation_rate(current_cpi, previous_cpi)

print(f"The annual inflation rate is {inflation_rate:.2f}%.")

#Returned:  "The annual inflation rate is -47.69%.""

#[Done] exited with code=0 in 0.107 seconds