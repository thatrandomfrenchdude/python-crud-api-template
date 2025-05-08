from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
import databases
import sqlalchemy

# Define the database connection URL
DATABASE_URL = "postgresql://postgres:password@db/crud_api_template"

# Create a database instance
database = databases.Database(DATABASE_URL)

# Define the metadata for the database tables
metadata = sqlalchemy.MetaData()

# Define the contacts table
contacts = sqlalchemy.Table(
    "contacts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
)

# Create the database engine
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# Initialize the FASTAPI application
app = FastAPI()

# Define the data model for the Contacts table
class Contact(BaseModel):
    id: UUID
    name: str
    phone_number: str

    class Config:
        orm_mode = True

# Create a new contact
@app.post("/contacts/", response_model=Contact)
async def create_contact(contact: Contact):
    # Check if a contact with the same id already exists
    query = contacts.select().where(contacts.c.id == str(contact.id))
    existing_contact = await database.fetch_one(query)
    if existing_contact:
        raise HTTPException(status_code=400, detail="Contact with this ID already exists")

    # Insert the new contact into the database
    query = contacts.insert().values(id=str(contact.id), name=contact.name, phone_number=contact.phone_number)
    await database.execute(query)
    return contact

# Read all contacts
@app.get("/contacts/", response_model=List[Contact])
async def read_contacts():
    # Fetch all contacts from the database
    query = contacts.select()
    contacts_list = await database.fetch_all(query)
    return [Contact(id=UUID(contact["id"]), name=contact["name"], phone_number=contact["phone_number"]) for contact in contacts_list]

# Read a contact by ID
@app.get("/contacts/{contact_id}", response_model=Contact)
async def read_contact(contact_id: UUID):
    # Fetch the contact with the specified ID from the database
    query = contacts.select().where(contacts.c.id == str(contact_id))
    contact = await database.fetch_one(query)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return Contact(id=UUID(contact["id"]), name=contact["name"], phone_number=contact["phone_number"])

# Update a contact
@app.put("/contacts/{contact_id}", response_model=Contact)
async def update_contact(contact_id: UUID, contact: Contact):
    # Fetch the contact with the specified ID from the database
    query = contacts.select().where(contacts.c.id == str(contact_id))
    existing_contact = await database.fetch_one(query)
    if existing_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    # Update the contact in the database
    query = contacts.update().where(contacts.c.id == str(contact_id)).values(name=contact.name, phone_number=contact.phone_number)
    await database.execute(query)
    return contact

# Delete a contact
@app.delete("/contacts/{contact_id}")
async def delete_contact(contact_id: UUID):
    # Fetch the contact with the specified ID from the database
    query = contacts.select().where(contacts.c.id == str(contact_id))
    contact = await database.fetch_one(query)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    # Delete the contact from the database
    query = contacts.delete().where(contacts.c.id == str(contact_id))
    await database.execute(query)
    return {"message": "Contact deleted successfully"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
