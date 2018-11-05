while True:
    a = float(input("실험값: "))
    b = float(input("이론 값: "))
    error = float((b-a)/b) * 100
    print("%.3f" %error)
