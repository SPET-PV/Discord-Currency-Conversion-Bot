# Built-In Modules
import json
# External Modules
import requests



# ----------------------------------------------------------------------------

def get(from_currency: str,
        to_currency: str,
        amount:str) -> str:
    """Get currency conversion data from the fawazahmed0 API
    and converts an amount from the response data to the target currency.

    Args:
        form_currency (str): The currency to convert from (e.g., 'USD').
        to_currency (str): The currency to convert to (e.g., 'EUR').
        amount (int): The amount to convert.

    Returns:
        str: The converted amount as a formatted string with two 
        decimal places and the date of the rate

    Raises:
        ValueError: If the target currency code does not exist in 
        the response data.
        requests.exceptions.RequestException: If all fallback 
        URLs result in non-200 responses.
    """
    
    # Verification if the currency exist
    with open('currencies.json', 'r') as file:
        currencies = json.load(file)
    from_found = False
    to_found = False
    
    for key, value in currencies.items():
        if value.lower() == from_currency.lower() or key == from_currency.lower():
            from_found = True
            from_currency = key
        elif value.lower() == to_currency.lower() or key == to_currency.lower():
            to_found = True
            to_currency = key
    
    if not (from_found and to_found):
        raise ValueError("The currencies inserted are incorrect.")

    # Fallback System
    urls = [
        f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1\
/latest/currencies/{from_currency}/{to_currency}\
.json',
        f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1\
/latest/currencies/{from_currency}/{to_currency}\
.min.json',
        f'https://raw.githubusercontent.com/fawazahmed0/currency-api\
/1/latest/currencies/{from_currency}/{to_currency}\
.json',
        f'https://raw.githubusercontent.com/fawazahmed0/currency-api\
/1/latest/currencies/{from_currency}/{to_currency}\
.min.json'
    ]

    for url in urls:
        try:
            response = requests.get(url)
            # Raise an exception for non-200 responses
            response.raise_for_status() 
            response_data = response.text
            break
        except requests.exceptions.RequestException as e :
            return f"Error: Failed to retrieve currency data - {e}"
    
    # Convert the string formatted-JSON to a Dictionnary 
    response_dict = json.loads(response_data)
    
    # Calculate the currency conversion result
 
    result = float(amount) * response_dict[to_currency.lower()]
    date = response_dict['date']
    return f'{result:.2f} {date}'



if __name__ == "__main__":
    form_currency = input("from : ")
    to_currency = input("to : ")
    amount = input("amount :")
    values = get(form_currency,to_currency,amount).split()
    # Assign the values to separate variables
    conversion = values[0]
    date = values[1]
    print(f"{conversion} and {date}")
