
def menu():
    print("1. Normal Calculator")
    print("2. Scientific Calculator")
    print("3. Graphing Calculator")
    print("4. Solving The Roots Of Equations")
    print("5. Geometry")
    print("6. Unit Converter")
    print("7. Exit")
    chos = input("Enter The Type of calculator you want:")
    if chos == "1":
        normal()
    elif chos == "2":
        scientific()
    elif chos == "3":
        graphingcalc()
    elif chos == "4":
        rootsolve()
    elif chos == "5":
        geometry()
    elif chos == "6":
        uc()    
    elif chos == "7":
        exit()
    else:
        menu()
def uc():
    print("Welcome to Unit Solver")
    print("1. Multiples Of SI units")
    print("2. Length")
    print("3. Area")
    print("4. Temperature")
    print("5. Kinematic Viscocity")
    print("6. Dynamic Viscocity")
    print("7. Volumetric Gas Flow")
    print("8. Torque")
    print("9. Mass Flow")
    print("10. Density")
    print("11. Mass")
    print("12. Speed")
    print("13. Volume")
    print("14. Electric Force")
    print("15.Gravitational Force")
    print("16. Exit")
    dex = input("Which function do you want:")
    if dex == "1":
        print("Check the file named multiconv.txt")
        unitmenu()
    elif dex == "2":
        length()
    elif dex == "3":
        area()
    elif dex == "4":
        temperature()
    elif dex == "5":
        kinematicviscosity()
    elif dex == "6":
        dynamicviscosity()
    elif dex == "7":
        volumetricgasflow()
    elif dex == "8":
        torque()
    elif dex == "9":
        massflow()
    elif dex == "10":
        density()
    elif dex == "11":
        mass()
    elif dex == "12":
        speed()
    elif dex == "13":
        volume()
    elif dex == "14":
        elec()
    elif dex == "15":
        gravity()        
    else:
        exit()
def gravity():
    m1=float(input("Enter the first mass: "))
    m2=float(input("Enter the second mass: "))
    r=float(input("Enter the distance between the centres of the masses: "))
    G=6.673*(10**-11)
    f=(G*m1*m2)/(r**2)
    print("Hence, the gravitational force is: ",f,"N")
    msg = input("1. Go Back 2. Recalculate:")
    if msg == "1":
            uc()
    else:
            gravity()   
    gravity()
def elec():
    c1=float(input("Enter the first charge: "))
    c2=float(input("Enter the second charge: "))
    r=float(input("Enter the distance between the centres of the charges: "))
    K=8.9875517923*(10**9)
    f=(K*c1*c2)/(r**2)
    print("Hence, the electrostatic force is: ",f,"N","m^2","C^-2")
    msg = input("1. Go Back 2. Recalculate:")
    if msg == "1":
            uc()
    else:
         elec()
