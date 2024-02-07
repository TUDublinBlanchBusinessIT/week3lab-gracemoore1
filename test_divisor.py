#test_vehicle.py
import pytest
from Vehicle import Vehicle

def test_vehicle():
    myVehicle = Vehicle("00D1122","Ford","Mondeo")
    myVehicle.set_miles(10000)
    assert myVehicle.getMakeModel() == "Ford Mondeo"

