from Keja_Smart.models.database import DatabaseManager

def create_tables():
    house_rent_db = DatabaseManager('house_rent.db')
    tenant_db = DatabaseManager('tenant_data.db')

    house_rent_db.connect()
    tenant_db.connect()

    # Create tables in house_rent.db
    query = '''
    CREATE TABLE IF NOT EXISTS house_rent (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_name TEXT NOT NULL,
        rent_amount REAL NOT NULL
    );
    '''
    house_rent_db.execute_query(query)

    # Create tables in tenant_data.db
    query = '''
    CREATE TABLE IF NOT EXISTS tenants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        move_in_date DATE NOT NULL,
        rent_amount REAL NOT NULL
    );
    '''
    tenant_db.execute_query(query)

    house_rent_db.disconnect()
    tenant_db.disconnect()

if __name__ == '__main__':
    create_tables()
