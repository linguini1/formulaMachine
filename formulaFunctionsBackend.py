# Physics Formula Machine: Basic function is to solve physics problems using user input

# Imports
import math
import addingForces

# Variables
var_prompt = "Please type your variables into the terminal. Put '?' for the variable you want to solve for."

# Classes


class Vector:
    def __init__(self, direction, magnitude, degree):
        self.direction = direction
        self.magnitude = magnitude
        self.degree = degree


# Valid input checker
def validInput(prompt, dataRange=None, unknowns=False):
    while True:
        usr_input = input(prompt)

        if unknowns:
            err_msg = "A number or '?' is required for this input."
        else:
            err_msg = "A number is required for this input."

        try:
            usr_input = eval(usr_input)
            error = False
        except SyntaxError:
            if unknowns:
                if usr_input == '?':
                    break
                else:
                    error = True
                    print(err_msg)
            else:
                print(err_msg)
                error = True

        if not error:
            if dataRange is not None:
                if usr_input in dataRange:
                    break
                else:
                    print("Invalid input.")
            elif dataRange is None:
                break

    return usr_input


# Determining Unit
def detU():
    print("""1) Kinematics\n2) Forces\n3) Energy and Society\n4) Waves and Sound\n5) Electricity and Magnetism\n""")
    unit = validInput("Unit number: ", [1, 2, 3, 4, 5])

    if unit == 1:
        print("""\n1) Finding V\n2) Finding d\n3) Finding t\n4) Finding a\n""")

        problem = validInput("Type your problem's number here: ", [1, 2, 3, 4])
        detFormulaU1(problem)

    elif unit == 2:
        print("\n1) Finding net force\n2) Finding force of gravity\n3) Finding gravitational field strength")
        print("4) Finding force of friction\n5) Adding non-collinear forces\n6) Returning vector components\n")

        problem = validInput("Type your problem's number here: ", [1, 2, 3, 4, 5, 6])
        detFormulaU2(problem)

    elif unit == 3:
        print("\n1) Finding work\n2) Finding kinetic energy\n3) Finding gravitational potential energy")
        print("4) Finding power\n5) Finding efficiency\n6) Finding thermal energy\n")

        problem = validInput("Type your problem's number here: ", [1, 2, 3, 4, 5, 6])
        detFormulaU3(problem)

    elif unit == 4:
        print("\n1) Adding Decibels\n2) Doppler Effect\n3) Beat Frequency\n4) Velocity of sound in air\n")

        problem = validInput("Type your problem's number here: ", [1, 2, 3, 4])
        detFormulaU4(problem)

    elif unit == 5:
        print("\n1) V = IR equation\n2) Finding P (or using P to find other variables)")
        print("3) Finding E (or using E to find other variables)\n4) I = Q/t equation\n5) BIL equation")
        print("6) Adding resistance in parallel circuits\n")

        problem = validInput("Type your problem's number here: ", [1, 2, 3, 4, 5, 6])
        detFormulaU5(problem)


