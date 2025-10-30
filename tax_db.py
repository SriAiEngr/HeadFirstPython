import sqlite3
from pathlib import Path
import datetime

DB_PATH = Path(__file__).parent / 'tax_rates.sqlite3'

def init_db():
    """Create the Tax table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Create Tax table to store province tax rates
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Tax (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        province TEXT UNIQUE,         -- province name (e.g., 'Ontario')
        province_code TEXT,           -- two-letter code (e.g., 'ON')
        tax_percent REAL,            -- stored as number (e.g., 13.0)
        tax_percent_str TEXT,         -- original string (e.g., '13%')
        last_updated TEXT,           -- ISO timestamp
        source TEXT                  -- 'web', 'manual', etc.
    )
    ''')
    
    conn.commit()
    conn.close()

def save_tax_rate(province, tax_percent_str, province_code=None, source='web'):
    """Save or update a province's tax rate.
    
    Args:
        province: Full province name (e.g., 'Ontario')
        tax_percent_str: Tax rate as string (e.g., '13%')
        province_code: Optional two-letter code (e.g., 'ON')
        source: Where this rate came from
    """
    # Clean up the tax percentage (remove % and convert to float)
    try:
        tax_percent = float(tax_percent_str.replace('%', '').strip())
    except ValueError as e:
        raise ValueError(f"Invalid tax percentage '{tax_percent_str}': {e}")
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Use UPSERT (INSERT OR REPLACE) to handle both new and updated rates
    cur.execute('''
    INSERT OR REPLACE INTO Tax 
    (province, province_code, tax_percent, tax_percent_str, last_updated, source)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        province.strip(),
        province_code.strip() if province_code else None,
        tax_percent,
        tax_percent_str.strip(),
        datetime.datetime.utcnow().isoformat(),
        source
    ))
    
    conn.commit()
    conn.close()

def get_tax_rate(province_or_code):
    """Get tax rate for a province (by name or code).
    
    Returns:
        tuple: (tax_percent_str, last_updated) or (None, None) if not found
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Try exact match on province name or code
    cur.execute('''
    SELECT tax_percent_str, last_updated 
    FROM Tax 
    WHERE province = ? OR province_code = ?
    ''', (
        province_or_code.strip(),
        province_or_code.strip().upper()
    ))
    
    result = cur.fetchone()
    conn.close()
    
    return result if result else (None, None)

def list_all_rates():
    """Return all stored tax rates."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # return rows as dict-like objects
    cur = conn.cursor()
    
    cur.execute('''
    SELECT province, province_code, tax_percent_str, last_updated, source
    FROM Tax
    ORDER BY province
    ''')
    
    rows = cur.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

if __name__ == '__main__':
    # Quick demo/test of the functions
    init_db()
    
    # Example: save some tax rates
    save_tax_rate('Ontario', '13%', 'ON')
    save_tax_rate('British Columbia', '12%', 'BC')
    
    # Demo: retrieve and print rates
    print("\nStored tax rates:")
    for rate in list_all_rates():
        print(f"{rate['province']} ({rate['province_code']}): "
              f"{rate['tax_percent_str']} (from {rate['source']} "
              f"on {rate['last_updated']})")
    
    # Demo: look up by code
    tax_str, updated = get_tax_rate('ON')
    if tax_str:
        print(f"\nOntario tax rate: {tax_str} (as of {updated})")