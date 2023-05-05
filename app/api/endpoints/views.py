import os
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.models.models import PcbSpecs, TestPointList
from api.schemas.schema import PcbSpecsBase, PcbSpecsOutput, TestPointListBase, TestPointListOutput
from config.settings import *

router = APIRouter(
    prefix="/api/v1",
    tags=["API Endpoints"],
)

def get_db():
    """
        This function returns a database session and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/pcb/specs")
async def enter_pcb_specs(payload: PcbSpecsBase, db: Session= Depends(get_db)):
    """
        General information on the PCB size, thickness and panel information (if applicable)
        
        :param payload: The payload parameter is an instance of the PcbSpecsBase class, which contains the
        information about the PCB specifications that are being entered into the database. This information
        includes the PCB information, value, and notes
        :type payload: PcbSpecsBase
        :param db: db is a parameter that represents the database session. It is obtained using the get_db
        function which is a dependency that is injected into the function using the Depends function from
        the FastAPI framework. The database session is used to interact with the database and perform CRUD
        (Create, Read, Update, Delete)
        :type db: Session
        :return: either the newly created `PcbSpecs` object if the try block is successful, or a string
        representation of the exception that occurred if there was an error.
    """
    try:
        query = PcbSpecs(pcb_information=payload.pcb_information, value=payload.value, notes=payload.notes)
        db.add(query)
        db.commit()
        db.refresh(query)
        return query
    except Exception as e:
        return str(e)
   
@router.post("/pcb/test-points")
async def add_test_points_list(payload: TestPointListBase, db: Session= Depends(get_db)):
    """
        List containing the testpoint locations and other information that is needed to create the test fixture.
        
        :param payload: The payload parameter is an instance of the TestPointListBase class, which contains
        the data needed to create a new TestPointList object in the database. This data includes the network
        name, test point name, coordinates, side, type, and hole size
        :type payload: TestPointListBase
        :param db: The "db" parameter is a dependency injection that provides a database session to the
        function. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
        operations. The "Session" type is imported from the SQLAlchemy ORM (Object-Relational Mapping)
        library and
        :type db: Session
        :return: either a TestPointList object if the data was successfully added to the database, or a
        string containing the error message if an exception was raised during the process.
    """
    
    try:
        query = TestPointList(
            net=payload.net,
            name=payload.name,
            x_coord=payload.x_coord,
            y_coord=payload.y_coord,
            side=payload.side,
            type=payload.type,
            hole_size=payload.hole_size,
        )
        db.add(query)
        db.commit()
        db.refresh(query)
        return query
    except Exception as e:
        return str(e)
   