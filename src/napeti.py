from ADCDACPi import ADCDACPi

#####
# Chybí mi tady komentáře
# Rozhodně bych napsal, co to je ADCDACPi, co to dělá a k čemu to používáš
# Jaká je funkce téhle def, kde se to využívá,...
#####

prevodnik = ADCDACPi(2)

def read_voltage():
    return prevodnik.read_adc_voltage(1,0)