# Determining Formula
def detFormulaU5(problem):

    if problem == 1:
        print(var_prompt)

        v = validInput("V: ", unknowns=True)
        i = validInput("I: ", unknowns=True)
        r = validInput("R: ", unknowns=True)
        print(virEquation(v, i, r))

    elif problem == 2:
        print("Do you want to solve for P, V, I or R (type the corresponding letter in caps)?")
        while True:
            solve_for = input("Which variable?: ")
            if solve_for not in "PVIR":
                print("Invalid input.")
            else:
                break

        print(var_prompt)
        if solve_for == 'P':
            v = validInput("V: ", unknowns=True)
            i = validInput("I: ", unknowns=True)
            r = validInput("R: ", unknowns=True)
            p = '?'
        elif solve_for == 'V':
            p = validInput("P: ", unknowns=True)
            i = validInput("I: ", unknowns=True)
            r = validInput("R: ", unknowns=True)
            v = '?'
        elif solve_for == 'I':
            v = validInput("V: ", unknowns=True)
            p = validInput("P: ", unknowns=True)
            r = validInput("R: ", unknowns=True)
            i = '?'
        else:
            v = validInput("V: ", unknowns=True)
            i = validInput("I: ", unknowns=True)
            p = validInput("P: ", unknowns=True)
            r = '?'
        
        print(findP(solve_for, v, i, r, p))

    elif problem == 3:
        print(var_prompt)

        e = validInput("E: ", unknowns=True)
        q = validInput("q: ", unknowns=True)
        delta_v = validInput("E: ", unknowns=True)
        print(findE(e, q, delta_v))

    elif problem == 4:
        print(var_prompt)

        i = validInput("I: ", unknowns=True)
        q = validInput("Q: ", unknowns=True)
        t = validInput("t: ", unknowns=True)
        print(iqtEquation(i, q, t))

    elif problem == 5:
        print(var_prompt)

        fm = validInput("Fm: ", unknowns=True)
        b = validInput("B: ", unknowns=True)
        i = validInput("I: ", unknowns=True)
        length = validInput("L: ", unknowns=True)
        print(BIL(fm, b, i, length))

    elif problem == 6:
        print("Please type in the resistor values, separated by a comma, in ohms (123, 456, 789).")
        while True:
            resistors = input("Resistors: ")
            if ',' not in resistors:
                print("Resistors must be inputted in format '1, 2, 3, 4, 5'")
                error = True
            else:
                resistors = resistors.split(',')
                error = False
            if not error:
                try:
                    for resistor in resistors:
                        float(resistor)
                    break
                except ValueError:
                    print("Invalid input.")

        print(addingParallel(resistors))


def detFormulaU4(problem):

    if problem == 1:
        print("Okay, I can add two decibel values for you! Please write your number to one decimal place only.")

        decibel1 = validInput("First decibel value here: ")
        decibel2 = validInput("Second decibel value here: ")
        print(addingDecibels(decibel1, decibel2))

    elif problem == 2:
        print(var_prompt)

        f1 = validInput("F1: ", unknowns=True)
        f2 = validInput("F2: ", unknowns=True)
        vs = validInput("VS (speed of sound): ", unknowns=True)
        vo = validInput("VO (speed of object): ", unknowns=True)
        print(dopplerEffect(f1, f2, vs, vo))

    elif problem == 3:
        print("Please input your variables in Hz. Put '?' for the variable you want to solve for.")

        fb = validInput("Fb (beat frequency): ", unknowns=True)
        f1 = validInput("F1: ", unknowns=True)
        f2 = validInput("F2: ", unknowns=True)
        print(beatFrequency(fb, f1, f2))

    elif problem == 4:
        print(var_prompt)

        t = validInput("T: ", unknowns=True)
        vs = validInput("VS: ", unknowns=True)
        print(soundInAir(t, vs))


def detFormulaU3(problem):

    if problem == 1:
        print(var_prompt)

        work = validInput("W: ", unknowns=True)
        force = validInput("F: ", unknowns=True)
        distance = validInput("d: ", unknowns=True)
        print(findWork(work, force, distance))

    elif problem == 2:
        print(var_prompt)

        ek = validInput("Ek: ", unknowns=True)
        m = validInput("m: ", unknowns=True)
        v = validInput("v: ", unknowns=True)
        print(findEk(ek, m, v))

    elif problem == 3:
        print(var_prompt)

        eg = validInput("Eg: ", unknowns=True)
        m = validInput("m: ", unknowns=True)
        h = validInput("h: ", unknowns=True)
        print(findEg(eg, m, h))

    elif problem == 4:
        print("Do you have work or two energies as a variable? If you only have the change in energy and not the two "
              "energies, select the work option. Type 'WORK' or 'DELTA E': ")
        while True:
            work_or_energy = input("WORK or DELTA E: ")
            if work_or_energy != "WORK" or work_or_energy != "DELTA E":
                print("Invalid input.")
            else:
                break

        print(var_prompt)
        p = validInput("P: ", unknowns=True)
        t = validInput("t: ", unknowns=True)

        if work_or_energy == 'WORK':
            w = validInput("W: ", unknowns=True)
            print(findPower(p, w, t, 0, 0))

        elif work_or_energy == 'DELTA E':
            e1 = validInput("First energy: ", unknowns=True)
            e2 = validInput("Second energy: ", unknowns=True)
            print(findPower(p, 0, t, e1, e2, work_or_energy='DELTA E'))

    elif problem == 5:
        print(var_prompt)

        e_in = validInput("Energy in: ", unknowns=True)
        e_out = validInput("Energy out: ", unknowns=True)
        eff = validInput("Efficiency: ", unknowns=True)
        print(calcEff(e_in, e_out, eff))

    elif problem == 6:
        print("Do you have two temperature values or just delta T? Put '2' for two values and '1' for delta T:")
        use_delta_t = validInput("1 or 2: ", dataRange=[1, 2])
        print(var_prompt)

        q = validInput("Q: ", unknowns=True)
        m = validInput("m: ", unknowns=True)
        c = validInput("c: ", unknowns=True)

        if use_delta_t == 1:
            delta_t = validInput("Delta T: ", unknowns=True)

            print(calculateThermalEnergy(q, m, c, 0, 0, delta_t, use_delta_t))

        elif use_delta_t == 2:
            t1 = validInput("First temperature: ", unknowns=True)
            t2 = validInput("Second temperature: ", unknowns=True)

            print(calculateThermalEnergy(q, m, c, t1, t2, 0, use_delta_t))


