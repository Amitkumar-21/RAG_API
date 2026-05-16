import sqlite3

connection = sqlite3.connect(
    "data/metadata.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    pages INTEGER,
    chunks INTEGER
)
""")

connection.commit()

def save_document_metadata(filename, pages, chunks):

    cursor.execute("""
    INSERT INTO documents (filename, pages, chunks)
    VALUES (?, ?, ?)
    """, (filename, pages, chunks))

    connection.commit()

def get_all_documents():

    cursor.execute("""
    SELECT filename, pages, chunks
    FROM documents
    """)

    rows = cursor.fetchall()

    documents = []

    for row in rows:

        documents.append({
            "filename": row[0],
            "pages": row[1],
            "chunks": row[2]
        })

    return documents

def get_document_count():

    cursor.execute("""
    SELECT COUNT(*) FROM documents
    """)
    count = cursor.fetchone()[0]

    return count