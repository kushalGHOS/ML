import oracledb as cx_Oracle
import pandas as pd


connStr = 'c##scott/tiger@localhost:1521/xe'


conn = None
try:
   
    conn = cx_Oracle.connect(connStr)

    
    cur = conn.cursor()

    
    dataDf = pd.read_excel("car data.xlsx")

    
    print("Columns in DataFrame:", dataDf.columns)
    print("Data types in DataFrame:", dataDf.dtypes)

    
    required_columns = ["Car_Name", "Year", "Present_Price", "Kms_Driven", "Fuel_Type", "Seller_Type", "Transmission", "Owner", "Selling_Price"]

    
    if not all(col in dataDf.columns for col in required_columns):
        missing_cols = [col for col in required_columns if col not in dataDf.columns]
        print(f"Missing columns in DataFrame: {missing_cols}")
        raise ValueError("DataFrame is missing required columns")

    # Convert columns to appropriate data types if necessary
    dataDf['Car_Name'] = dataDf['Car_Name'].astype(str)
    dataDf['Year'] = dataDf['Year'].astype(int)
    dataDf['Present_Price'] = dataDf['Present_Price'].astype(float)
    dataDf['Kms_Driven'] = dataDf['Kms_Driven'].astype(int)
    dataDf['Fuel_Type'] = dataDf['Fuel_Type'].astype(str)
    dataDf['Seller_Type'] = dataDf['Seller_Type'].astype(str)
    dataDf['Transmission'] = dataDf['Transmission'].astype(str)
    dataDf['Owner'] = dataDf['Owner'].astype(int)
    dataDf['Selling_Price'] = dataDf['Selling_Price'].astype(float)

    
    dataDf = dataDf[required_columns]

    
    dataInsertionTuples = [tuple(x) for x in dataDf.values]
    print("Data insertion tuples prepared:", dataInsertionTuples)

    
    sqlTxt = '''
    INSERT INTO cars
    (car_name, year, present_price, kms_driven, fuel_type, seller_type, transmission, owner, selling_price)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
    '''

    
    cur.executemany(sqlTxt, dataInsertionTuples)

    rowCount = cur.rowcount
    print("Number of inserted rows =", rowCount)

    
    conn.commit()
except Exception as err:
    print('Error while inserting rows into db')
    print(err)
finally:
    if conn:
        # Close the cursor object to avoid memory leaks
        cur.close()
        # Close the connection object also
        conn.close()
print("Data insert example execution complete!")
