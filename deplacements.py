def tourneGauche(event) :
    "tourner à gauche"
    
    if orientationTete.get() == 0 :
        dx.set(0)
        dy.set(-1)
        orientationTete.set(3)
    elif orientationTete.get() == 1 :
        dx.set(1)
        dy.set(0)
        orientationTete.set(0)
    elif orientationTete.get() == 2 :
        dx.set(0)
        dy.set(1)
        orientationTete.set(1)
    else :
        dx.set(-1)
        dy.set(0)
        orientationTete.set(2)

def tourneDroite(event) :
    "tourner à droite"
    
    if orientationTete.get() == 0 :
        dx.set(0)
        dy.set(1)
        orientationTete.set(1)
    elif orientationTete.get() == 1 :
        dx.set(-1)
        dy.set(0)
        orientationTete.set(2)
    elif orientationTete.get() == 2 :
        dx.set(0)
        dy.set(-1)
        orientationTete.set(3)
    else :
        dx.set(1)
        dy.set(0)
        orientationTete.set(0)