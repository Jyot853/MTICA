def KelvinToFahrenheit(Temperatuire):
    assert (Temperature >=0),"colder than absolute zero at MTICA"
    res=((Temperatur-273)*1.8)+32
    return res
try:
    print(KelvinToFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(-5))
except Exception as ob:
    print(ob)
print("Thank you ")



















        