def length():
    print("Which unit do you have:")
    print("1. Millimeters\n"
          "2. Centimeters\n"
          "3. Meters\n"
          "4. Kilometers\n"
          "5. Inches\n"
          "6. Feet\n"
          "7. Yards\n"
          "8. Miles\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        unit1 = 1
        unit2 = 0.1
        unit3 = 0.01
        unit4 = 0.000001
        unit5 = 0.03937
        unit6 = 0.003281
        unit7 = 0.001094
        unit8 = 6.21e-07
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "2":
        unit1 = 10
        unit2 = 0.01
        unit3 = 1
        unit4 = 0.00001
        unit5 = 0.393701
        unit6 = 0.032808
        unit7 = 0.010936
        unit8 = 0.000006
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "3":
        unit1 = 1000
        unit2 = 100
        unit3 = 1
        unit4 = 0.001
        unit5 = 39.37008
        unit6 = 3.28084
        unit7 = 1.093613
        unit8 = 0.000621
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "4":
        unit1 = 1000000
        unit2 = 100000
        unit3 = 1000
        unit4 = 1
        unit5 = 39370.08
        unit6 = 3280.84
        unit7 = 1093.613
        unit8 = 0.621371
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "5":
        unit1 = 25.4
        unit2 = 2.54
        unit3 = 0.0254
        unit4 = 0.000025
        unit5 = 1
        unit6 = 0.083333
        unit7 = 0.027778
        unit8 = 0.000016
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "6":
        unit1 = 304.8
        unit2 = 30.48
        unit3 = 0.3048
        unit4 = 0.000305
        unit5 = 12
        unit6 = 1
        unit7 = 0.333333
        unit8 = 0.000189
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "7":
        unit1 = 914.4
        unit2 = 91.44
        unit3 = 0.9144
        unit4 = 0.000914
        unit5 = 36
        unit6 = 3
        unit7 = 1
        unit8 = 0.000568
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
    elif index == "8":
        unit1 = 1609344
        unit2 = 160934.4
        unit3 = 1609.344
        unit4 = 1.609344
        unit5 = 63360
        unit6 = 5280
        unit7 = 1760
        unit8 = 1
        print("in MM is:"+str(value * unit1))
        print("in CM is:"+str(value * unit2))
        print("in M is:"+str(value * unit3))
        print("in KM is:"+str(value * unit4))
        print("in INCH is:"+str(value * unit5))
        print("in FEET is:"+str(value * unit6))
        print("in YARD is:"+str(value * unit7))
        print("in MILE is:"+str(value * unit8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            length()
def area():
    print("Which unit do you have:")
    print("1. Millimeter square\n"
          "2. Centimeter square\n"
          "3. Meter square\n"
          "4. Inches square\n"
          "5. Feet square\n"
          "6. Yards square\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        unit1 = 1
        unit2 = 0.01
        unit3 = 0.000001
        unit4 = 0.00155
        unit5 = 0.000011
        unit6 = 0.000001
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()
    elif index == "2":
        unit1 = 100
        unit2 = 1
        unit3 = 0.0001
        unit4 = 0.155
        unit5 = 0.001076
        unit6 = 0.00012
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()

    elif index == "3":
        unit1 = 1000000
        unit2 = 10000
        unit3 = 1
        unit4 = 1550.003
        unit5 = 10.76391
        unit6 = 1.19599
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()

    elif index == "4":
        unit1 = 645.16
        unit2 = 6.4516
        unit3 = 0.000645
        unit4 = 1
        unit5 = 0.006944
        unit6 = 0.000772
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()

    elif index == "5":
        unit1 = 92903
        unit2 = 929.0304
        unit3 = 0.092903
        unit4 = 144
        unit5 = 1
        unit6 = 0.111111
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()

    elif index == "6":
        unit1 = 836127
        unit2 = 8361.274
        unit3 = 0.836127
        unit4 = 1296
        unit5 = 9
        unit6 = 1
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            area()
def temperature():
    print("Choose the unit given")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Celsius is:" + str(value))
        print("In Fahrenheit is:" + str((value * 9/5) + 32))
        print("In Kelvin is:" + str(value + 273.15))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            temperature()
    elif index == "2":
        print("In Celsius is:" + str((value-32)*(5/9)))
        print("In Fahrenheit is:" + str(value))
        print("In Kelvin is:" + str((value + 459.67)/1.8))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            temperature()
    elif index == "3":
        print("In Celsius is:" + str(value - 273.15))
        print("In Fahrenheit is:" + str((1.8 * value) - 459.67))
        print("In Kelvin is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            temperature()
def kinematicviscosity():
    print("Choose the unit given")
    print("1. Centistroke")
    print("2. Stroke")
    print("3. Foot square / second")
    print("4. Metre square / second")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Centistroke is:" + str(value))
        print("In Stroke is:" + str(value * 0.01))
        print("In Foot Square / sec is:" + str(value * 0.00001))
        print("In Metre square / sec is:" + str(value * 0.000001))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            kinematicviscosity()
    elif index == "2":
        print("In Centistroke is:" + str(value * 100))
        print("In Stroke is:" + str(value))
        print("In Foot Square / sec is:" + str(value * 0.001076))
        print("In Metre square / sec is:" + str(value * 0.0001))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            kinematicviscosity()
    elif index == "3":
        print("In Centistroke is:" + str(value * 92903))
        print("In Stroke is:" + str(value * 929.03))
        print("In Foot Square / sec is:" + str(value))
        print("In Metre square / sec is:" + str(value * 0.092903))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            kinematicviscosity()
    elif index == "4":
        print("In Centistroke is:" + str(value * 1000000))
        print("In Stroke is:" + str(value * 10000))
        print("In Foot Square / sec is:" + str(value * 10.76392))
        print("In Metre square / sec is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            kinematicviscosity()
def dynamicviscosity():
    print("Choose the unit given")
    print("1. Centipoise")
    print("2. Poise")
    print("3. Pound square/ sec")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Centipoise is:" + str(value))
        print("In Poise is:" + str(value * 0.01))
        print("In Pound square/ sec is:" + str(value * 0.000672))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            dynamicviscosity()
    elif index == "2":
        print("In Centipoise is:" + str(value * 100))
        print("In Poise is:" + str(value))
        print("In Pound square/ sec is:" + str(value * 0.067197))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            dynamicviscosity()
    elif index == "3":
        print("In Centipoise is:" + str(value * 1488.16))
        print("In Poise is:" + str(value * 14.8816))
        print("In Pound square/ sec is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            dynamicviscosity()
def volumetricgasflow():
    print("Choose the unit given")
    print("1. Normal metre cube/hour")
    print("2. Standard cubic feet/hour")
    print("3. Standard cubic feet/minute")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Normal metre cube/hour is:" + str(value))
        print("In Standard cubic feet/hour is:" + str(value * 35.31073))
        print("In Standard cubic feet/minute is:" + str(value * 0.588582))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volumetricgasflow()
    elif index == "2":
        print("In Normal metre cube/hour is:" + str(value * 0.02832))
        print("In Standard cubic feet/hour is:" + str(value))
        print("In Standard cubic feet/minute is:" + str(value * 0.016669))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volumetricgasflow()
    elif index == "3":
        print("In Normal metre cube/hour is:" + str(value * 1.699))
        print("In Standard cubic feet/hour is:" + str(value * 59.99294))
        print("In Standard cubic feet/minute is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volumetricgasflow()
def torque():
    print("Choose the unit given")
    print("1. Newton metre")
    print("2. Kilogram force metre")
    print("3. Foot pound")
    print("4. Inch pound")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Newton metre is:" + str(value))
        print("In Kilogram force metre is:" + str(value * 0.101972))
        print("In Foot pound is:" + str(value * 0.737561))
        print("In Inch pound is:" + str(value * 8.850732))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            torque()
    elif index == "2":
        print("In Newton metre is:" + str(value * 9.80665))
        print("In Kilogram force metre is:" + str(value))
        print("In Foot pound is:" + str(value * 7.233003))
        print("In Inch pound is:" + str(value * 86.79603))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            torque()
    elif index == "3":
        print("In Newton metre is:" + str(value * 1.35582))
        print("In Kilogram force metre is:" + str(value * 0.138255))
        print("In Foot pound is:" + str(value))
        print("In Inch pound is:" + str(value * 12))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            torque()
    elif index == "4":
        print("In Newton metre is:" + str(value * 0.112985))
        print("In Kilogram force metre is:" + str(value * 0.011521))
        print("In Foot pound is:" + str(value * 0.083333))
        print("In Inch pound is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            torque()
def massflow():
    print("Choose the unit given")
    print("1. Kilogram/hour")
    print("2. Pound/hour")
    print("3. Kilogram/second ")
    print("4. Ton/hour")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Kilogram/hour is:" + str(value))
        print("In Pound/hour is:" + str(value * 2.204586))
        print("In Kilogram/second  is:" + str(value * 0.000278))
        print("In Ton/hour is:" + str(value * 0.001))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            massflow()
    elif index == "2":
        print("In Kilogram/hour is:" + str(value * 0.4536))
        print("In Pound/hour is:" + str(value))
        print("In Kilogram/second  is:" + str(value * 0.000126))
        print("In Ton/hour is:" + str(value * 0.000454))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            massflow()
    elif index == "3":
        print("In Kilogram/hour is:" + str(value * 3600))
        print("In Pound/hour is:" + str(value * 7936.508))
        print("In Kilogram/second  is:" + str(value))
        print("In Ton/hour is:" + str(value * 3.6))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            massflow()
    elif index == "4":
        print("In Kilogram/hour is:" + str(value * 1000))
        print("In Pound/hour is:" + str(value * 2204.586))
        print("In Kilogram/second  is:" + str(value * 0.277778))
        print("In Ton/hour is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            massflow()
def density():
    print("Choose the unit given")
    print("1. Gram/millilitre")
    print("2. Kilogram/metre cube")
    print("3. Pound/foot cube ")
    print("4. Pound/inch cube")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Gram/millilitre is:" + str(value))
        print("In Kilogram/metre cube is:" + str(value * 1000))
        print("In Pound/foot cube  is:" + str(value * 62.42197))
        print("In Pound/inch cube is:" + str(value * 0.036127))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            density()
    elif index == "2":
        print("In Gram/millilitre is:" + str(value * 0.001))
        print("In Kilogram/metre cube is:" + str(value))
        print("In Pound/foot cube  is:" + str(value * 0.062422))
        print("In Pound/inch cube is:" + str(value * 0.000036))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            density()
    elif index == "3":
        print("In Gram/millilitre is:" + str(value * 0.01602))
        print("In Kilogram/metre cube is:" + str(value * 16.02))
        print("In Pound/foot cube  is:" + str(value))
        print("In Pound/inch cube is:" + str(value * 0.000579))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            density()
    elif index == "4":
        print("In Gram/millilitre is:" + str(value * 27.68))
        print("In Kilogram/metre cube is:" + str(value * 27680))
        print("In Pound/foot cube  is:" + str(value * 1727.84))
        print("In Pound/inch cube is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            density()
def mass():
    print("Which unit do you have:")
    print("1. Grams\n"
          "2. Kilograms\n"
          "3. Metric tonnes\n"
          "4. Short ton\n"
          "5. Long ton\n"
          "6. Pounds\n"
          "7. Ounces\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":

        print("in Grams is:" + str(value))
        print("in Kilograms is:" + str(value * 0.001))
        print("in Metric tonnes is:" + str(value * 0.000001))
        print("in Short ton is:" + str(value * 0.000001))
        print("in Long ton is:" + str(value * 9.84e-07))
        print("in Pounds is:" + str(value * 0.002205))
        print("in Ounces is:" + str(value * 0.035273))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "2":

        print("in Grams is:" + str(value * 1000))
        print("in Kilograms is:" + str(value))
        print("in Metric tonnes is:" + str(value * 0.001))
        print("in Short ton is:" + str(value * 0.001102))
        print("in Long ton is:" + str(value * 0.000984))
        print("in Pounds is:" + str(value * 2.204586))
        print("in Ounces is:" + str(value * 35.27337))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "3":

        print("in Grams is:" + str(value * 1000000))
        print("in Kilograms is:" + str(value * 1000))
        print("in Metric tonnes is:" + str(value))
        print("in Short ton is:" + str(value * 1.102293))
        print("in Long ton is:" + str(value * 0.984252))
        print("in Pounds is:" + str(value * 2204.586))
        print("in Ounces is:" + str(value * 35273.37))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "4":

        print("in Grams is:" + str(value * 907200))
        print("in Kilograms is:" + str(value * 907.2))
        print("in Metric tonnes is:" + str(value * 0.9072))
        print("in Short ton is:" + str(value))
        print("in Long ton is:" + str(value * 0.892913))
        print("in Pounds is:" + str(value * 2000))
        print("in Ounces is:" + str(value * 32000))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "5":

        print("in Grams is:" + str(value * 1016000))
        print("in Kilograms is:" + str(value * 1016))
        print("in Metric tonnes is:" + str(value * 1.016))
        print("in Short ton is:" + str(value * 1.119929))
        print("in Long ton is:" + str(value))
        print("in Pounds is:" + str(value * 2239.859))
        print("in Ounces is:" + str(value * 35837.74))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "6":
        print("in Grams is:" + str(value * 453.6))
        print("in Kilograms is:" + str(value * 0.4536))
        print("in Metric tonnes is:" + str(value * 0.000454))
        print("in Short ton is:" + str(value * 0.0005))
        print("in Long ton is:" + str(value * 0.000446))
        print("in Pounds is:" + str(value))
        print("in Ounces is:" + str(value * 16))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
    elif index == "7":
        print("in Grams is:" + str(value * 28))
        print("in Kilograms is:" + str(value * 0.02835))
        print("in Metric tonnes is:" + str(value * 0.000028))
        print("in Short ton is:" + str(value * 0.000031))
        print("in Long ton is:" + str(value * 0.000028))
        print("in Pounds is:" + str(value * 0.0625))
        print("in Ounces is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            mass()
def speed():
    print("Which unit do you have:")
    print("1. Meter/second\n"
          "2. Meter/minute\n"
          "3. Kilometer/hour\n"
          "4. Foot/second\n"
          "5. Foot/minute \n"
          "6. Miles/hour\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("in Meter/second is:" + str(value))
        print("in Meter/minute is:" + str(value * 59.988))
        print("in Kilometer/hour is:" + str(value * 3.599712))
        print("in Foot/second is:" + str(value * 3.28084))
        print("in Foot/minute  is:" + str(value * 196.8504))
        print("in Miles/hour is:" + str(value * 2.237136))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
    elif index == "2":

        print("in Meter/second is:" + str(value * 0.01667))
        print("in Meter/minute is:" + str(value))
        print("in Kilometer/hour is:" + str(value * 0.060007))
        print("in Foot/second is:" + str(value * 0.054692))
        print("in Foot/minute  is:" + str(value * 3.281496))
        print("in Miles/hour is:" + str(value * 0.037293))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
    elif index == "3":

        print("in Meter/second is:" + str(value * 0.2778))
        print("in Meter/minute is:" + str(value * 16.66467))
        print("in Kilometer/hour is:" + str(value))
        print("in Foot/second is:" + str(value * 0.911417))
        print("in Foot/minute  is:" + str(value * 54.68504))
        print("in Miles/hour is:" + str(value * 0.621477))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
    elif index == "4":

        print("in Meter/second is:" + str(value * 0.3048))
        print("in Meter/minute is:" + str(value * 18.28434))
        print("in Kilometer/hour is:" + str(value * 1.097192))
        print("in Foot/second is:" + str(value))
        print("in Foot/minute  is:" + str(value * 60))
        print("in Miles/hour is:" + str(value * 0.681879))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
    elif index == "5":

        print("in Meter/second is:" + str(value * 0.00508))
        print("in Meter/minute is:" + str(value * 0.304739))
        print("in Kilometer/hour is:" + str(value * 0.018287))
        print("in Foot/second is:" + str(value * 0.016667))
        print("in Foot/minute  is:" + str(value))
        print("in Miles/hour is:" + str(value * 0.016667))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
    elif index == "6":
        print("in Meter/second is:" + str(value * 0.447))
        print("in Meter/minute is:" + str(value * 26.81464))
        print("in Kilometer/hour is:" + str(value * 1.609071))
        print("in Foot/second is:" + str(value * 1.466535))
        print("in Foot/minute  is:" + str(value * 87.99213))
        print("in Miles/hour is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            speed()
def volume():
    Print("Sorry for the inconvinience under build check in version 2")
  """
    print("Which unit do you have:")
    print("1. Centimetre Cube\n"
          "2. Metre Cube\n"
          "3. Litre\n"
          "4. Inch cube\n"
          "5. Foot cube\n"
          "6. US gallons\n"
          "7. Imperial gallons\n"
          "8. US barrel (oil)\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("in MM is:" + str(value))
        print("in CM is:" + str(value * 0.000001))
        print("in M is:" + str(value * 0.001))
        print("in KM is:" + str(value * 0.061024))
        print("in INCH is:" + str(value * 0.000035))
        print("in FEET is:" + str(value * 0.000264))
        print("in YARD is:" + str(value * 0.00022))
        print("in MILE is:" + str(value * 0.000006))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "2":
        print("in MM is:" + str(value * 1000000))
        print("in CM is:" + str(value))
        print("in M is:" + str(value * 1000))
        print("in KM is:" + str(value * 61024))
        print("in INCH is:" + str(value * 35))
        print("in FEET is:" + str(value * 264))
        print("in YARD is:" + str(value * 220))
        print("in MILE is:" + str(value * 6.29))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "3":
        print("in MM is:" + str(value * 1000))
        print("in CM is:" + str(value * 0.001))
        print("in M is:" + str(value))
        print("in KM is:" + str(value * 61))
        print("in INCH is:" + str(value * 0.035))
        print("in FEET is:" + str(value * 0.264201))
        print("in YARD is:" + str(value * 0.22))
        print("in MILE is:" + str(value * 0.00629))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "4":
        print("in MM is:" + str(value * 16.4))
        print("in CM is:" + str(value * 0.000016))
        print("in M is:" + str(value * 0.016387))
        print("in KM is:" + str(value))
        print("in INCH is:" + str(value * 0.000579))
        print("in FEET is:" + str(value * 0.004329))
        print("in YARD is:" + str(value * 0.003605))
        print("in MILE is:" + str(value * 0.000103))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "5":
        print("in MM is:" + str(value * 28317))
        print("in CM is:" + str(value * 0.028317))
        print("in M is:" + str(value * 28.31685))
        print("in KM is:" + str(value * 1728))
        print("in INCH is:" + str(value))
        print("in FEET is:" + str(value * 7.481333))
        print("in YARD is:" + str(value * 6.229712))
        print("in MILE is:" + str(value * 0.178127))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "6":
        print("in MM is:" + str(value * 3785))
        print("in CM is:" + str(value * 0.003785))
        print("in M is:" + str(value * 3.79))
        print("in KM is:" + str(value * 231))
        print("in INCH is:" + str(value * 0.13))
        print("in FEET is:" + str(value))
        print("in YARD is:" + str(value * 0.832701))
        print("in MILE is:" + str(value * 0.02381))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "7":
        print("in MM is:" + str(value * 4545))
        print("in CM is:" + str(value * 0.004545))
        print("in M is:" + str(value * 4.55))
        print("in KM is:" + str(value * 277))
        print("in INCH is:" + str(value * 0.16))
        print("in FEET is:" + str(value * 1.20))
        print("in YARD is:" + str(value))
        print("in MILE is:" + str(value * 0.028593))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            volume()
    elif index == "8":
        print("in MM is:" + str(value * 158970))
        print("in CM is:" + str(value * 0.15897))
        print("in M is:" + str(value * 159))
        print("in KM is:" + str(value * 9701))
        print("in INCH is:" + str(value * 6))
        print("in FEET is:" + str(value * 42))
        print("in YARD is:" + str(value * 35))
        print("in MILE is:" + str(value))
        input("1. Go Back 2. Recalculate")
        if msg == "1":
            uc()
        else:
            """
            volume()         
def normal():
    print("Welcome To Normal Calculator")
    print("Here you can Add(+), Subtract(-), Multiply(*), Divide(/) and Modulus(%)")
    num1 = input("Enter the First Number:")
    operator = input("Enter the Operation :")
    num2 = input("Enter the Second Number:")
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2
    elif operator == "%":
        out = num1 % num2    
    else:
        out = "Please Enter A Valid string"
    print("Answer: " + str(out))
    print("Do you want to go back or re-calculate")
    msg = input("1. Go Back 2. Recalculate:")
    if msg == "1":
        menu()
    else:
        normal()
def rootsolve():
    print("Welcome To Root solver")
    print("What Type Of Equation Is Your Equation")
    print("1. Linear Equation(One Variable)")
    print("2. Linear Equation(Two Variable)")
    print("3. Pair Of Linear Equations(Two Variable)")
    print("4. Quadratic Equation")
    print("5. Cubic Equation*")
    print("6. Back")
    print("7. Exit")
    print("*-These Are Not Yet Fully Developed and may have bugs.")
    funct = input("What you want to do:")

    def linear_one():
        print("Enter The Values As Per the standard Form- ax+b=0")
        a = input("a:")
        b = input("b:")
        x = - (float(b)) / float(a)
        print("The Value of x is " + str(x))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            rootsolve()
        else:
            linear_one()

    def linear_two():
        print("Enter The Values As Per the standard Form- ax+by+c=0")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        xint = - float(c) / float(a)
        yint = -float(c) / float(b)
        slope = yint / (0 - xint)

        print("The X intercept is ("+str(xint)+",0)")
        print("The Y intercept is (0,"+str(yint)+")")
        print("Slope Is " + str(slope))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            rootsolve()
        else:
            linear_two()

    def pair_linear():
        print("Enter The Values As Per the standard Form- a1x+b1y+c1=0 and a2x+b2y+c2=0 ")
        a1 = input("a1:")
        b1 = input("b1:")
        c1 = input("c1:")
        a2 = input("a2:")
        b2 = input("b2:")
        c2 = input("c2:")
        if (float(a1)/float(a2)) != (float(b1)/float(b2)):
            mint = (((float(a1)) * (float(b2))) - ((float(a2)) * (float(b1))))
            xint = (((float(b1)) * (float(c2))) - ((float(b2)) * (float(c1)))) / mint
            yint = (((float(c1)) * (float(a2))) - ((float(c2)) * (float(a1)))) / mint
            print("The solution is" + str(xint) + "," + str(yint))
        elif float(a1)/float(a2) == float(b1)/float(b2) and float(a1)/float(a2) == (float(c1)/float(c2)):
            print("Infinite Solutions")
        else:
            print("No solutions")
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            rootsolve()
        else:
            pair_linear()

    def quadratic():
        import cmath
        print("Enter The Values As Per the standard Form-ax^2+bx+c=0")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        discriminant = (float(b) ** 2) - 4 * (float(a) * float(c))
        root1 = -((float(b)) - cmath.sqrt(discriminant)) / 2 * (float(a))
        root2 = -((float(b)) + cmath.sqrt(discriminant)) / 2 * (float(a))
        print('The roots are {0} and {1}'.format(root1, root2))
        print("The Discriminant is " + str(discriminant))
        print("The Y-Intercept is:" + str(c))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            rootsolve()
        else:
            quadratic()

    def cubic():
        print("Enter The Values As Per the standard Form-ax^3+bx^2+cx+d=0")
        print("Please Note: This can be used only to find one Root.")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        d = input("d:")
        p = (- float(b))/(3*(float(a)))
        q = ((p**3)+(((float(b))*(float(c)))-(3*((float(a))*(float(d)))))/(6*((float(a))**2)))
        r = ((float(c))/(3*float(a)))
        root = (q + (q**2 + (r-p**2)**3)**1/2)**1/3+(q - (q**2 + (r-p**2)**3)**1/2)**1/3+p
        print("One of the roots is "+str(root))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            rootsolve()
        else:
            cubic()

    if funct == "1":
        linear_one()
    elif funct == "2":
        linear_two()
    elif funct == "3":
        pair_linear()
    elif funct == "4":
        quadratic()
    elif funct == "5":
        cubic()
    elif funct == "6":
        menu()
    else:
        exit()

def scientific():
    print("Welcome To scientific Calculator")
    print("What do you want to solve")
    print("1. Trigonometric Functions")
    print("2. Logarithms")
    print("3. Squares And Cubes")
    print("4. Square And Cube Roots")
    print("5. Imaginary Numbers")
    print("6. Dot And Cross Products")
    print("7. Factor Calculator")
    print("8. Multiple Calculator")
    print("9. Factorial Finder")
    print("10. Back")
    print("11. Exit")

    def factorial():
                   import math
                   print("Welcome to Factorial Finder.")
                   x = input("Enter the number you want to find factorial of:")
                   print ("The factorial of x is : ", end="") 
                   print (math.factorial(x))
                   print("Do you want to go back or re-calculate")
                   msg = input("1. Go Back 2. Recalculate:")
                   if msg == "1":    
                                menu()
                   else:
                                factorial()  
    def trigno():
        print("This is Trignometry Calculator")
        print("1. Functions")
        print("2. Inverse Functions")
        print("3. Back")

        def trigfunctions():
            import math
            print("Write the angle in degrees")
            angle = int(input("Angle:"))
            degtorad = (22/7)/180
            print("Sin:" + str(math.sin(angle * degtorad)))
            print("Cos:" + str(math.cos(angle * degtorad)))
            print("Tan:" + str(math.tan(angle * degtorad)))
            print("These Values are approximated and may not be up to mark")
            print("Exact Values can be found using the plugins available. ")

        def invtrigfunctions():
            import math
            print("Write the Value")
            value = float(input("Value:"))
            print("Sin inv:" + str(math.degrees(math.asin(value))))
            print("Cos inv:" + str(math.degrees(math.acos(value))))
            print("Tan inv:" + str(math.degrees(math.atan(value))))
            print("These Values are approximated and may not be up to point")

        trigfunct = input("Index:")
        if trigfunct == "1":
            trigfunctions()
        elif trigfunct == "2":
            invtrigfunctions()
        else:
            scientific()

    def logs():
        import math
        print("Write in the following format number")
        number = float(input("Number:"))
        base = int(input("Base:"))
        print(f"Logarithm in base {base} is:" + str(math.log(number, base)))
        print("Natural Logharithm is:" + str(math.log(number)))
        print("Logarithm in Base 2 is:" + str(math.log2(number)))
        print("Logarithm in Base 10 is:" + str(math.log10(number)))
        print("Inverse Log in Base 10 is:" + str(number**2))

    def sqacubes():
        num1 = input("Enter The Number:")
        power = input("Enter the Power:")
        print(str(float(num1) ** float(power)))

    def sqacubesroots():
        num1 = input("Enter The Number:")
        power = input("Enter the Power of root:")
        print("+/-"+str(float(num1)**(1/float(power))))

    def imaginaryno():
        print("Choose One Of The Below")
        print("1. Basic Arithmetics")
        print("2. Advanced Arithmetic")
        print("3. Back")

        def basicimg():
            print("Write in the following type (a1+b1j) and (a2+b2j)")
            imgno1 = float(input("Number 1:"))
            imgno2 = float(input("Number 2:"))
            addimg = (imgno1 + imgno2)
            subimg = (imgno1 - imgno2)
            multimg = imgno1 * imgno2
            print("Addition:"+str(addimg))
            print("Subtraction:" + str(subimg))
            print("Multiplication:" + str(multimg))
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                imaginaryno()
            else:
                basicimg()

        def adving():
            import math
            import cmath
            print("Write in the following type (a+bj)")
            aimg = float(input("a:"))
            bimg = float(input("b:"))
            fortan = bimg/aimg
            print("Conjugate is:" + str(complex(aimg, -bimg)))
            print("Magnitude is:" + str(math.sqrt(aimg**2+bimg**2)))
            print("Argument is:" + str(math.degrees(math.atan(fortan))))
            print("Polar Coordinates:" + str(cmath.polar(complex(aimg, bimg))))
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                imaginaryno()
            else:
                adving()
        msginput = input("Your Choice:")
        if msginput == "1":
            basicimg()
        elif msginput == "2":
            adving()
        else:
            scientific()

    def dotandcross():
        print("Which dimension is your vector in?")
        print("1. Two Dimensional")
        print("2. Three Dimensional")
        print("3. Back")

        def twodime():
            print("Write in the form A[a1,b1] and B[a2,b2]")
            a1 = float(input("a1:"))
            b1 = float(input("b1:"))
            a2 = float(input("a2:"))
            b2 = float(input("b2:"))
            dotp = (a1*a2)+(b1*b2)
            print("The Dot Product Is:" + str(dotp))

        def threedime():
            print("Write in the form A[a1,b1,c1] and B[a2,b2,c2]")
            a1 = float(input("a1:"))
            b1 = float(input("b1:"))
            c1 = float(input("c1:"))
            a2 = float(input("a2:"))
            b2 = float(input("b2:"))
            c2 = float(input("c2:"))
            dotp = (a1 * a2) + (b1 * b2) + (c1*c2)
            crosspi = ((b1*c2)-(b2*c1))
            crosspj = -((a1*c2)-(a2*c1))
            crosspk = ((a1*b2)-(a2*b1))
            print("The Dot Product Is:" + str(dotp))
            print("The Cross Product Is:(" + str(crosspi)+"," + str(crosspj)+"," + str(crosspk)+")")
        dime = input("Dimension:")
        if dime == "1":
            twodime()
        elif dime == "2":
            threedime()
        else:
            scientific()

    def factorcalc():
        def print_factors(x):
            print("The factors of", x, "are:")
            for i in range(1, x + 1):
                if x % i == 0:
                    print(i)

        num = int(input("Enter your number:"))
        print_factors(num)
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            menu()
        else:
            factorcalc()

    def multiple():
        num = int(input("Enter the number:"))
        multipl = int(input("Enter the number of multiples:"))
        for i in range(1, multipl + 1):
            print(num, 'x', i, '=', num * i)
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            menu()
        else:
            multiple()

    funct = input("What you want to do:")
    if funct == "1":
        trigno()
    elif funct == "2":
        logs()
    elif funct == "3":
        sqacubes()
    elif funct == "4":
        sqacubesroots()
    elif funct == "5":
        imaginaryno()
    elif funct == "6":
        dotandcross()
    elif funct == "7":
        factorcalc()
    elif funct == "8":
        multiple()
    elif funct =="9":
        factorial()    
    elif funct == "10":
        menu()
    else:
        exit()
def geometry():
    print("Welcome To Geometry Calculator:")
    print("1. Two Dimensional Area")
    print("2. Three Dimensional Area")
    print("3. Parallelograms And Triangles")
    print("4. Heron's Formula")
    print("5. Triangle Checker")
    print("6. Back")
    geoindex = input("INDEX:")

    def twodimearea():
        print("Welcome To Area solve")
        print("1. Triangle")
        print("2. Quadrilaterals")
        print("3. n-gon")
        print("4. Circles And Elipses")
        print("5. Back")

        def triangle():
            height = float(input("Height:"))
            base = float(input("Base:"))
            print("Area is:" + str((1/2)*base*height))
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                twodimearea()
            else:
                triangle()

        def quadilaterals():
            print("Choose from the following quadilaterals")
            print("1. Trapezium")
            print("2. Parallelogram")
            print("3. Rectangle")
            print("4. Rhombus")
            print("5. Square")
            print("6. Kite")
            print("7. Back")

            def trapezium():
                para = float(input("Parallel side A:"))
                parb = float(input("Parallel side B:"))
                unpar = float(input("Un-parallel side:"))
                height = float(input("Height:"))
                print("Area is:" + str(0.5*(para+parb)*height))
                print("Perimeter is:" + str(para+parb+2*unpar))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    trapezium()

            def parallelogram():
                altitude = float(input("Altitude:"))
                base = float(input("Base:"))
                side = float(input("Side:"))
                print("Area is:" + str(altitude * base))
                print("Perimeter is:" + str(2 * (base + side)))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    parallelogram()

            def rectangle():
                length = float(input("Length:"))
                breadth = float(input("Breadth:"))
                print("Area is:" + str(length*breadth))
                print("Perimeter is:" + str(2*(length+breadth)))
                print("Diagonal is:" + str(((length**2)+(breadth**2))**0.5))
                print("Area of two triangles" + str(0.5*length*breadth))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    rectangle()

            def rhombus():
                diagnol1 = float(input("Longer Diagonal:"))
                diagnol2 = float(input("Shorter Diagonal:"))
                print("Area is:" + str(0.5 * diagnol1 * diagnol2))
                print("Side is:" + str((((diagnol1**2) + (diagnol2**2))**0.5)/2))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    rhombus()

            def square():
                side = float(input("Side:"))
                print("Perimeter is:" + str(4*side))
                print("Area is:" + str(side**2))
                print("Length Of Diagnol is:" + str((2**1/2)*side))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    square()

            def kite():
                diagnol1 = float(input("Longer Diagonal:"))
                diagnol2 = float(input("Shorter Diagonal:"))
                print("Area is:" + str(0.5*diagnol1*diagnol2))
                shodiagcut = float(input("Shorter Part of Longer Diagonal:"))
                side1 = (((diagnol2/2)**2)+shodiagcut**2)**0.5
                side2 = (((diagnol2/2)**2)+(diagnol1 - shodiagcut)**2)**0.5
                print("Sides are:" + str(side1) + "," + str(side2))
                print("Perimeter is:" + str((2*side1)+(2*side2)))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    quadilaterals()
                else:
                    kite()

            index = input("Option:")
            if index == "1":
                trapezium()
            elif index == "2":
                parallelogram()
            elif index == "3":
                rectangle()
            elif index == "4":
                rhombus()
            elif index == "5":
                square()
            elif index == "6":
                kite()
            else:
                twodimearea()

        def ngon():
            import math
            sides = float(input("Sides:"))
            sl = float(input("Side Length:"))
            print("Exterior Angle of Regular Polygon with "+str(sides)+" sides is:" + str(360/sides))
            print("Sum of interior angles of this polygon is:" + str((sides-2)*180))
            print("Number of diagnols in this polygon" + str(sides*(sides-3)/2))
            apothem = sl/(2*(math.tan(180/sides)))
            print("Apothem is:" + str(apothem))
            print("Area is:" + str((1/2)*(sides*sides)*apothem))
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                twodimearea()
            else:
                ngon()

        def circlesandellipses():
            print("1. Circles")
            print("2. Ellipses")
            print("3. Ring")
            print("4. Sector and Segment")
            index = input("Option:")

            def circles():
                import math
                radius = float(input("Radius:"))
                print("Perimeter is:" + str(2*math.pi*radius))
                print("Area is:" + str(math.pi * (radius**2)))
                print("Perimeter of The Semi Circle is:" + str((math.pi * radius)+2*radius))
                print("Area of a Semicircle of same radius:" + str((math.pi*(radius**2))/2))
                print("Perimeter of The Semi Circle is:" + str(((math.pi * radius)/2) + 2 * radius))
                print("Area of a Quadrant of same radius:" + str((math.pi * (radius ** 2)) / 4))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    circlesandellipses()
                else:
                    circles()

            def ellipses():
                print("Hello")
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    circlesandellipses()
                else:
                    ellipses()

            def ring():
                import math
                radiusa = float(input("Radius of Larger Circle"))
                radiusb = float(input("Radius of Shorter Circle"))
                print("Area of the ring:" + str(math.pi*(radiusa+radiusb)*(radiusa - radiusb)))
                print("Perimeter of the Rings combined are:" + str(2*math.pi*(radiusa+radiusb)))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    circlesandellipses()
                else:
                    ring()

            def secseg():
                import math
                radius = float(input("Radius:"))
                angle = float(input("Angle:"))
                print("Area of Sector:" + str((angle/360)*(math.pi * (radius**2))))
                print("Perimeter of Sector:" + str(((angle/360)*(2*math.pi*radius))+(2*radius)))
                areaseg = ((angle/360)*(math.pi * (radius**2)) - (0.5*(radius**2)*math.sin(angle)))
                periseg = ((math.pi*radius*angle)/180) + 2*radius*(math.sin(angle/2))
                print("Area of Segment:" + str(areaseg))
                print("Perimeter of Segment:" + str(periseg))
                print("Do you want to go back or re-calculate")
                msg = input("1. Go Back 2. Recalculate:")
                if msg == "1":
                    circlesandellipses()
                else:
                    secseg()
            if index == "1":
                circles()
            elif index == "2":
                ellipses()
            elif index == "3":
                ring()
            elif index == "4":
                secseg()
            else:
                circlesandellipses()

        areamenu = input("Shape:")
        if areamenu == "1":
            triangle()
        elif areamenu == "2":
            quadilaterals()
        elif areamenu == "3":
            ngon()
        elif areamenu == "4":
            circlesandellipses()
        else:
            geometry()

    def trinaglecheck():
        print("This Tool Can Be Used To Check if a traingle can be formed or not")
        a = float(input("Side A:"))
        b = float(input("Side B:"))
        c = float(input("Side C:"))
        if a+b > c and a+c > b and b+c > a:
            print("This triangle is possible")
        else:
            print("This triangle cannot be formed")
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            geometry()
        else:
            trinaglecheck()

    def parrandtri():
        print("This tool can be used to find the area of triangles and parallelograms")
        base = float(input("Base:"))
        hght = float(input("Height:"))
        print("The area of triangle formed is:" + str((base*hght)/2))
        print("The area of triangle formed is:" + str(base * hght))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            geometry()
        else:
            parrandtri()

    def heronform():
        import math
        print("This tool can be used to calculate area of triangle by Heron's Formula")
        a = float(input("Side A"))
        b = float(input("Side B"))
        c = float(input("Side C"))
        semip = (a+b+c)/2
        area = math.sqrt(semip*(semip-a)*(semip-b)*(semip-c))
        print("Semi-Perimeter is:" + str(semip))
        print("Area is:" + str(area))
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            geometry()
        else:
            heronform()

    def threedimearea():
        print("Welcome To Area solve")
        print("1. Cuboid")
        print("2. Cube")
        print("3. Cylinder")
        print("4. Cone")
        print("5. Sphere")
        print("6. Back")

        def cuboid():
            length = float(input("Length:"))
            breadth = float(input("Breadth:"))
            height = float(input("Height:"))
            print("Surface Area is" + str(2*((length*breadth)+(breadth*height)+(height*length))) + "m^3")
            print("Volume is" + str(length*breadth*height))
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                threedimearea()
            else:
                cuboid()

        def cube():
            side = float(input("Side:"))
            print("Surface Area is:" + str(6*(side**2)))
            print("Volume is;" + str(side**3))
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                threedimearea()
            else:
                cube()

        def cylinder():
            radius = float(input("Radius:"))
            height = float(input("Height:"))
            print("Total Surface Area is " + str(2*(22/7)*(radius+height)))
            print("Curved surface Area is " + str(2*(22/7)*radius*height))
            print("Volume is" + str((22/7)*(radius**2)*height))
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                threedimearea()
            else:
                cylinder()

        def cone():
            import math
            radius = float(input("Radius:"))
            height = float(input("Height:"))
            slant = math.sqrt((radius**2)+(height**2))
            print("Total Surface Area is " + str((22 / 7) * (radius + slant)))
            print("Curved surface Area is " + str(2 * (22 / 7) * radius * height))
            print("Volume is" + str((1/3)*(22 / 7) * (radius ** 2) * height))
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                threedimearea()
            else:
                cone()

        def sphere():
            radius = float(input("Radius:"))
            print("Surface Area of Sphere:" + str(4*(22/7)*(radius**2)))
            print("Curved Surface Area of Hemisphere:" + str(2*(22/7)*(radius**2)))
            print("Total Surface Area of Hemisphere:" + str(3*(22/7)*(radius**2)))
            print("Volume of Sphere:" + str((4/3)*(22/7)*(radius**3)))
            print("Volume of Hemisphere:" + str((2/3)*(22/7)*(radius**2)))
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                threedimearea()
            else:
                sphere()

        areamenu = input("Shape:")
        if areamenu == "1":
            cuboid()
        elif areamenu == "2":
            cube()
        elif areamenu == "3":
            cylinder()
        elif areamenu == "4":
            cone()
        elif areamenu == "5":
            sphere()
        else:
            geometry()

    if geoindex == "1":
        twodimearea()
    elif geoindex == "2":
        threedimearea()
    elif geoindex == "3":
        parrandtri()
    elif geoindex == "4":
        heronform()
    elif geoindex == "5":
        trinaglecheck()
    else:
        menu()
def graphingcalc():
    def pointplot():
        import numpy as np
        import matplotlib.pyplot as plt
        index = float(input("Point X:"))
        indey = float(input("Point Y:"))
        x = np.array([index])
        y = np.array([indey])
        plt.scatter(x, y)
        plt.show()
        print("Do you want to go back or re-calculate")
        msg = input("1. Go Back 2. Recalculate:")
        if msg == "1":
            graphingcalc()
        else:
            pointplot()

    def trignometricfunct():
        def sin():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.sin(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                sin()

        def cos():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.cos(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                cos()

        def tan():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.tan(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                tan()

        def sininv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arcsin(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                sininv()

        def cosinv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arccos(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                cosinv()

        def taninv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arctan(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                trignometricfunct()
            else:
                taninv()

        print("Which function do you want to solve?")
        print("1. sin\n"
              "2. cos\n"
              "3. tan\n"
              "4. sin inv\n"
              "5. cos inv\n"
              "6. tan inv\n"
              "7. Back\n"
              )
        ind = input("Function:")
        if ind == '1':
            sin()
        elif ind == '2':
            cos()
        elif ind == '3':
            tan()
        elif ind == '4':
            sininv()
        elif ind == '5':
            cosinv()
        elif ind == '6':
            taninv()
        else:
            menu()

    def addsubtrig():
        print("Choose from the following options:")
        print("1. msin(x)+ncos(x)\n"
              "2. mcos(x)+ntan(x)\n"
              "3. mtan(x)+nsin(x)\n"
              "4. msin(x)+ncos(x)+ptan(x)\n"
              )
        ind = input("Choose:")

        def sincos():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.sin(x)) + n * (np.cos(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                addsubtrig()
            else:
                sincos()

        def costan():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.cos(x)) + n * (np.tan(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                addsubtrig()
            else:
                costan()

        def tansin():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.tan(x)) + n * (np.sin(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                addsubtrig()
            else:
                tansin()

        def sincostan():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            p = float(input("Enter the constant p:"))
            x = np.linspace(0, 10, 30)
            y = ((m * (np.sin(x))) + (n * (np.cos(x))) + (p * (np.tan(x))))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msg = input("1. Go Back 2. Recalculate:")
            if msg == "1":
                addsubtrig()
            else:
                sincostan()

        if ind == "1":
            sincos()
        elif ind == "2":
            costan()
        elif ind == "3":
            tansin()
        elif ind == "4":
            sincostan()
        else:
            menu()

    print("1. Points Plotter")
    print("2. Trigonometric Function Grapher")
    print("3. Addition And Subtraction of Trigonometric Functions")
    print("4. Back")
    menuin = input("Menu:")
    if menuin == "1":
        pointplot()
    elif menuin == "2":
        trignometricfunct()
    elif menuin == "3":
        addsubtrig()
    else:
        graphingcalc()


print("A Super calculator by P S Mithul Sourav")
print("Visit github.com/psmithulsourav For More Apps")
menu()
