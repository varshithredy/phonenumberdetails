# Dictionary mapping country codes to country information
country_data = {
    '+1': {'timezone': 'US/Pacific', 'country': 'United States'},
    '+44': {'timezone': 'Europe/London', 'country': 'United Kingdom'},
    '+91': {'timezone': 'Asia/Kolkata', 'country': 'India'},
    # Add more country data as needed
}

def get_country_info(country_code):
    return country_data.get(country_code, {})

def main():
    mobileNo = input("Enter Phone number with country code(+xx xxxxxxxxx):")
    service_provider = input("Enter Service Provider Name:")
    
    # Extract the country code from the input
    country_code = mobileNo.split()[0]
    
    country_info = get_country_info(country_code)
    
    if country_info:
        print('Phone Number belongs to region:', country_info['timezone'])
        print('Phone number belongs to country:', country_info['country'])
        print('Service Provider:', service_provider)
    else:
        print("Please enter a valid mobile number")

if __name__ == "__main__":
    main()
