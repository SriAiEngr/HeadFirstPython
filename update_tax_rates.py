"""Populate tax database with current rates from the web."""

import fetch_value_from_website
import tax_db

def update_tax_rates():
    """Fetch current tax rates and store them in the database."""
    # Common province codes (add more as needed)
    PROVINCES = {
        'Ontario': 'ON',
        'British Columbia': 'BC',
        'Alberta': 'AB',
        'Manitoba': 'MB',
        'Saskatchewan': 'SK',
        'Quebec': 'QC',
        'Nova Scotia': 'NS',
        'New Brunswick': 'NB',
        'Prince Edward Island': 'PE',
        'Newfoundland and Labrador': 'NL',
        'Northwest Territories': 'NT',
        'Yukon': 'YT',
        'Nunavut': 'NU'
    }
    
    # Initialize the database
    tax_db.init_db()
    updated = 0
    
    # Fetch and store each province's rate
    for province, code in PROVINCES.items():
        try:
            tax_str = fetch_value_from_website.fetch_value_from_website(province)
            if tax_str:
                tax_db.save_tax_rate(province, tax_str, code)
                updated += 1
                print(f"Updated {province}: {tax_str}")
            else:
                print(f"No rate found for {province}")
        except Exception as e:
            print(f"Error updating {province}: {e}")
    
    print(f"\nUpdated {updated} tax rates in the database.")
    print("\nCurrent rates in database:")
    for rate in tax_db.list_all_rates():
        print(f"{rate['province']} ({rate['province_code']}): {rate['tax_percent_str']}")

if __name__ == '__main__':
    update_tax_rates()