def detFormulaU2(problem):

    if problem == 1:
        print(var_prompt)

        fnet = validInput("F net: ", unknowns=True)
        m = validInput("Mass: ", unknowns=True)
        a = validInput("Acceleration: ", unknowns=True)
        print(netForce(fnet, m, a))

    elif problem == 2:
        print(var_prompt)

        fg = validInput("Force of gravity: ", unknowns=True)
        m = validInput("Mass: ", unknowns=True)
        print(forceGravity(fg, m))

    elif problem == 3:
        print(var_prompt)

        fg = validInput("Gravitational field strength (use form Y * 10 ** Z for scientific notation): ", unknowns=True)
        m1 = validInput("First mass: ", unknowns=True)
        m2 = validInput("Second mass: ", unknowns=True)
        d = validInput("Distance: ", unknowns=True)
        print(gravitFieldStrength(fg, m1, m2, d,))

    elif problem == 4:
        print(var_prompt)

        ff = validInput("Force of friction: ", unknowns=True)
        fn = validInput("Force normal: ", unknowns=True)
        coeff_friction = input("Coefficient of friction: ")
        print(forceFriction(ff, fn, coeff_friction))

    elif problem == 5:
        print(var_prompt + " Direction should be written in format 'XY' using capital letters.")

        force_sum = Vector(input("Direction of force sum: "),
                           validInput("Magnitude of force sum: ", unknowns=True),
                           validInput("Angle of force sum: ", unknowns=True))

        force1 = Vector(input("Direction of force one: "),
                        validInput("Magnitude of force one: ", unknowns=True),
                        validInput("Angle of force one: ", unknowns=True))

        force2 = Vector(input("Direction of force two: "),
                        validInput("Magnitude of force two: ", unknowns=True),
                        validInput("Angle of force two: ", unknowns=True))

        print(addingForces.adding_forces(force_sum, force1, force2))

    elif problem == 6:
        print("Please input your variables into the terminal. "
              "You will be returned the X and Y vector components of your input vector. "
              "Direction should be written in format XY using capital letters.")

        vector_in = Vector(input("Direction of vector: "),
                           validInput("Magnitude of vector: "),
                           validInput("Angle of vector: "))

        print(vectorComp(vector_in))


