from django.shortcuts import render
import psycopg2,sys,os

# Create your views here.


def create_connection():
    conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'),
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASSWORD'),
                            host=os.environ.get('DB_HOST'),
                            port=os.environ.get('DB_PORT'))
    curr = conn.cursor()
    return conn, curr
  
def create_collum():
    try:
        # Get the cursor object from the connection object
        conn, curr = create_connection()
        try:
            # Fire the CREATE query
            curr.execute("ALTER TABLE IF EXISTS app_1_producto\
            ADD COLUMN img bytea;")
              
        except(Exception, psycopg2.Error) as error:
            # Print exception
            print("Error while creating collum table", error)
        finally:
            # Close the connection object
            conn.commit()
            conn.close()
    finally:
        # Since we do not have to do anything here we will pass
        pass 

def write_blob(id,file_path):
    try:
        # Read data from an image file
        drawing = open(file_path, 'rb').read()
        # Read database configuration
        conn, cursor = create_connection()
        try:           
            # Execute the INSERT statement
            # Convert the image data to Binary
            cursor.execute("UPDATE app_1_producto SET img = %s WHERE id=%s",(psycopg2.Binary(drawing),id)) 
            # Commit the changes to the database
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data in Producto table", error)
        finally:
            # Close the connection object
            conn.close()
    finally:
        # Since we do not have to do anything here, we will pass
        pass

# function to store the image which is read from the table
def db_img(data, num):
    # out variable set to null
    out = None
  
    try:
        # creating files in output folder for writing in binary mode
        out = open('media/medios/img'+str(num)+'.jpg', 'wb')
          
        # writing image data
        out.write(data)
          
    # if exception raised
    except IOError:
        sys.exit(1)
          
    # closing output file object
    finally:
        out.close()
  
  
# calling the connect_db function for connection & cursor object
con, cur = create_connection()
try:
    # Cursor object holding all image data from table
    cur.execute("SELECT img FROM app_1_producto")
    for i in range(1, 1):
        
        # fetchone method returns a tuple object of next row of query result set
        # image data is in first column after Select query execution, so [0] index
        data = cur.fetchone()[0]
          
        # the image data is written to file using db_img() for viewing
        db_img(data, i)
except(Exception, psycopg2.Error) as e:
    # Print exception
    print(e)
      
finally:
    # Closing connection
    con.close()
        

#write_blob(1,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\MOUSE.jpg")
#write_blob(2,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\laptop.jpg")
#write_blob(3,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\audifono.webp")
#write_blob(4,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\tarjeta_carton.jpg")
#write_blob(5,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\gameboy.jpg")
#write_blob(6,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\ram.jpg")
#write_blob(7,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\lavadora.jpg")
#write_blob(8,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\jordan.jpg")
#write_blob(9,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\play_5.jpg")
#write_blob(10,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\pc_gamer.jpg")
#write_blob(11,"C:\\Users\\ZeroX\\OneDrive\\Escritorio\\curso python\\modulo 7\\grupal 1\\ABPro-Grupal\\telovendoM7\\media\\medios\\silla.jpg")