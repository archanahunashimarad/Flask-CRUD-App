import sqlite3
def get_connection(database):
	try:
		conn = sqlite3.connect(database)

	except Exception as e:
		print(e)
		conn = None

	return conn


def create_tables(database):
	conn = get_connection(database)
	feedbacks_create_query = """
	CREATE TABLE IF NOT EXISTS FEEDBACKS(
										NAME VARCHAR(30),
										EMAIL VARCHAR(50)
										)
 						   """

	if conn is not None:
		conn.execute(feedbacks_create_query)
		conn.commit()
		conn.close()

	return "SUCCESS"

def add_feedback(name, email):
	
	add_feedback_query = """
		INSERT INTO FEEDBACKS(NAME,EMAIL) VALUES(?,?)
	"""
	conn = get_connection("feedbacks.db")
	if conn is not None:
		try:
			conn.execute(add_feedback_query,(name,email))
			conn.commit()		
			status = "SUCCESS"

		except Exception as e:
			print(e)
			status = "FAILURE"

	
		finally:
			conn.close()

	return status


def get_feedbacks():
	query = "SELECT * FROM FEEDBACKS"
	conn = get_connection("feedbacks.db")
	if conn is not None:
		try:
		   customers = conn.execute(query).fetchall()

		except Exception as e:
			print(e)
			customers=[]
		
		finally:
			conn.close()

	return customers

if __name__ == "__main__":
	print(create_tables("feedbacks.db"))
	