def detFormulaU1(problem):

    if problem == 1:
        print("Do you need to solve for V1, V2 or Vav?")
        while True:
            which_v = input("Which one: ")
            if which_v in "V1V2Vav":
                break
            else:
                print("Invalid input.")

        print(var_prompt)
        d = validInput("d: ", unknowns=True)
        a = validInput("a: ", unknowns=True)
        t = validInput("t: ", unknowns=True)
    
        if which_v == "V1":
            vav = validInput("Vav: ", unknowns=True)
            v2 = validInput("V2: ", unknowns=True)
            v1 = '?'
        elif which_v == "V2":
            vav = validInput("Vav: ", unknowns=True)
            v1 = validInput("V1: ", unknowns=True)
            v2 = '?'
        else:
            v1 = validInput("V1: ", unknowns=True)
            v2 = validInput("V2: ", unknowns=True)
            vav = '?'

        print(findV(which_v, d, vav, v2, v1, a, t))

    elif problem == 2:
        print(var_prompt)
        vav = validInput("Vav: ", unknowns=True)
        v2 = validInput("V2: ", unknowns=True)
        v1 = validInput("V1: ", unknowns=True)
        a = validInput("a: ", unknowns=True)
        t = validInput("t: ", unknowns=True)

        print(findD(vav, v2, v1, a, t))

    elif problem == 3:
        print(var_prompt)
        vav = validInput("Vav: ", unknowns=True)
        v2 = validInput("V2: ", unknowns=True)
        v1 = validInput("V1: ", unknowns=True)
        a = validInput("a: ", unknowns=True)
        d = validInput("d: ", unknowns=True)

        print(findT(vav, v2, v1, a, d))

    elif problem == 4:
        print(var_prompt)
        v2 = validInput("V2: ", unknowns=True)
        v1 = validInput("V1: ", unknowns=True)
        t = validInput("t: ", unknowns=True)
        d = validInput("d: ", unknowns=True)

        print(findA(v2, v1, t, d))

# Unit 1 Formula Functions


def findV(which_v, d, vav, v2, v1, a, t):
    if which_v == 'V1':
        if d == '?' and vav == '?':
            v1 = (-a * t) + v2
            return v1
        elif vav == '?' and t == '?':
            v1 = math.sqrt(v2 ** 2 - 2 * a * d)
            return v1
        elif vav == '?' and a == '?':
            v1 = 2 * (d / t) - v2
            return v1
        elif vav == '?' and v2 == '?':
            v1 = (d - 0.5 * a * t ** 2) / t
            return v1
        elif v2 != '?' and vav != '?':
            v1 = 2 * vav - v2
            return v1
        else:
            return "Invalid input."

    elif which_v == 'V2':
        if vav == '?' and t == '?':
            v2 = math.sqrt(v1 ** 2 + 2 * a * d)
            return v2
        elif vav == '?' and a == '?':
            v2 = 2 * (d / t) - v1
            return v2
        elif vav == '?' and d == '?':
            v2 = a * t + v1
            return v2
        elif d == '?' and a == '?' and t == '?':
            v2 = 2 * vav - v1
            return v2
        elif vav == '?' and v1 == '?':
            v2 = (d + 0.5 * a * t ** 2) / t
            return v2
        else:
            return "Invalid input."
    
    elif which_v == 'Vav':
        if v1 != '?':
            vav = (v1 + v2) / 2
            return vav
        elif d != '?':
            vav = d / t
            return vav
        else:
            return "Invalid input."
    else:
        print("Invalid input.")


def findD(vav, v2, v1, a, t):
    if a == '?' and v2 == '?' and v1 == '?':
        d = vav * t
        return d
    elif vav == '?' and a == '?':
        d = (v1 + v2 / 2) * t
        return d
    elif vav == '?' and v2 == '?':
        d = v1 * t + 0.5 * a * t ** 2
        return d
    elif vav == '?' and t == '?':
        d = (v2 ** 2 - v1 ** 2) / 2 * a
        return d
    else:
        return "Invalid input."


def findT(vav, v2, v1, a, d):
    if vav == '?' and d == '?':
        t = (v2 - v1) / a
        return t
    elif vav == '?' and a == '?':
        t = d / (v1 + v2 / 2)
        return t
    elif vav != '?' and d != '?':
        t = d / vav
        return t
    else:
        return "Invalid input."


def findA(v2, v1, t, d):
    if d == '?':
        a = (v2 - v1) / t
        return a
    elif t == '?':
        a = (v2 ** 2 - v1 ** 2) / 2 * d
        return a
    elif v2 == '?':
        a = (d - v1 * t) / 0.5 * t ** 2
        return a
    elif v1 == '?':
        a = (d - v2 * t) / -0.5 * t ** 2
        return a
    else:
        return "Invalid input."

# Unit 2 Formula Functions


def netForce(fnet, m, a):
    if fnet == '?':
        return f"F net is equal to: {m * a}N."
    elif m == '?':
        return f"Mass is equal to: {fnet / a} kilograms."
    elif a == '?':
        return f"Acceleration is equal to: {fnet / m} meters/second squared."
    else:
        return "Invalid input."


def forceGravity(fg, m):
    if fg == '?':
        return f"Force of gravity is equal to: {m * 9.8}N."
    elif m == '?':
        return f"Mass is equal to: {fg / 9.8} kilograms."
    else:
        return "Invalid input."


def gravitFieldStrength(fg, m1, m2, d):
    g = 6.67 * (10 ** -11)
    if fg == '?':
        return f"Gravitational field strength is equal to: {(g * m1 * m2) / d ** 2}N/kg."
    elif m1 == '?':
        return f"First mass is equal to: {(fg * d ** 2) / (g * m2)} kilograms."
    elif m2 == '?':
        return f"Second mass is equal to: {(fg * d ** 2) / (g * m1)} kilograms."
    elif d == '?':
        return f"Distance is equal to: {math.sqrt((g * m1 * m2) / fg)} meters."
    else:
        return "Invalid input."


def forceFriction(ff, fn, coeff_friction):
    if ff == '?':
        return f"Force of friction is equal to: {fn * coeff_friction}N."
    if fn == '?':
        return f"Force normal is equal to: {ff / coeff_friction}N."
    elif coeff_friction == '?':
        return f"Coefficient of friction is equal to: {ff / fn}"
    else:
        return 'Invalid input.'


def vectorComp(vector_in):
    # Vector reversal if first direction is an X value
    if vector_in.direction[0] == 'W' or vector_in.direction[0] == 'E':
        if int(vector_in.degree) < 90:
            sum_y = vector_in.direction[0]
            sum_x = vector_in.direction[1]
            vector_in.direction = sum_x + sum_y
            vector_in.degree = 90 - int(vector_in.degree)
        elif 90 < int(vector_in.degree) < 180:
            sum_y = vector_in.direction[0]
            sum_x = vector_in.direction[1]
            if sum_y == 'W':
                sum_y = 'E'
            elif sum_y == 'E':
                sum_y = 'W'
            vector_in.direction = sum_x + sum_y
            vector_in.degree = int(vector_in.degree) - 90
    # Splitting into x and y
    sum_x = vector_in.magnitude * math.sin(math.radians(vector_in.degree))
    sum_y = vector_in.magnitude * math.cos(math.radians(vector_in.degree))
    x_vector = Vector(vector_in.direction[1], sum_x, 0)
    y_vector = Vector(vector_in.direction[0], sum_y, 0)
    return f"X vector is: {x_vector.magnitude}[{x_vector.direction}] | Y vector is: {y_vector.magnitude}[{y_vector.direction}]"

# Unit 3 Formula Functions


def findWork(work, force, distance):
    if work == '?':
        return f"Work is equal to: {force * distance}J."
    elif force == '?':
        return f"Force is equal to: {work / distance}N."
    elif distance == '?':
        return f"Distance is equal to: {work / force} meters."
    else:
        return "Invalid input."


def findEk(ek, m, v):
    if ek == '?':
        return f"Ek is equal to: {0.5 * m * v ** 2}J."
    elif m == '?':
        return f"m is equal to: {(2 * ek) / v ** 2} kilograms."
    elif v == '?':
        return f"v is equal to: {math.sqrt((2 * ek) / m)} meters/second."
    else:
        return "Invalid input."


def findEg(eg, m, h):
    if eg == '?':
        return f"Eg is equal to: {m * 9.8 * h}J."
    elif m == '?':
        return f"m is equal to: {eg / (9.8 * h)} kilograms."
    elif h == '?':
        return f"h is equal to: {eg / (9.8 * m)} meters."
    else:
        return "Invalid input."


def calcEff(e_in, e_out, eff,):
    if eff == '?':
        return f"Efficiency is: {(e_in / e_out) * 100}%"
    elif e_in == '?':
        return f"Energy input is equal to: {e_out / (eff / 100)}J."
    elif e_out == '?':
        return f"Energy output is equal to: {(eff / 100) * e_in}J."
    else:
        return "Invalid input."


def findPower(p, w, t, e1, e2, work_or_energy='WORK'):
    if work_or_energy == 'WORK':
        if p == '?':
            return f"Power is equal to: {w / t} watts."
        elif w == '?':
            return f"Work is equal to: {p * t}J."
        elif t == '?':
            return f"Time is equal to: {w / p} seconds."
        else:
            return "Invalid input."
    elif work_or_energy == 'DELTA E':
        if p == '?':
            return f"Power is equal to: {(e2 - e1) / t} watts."
        elif t == '?':
            return f"Time is equal to: {(e2 - e1) / p} seconds."
        elif e1 == '?':
            return f"First energy is equal to: {-(p * t - e2)}J."
        elif e2 == '?':
            return f"Second energy is equal to: {p * t + e1}J."
        else:
            return "Invalid input."
    else:
        return 'Invalid input.'


def calculateThermalEnergy(q, m, c, t1, t2, delta_t, use_delta_t):
    if use_delta_t == 1:
        if q == '?':
            return f"Q is equal to: {m * c * delta_t}J."
        elif m == '?':
            return f"m is equal to: {q / (c * delta_t)} kilograms."
        elif c == '?':
            return f"C is equal to: {q / (m * delta_t)}J/kg degree celsius."
        elif delta_t == '?':
            return f"Change in temperature is equal to: {q / (m * c)} degrees celsius."
    elif use_delta_t == 2:
        if q == '?':
            return f"Q is equal to: {m * c * (t2 - t1)}J."
        elif m == '?':
            return f"m is equal to: {q / (c * (t2 - t1))} kilograms."
        elif c == '?':
            return f"C is equal to: {q / (m * (t2 - t1))}J/kg degree celsius"
        elif t1 == '?':
            return f"First temperature is equal to: {-(q / (m * c) - t2)} degrees celsius."
        elif t2 == '?':
            return f"Second temperature is equal to: {q / (m * c) + t1} degrees celsius."

# Unit 4 Formula Functions


def addingDecibels(decibel1, decibel2):
    decibel1 = str(decibel1)
    decibel2 = str(decibel2)
    if len(decibel1) == 3:
        decibel1 = eval(decibel1)
        decibel1 = decibel1 / 10
    elif len(decibel1) == 4:
        decibel1 = eval(decibel1)
        decibel1 = decibel1 / 10
    elif len(decibel1) == 5:
        decibel1 = eval(decibel1)
        decibel1 = decibel1 / 100
    elif len(decibel1) == 6:
        decibel1 = eval(decibel1)
        decibel1 = decibel1 / 1000
    else:
        return "Your first decibel value is too large."
    if len(decibel2) == 3:
        decibel2 = eval(decibel2)
        decibel2 = decibel2 / 10
    elif len(decibel2) == 4:
        decibel2 = eval(decibel2)
        decibel2 = decibel2 / 10
    elif len(decibel2) == 5:
        decibel2 = eval(decibel2)
        decibel2 = decibel2 / 100
    elif len(decibel2) == 6:
        decibel2 = eval(decibel2)
        decibel2 = decibel2 / 1000
    else:
        return "Your second decibel value is too large."
    decibel_answer = math.log10(10 ** decibel1 + 10 ** decibel2) * 10
    return f"The answer is: {decibel_answer} decibels."


def dopplerEffect(f1, f2, vs, vo):
    direction_of_object = input("Is the object moving towards you? Write 'YES' or 'NO': ")
    if direction_of_object == 'YES':
        if f1 == '?':
            return f"Real frequency is equal to: {f2 / (vs / (vs - vo))}Hz."
        elif f2 == '?':
            return f"Observed frequency is equal to: {f1 * (vs / (vs - vo))}Hz."
        elif vs == '?':
            return f"Speed of sound is equal to: {(f2 * vo) / (f2-f1)} meters/second."
        elif vo == '?':
            return f"Speed of the object is equal to: {(vs * (f2 - f1)) / f2} meters/second."
    elif direction_of_object == 'NO':
        if f1 == '?':
            return f"Real frequency is equal to: {f2 / (vs / (vs + vo))}Hz."
        elif f2 == '?':
            return f"Observed frequency is equal to: {f1 * (vs / (vs + vo))}Hz."
        elif vs == '?':
            return f"Speed of sound is equal to: {(-f2 * vo) / (f2-f1)} meters/second."
        elif vo == '?':
            return f"Speed of object is equal to: {(vs * (f2 - f1)) / -f2} meters/second."
    else:
        return "Invalid input."


def beatFrequency(fb, f1, f2):
    if f1 == '?':
        return f"First frequency is: {f2 - fb}Hz, {f2 + fb}Hz."
    elif f2 == '?':
        return f"Second frequency is: {f1 + fb}Hz, {f1 - fb}Hz."
    elif fb == '?':
        return f"Beat frequency is: {abs(f2 - f1)}Hz."
    else:
        return "Invalid input."


def soundInAir(t, vs):
    if t == '?':
        return f"Air temperature is: {(vs - 332) / 0.59} degrees celsius."
    elif vs == '?':
        return f"Velocity of sound is: {332 + 0.59 * t} meters/second."
    else:
        return "Invalid input."

# Unit 5 Formula functions


def virEquation(v, i, r):
    if v == '?':
        v = i * r
        return f"{v}v"
    elif i == '?':
        i = v / r
        return f"{i}A"
    elif r == '?':
        r = v / i
        return f"{r} ohms"
    else:
        return "Invalid input."


def findP(solve_for, v, i, r, p):
    if solve_for == 'P':
        if r == '?':
            p = v * i
            return f"{p}W"
        elif v == '?':
            p = (i ** 2) * r
            return f"{p}W"
        elif i == '?':
            p = (v ** 2) * r
            return f"{p}W"
        else:
            return "Invalid input."
    elif solve_for == 'V':
        if i == '?':
            v = math.sqrt(p / r)
            return f"{v}v"
        elif r == '?':
            v = p / i
            return f"{v}v"
        else:
            return "Invalid input."
    elif solve_for == 'I':
        if v == '?':
            i = math.sqrt(p / r)
            return f"{i}A"
        elif r == '?':
            i = p / v
            return f"{i}A"
        else:
            return "Invalid input."
    elif r == '?':
        if i == '?':
            r = p / v ** 2
            return f"{r} ohms"
        elif v == '?':
            r = p / i ** 2
            return f"{r} ohms"
        else:
            return "Invalid input."
    else:
        return "Invalid input."


def findE(e, q, delta_v):
    if e == '?':
        e = q * delta_v
        return f"{e}J"
    elif q == '?':
        q = e / delta_v
        return f"{q} coulombs"
    elif delta_v == '?':
        delta_v = e / q
        return f"{delta_v}v"
    else:
        return "Invalid input."


def iqtEquation(i, q, t):
    if i == '?':
        i = q / t
        return f"{i}A"
    elif q == '?':
        q = i * t
        return f"{q} coulombs"
    elif t == '?':
        t = i * q
        return f"{t} seconds"
    else:
        return "Invalid input."


def BIL(fm, b, i, length):
    if fm == '?':
        fm = b * i * length
        return f"{fm}N"
    elif b == '?':
        b = fm / (i * length)
        return f"{b}T"
    elif i == '?':
        i = fm / (b * length)
        return f"{i}A"
    elif length == '?':
        length = fm / (b * i)
        return f"{length}m"
    else:
        return "Invalid input."


def addingParallel(resistors_lst):
    resistors = ''

    for resistor in resistors_lst:
        prl_resistor = '1/' + resistor
        resistors += prl_resistor + '+'

    resistors = resistors[:-1]
    answer = eval(resistors)
    answer = answer ** -1

    return str(answer) + ' ohms.'
