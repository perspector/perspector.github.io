import flet
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN, localcontext
from fractions import Fraction
#from flet import *

def main(page: flet.Page):
    page.title = "Unit Converter"
    page.theme_mode = 'DARK' # 'DARK' or 'LIGHT'
    page.window_height = 720
    page.window_width = 640
    #page.horizontal_alignment = "top"
    #page.vertical_alignment = "left"
    page.padding = 50
    #page.theme = flet.Theme(use_material3=False)

    allUnitsDict = {
        "distanceUnits": [
            'picometers',
            'nanometers',
            'millimeters',
            'centimeters',
            'decimeters',
            'meters',
            'decameters',
            'hectometers',
            'kilometers',
            'megameters',
            'gigameters',
            'terrameters',
            'inches',
            'feet',
            'miles',
            'lightyears'
        ],
        "distanceConversions": [
            1000000000,
            1000000,
            1000,
            100,
            10,
            1,
            0.1,
            0.01,
            0.001,
            0.000001,
            0.000000001,
            0.000000000001,
            39.37008,
            3.28084,
            0.0006213712,
            0.0000000000000001057004
        ],
        "weightUnits": [
            'picograms',
            'nanograms',
            'milligrams',
            'centigrams',
            'decigrams',
            'grams',
            'decagrams',
            'hectograms',
            'kilograms',
            'ton (metric)',
            'gigagrams',
            'terragrams',
            'pounds',
            'ounces',
            'ton (imperial)'
        ],
        "weightConversions": [
            1000000000,
            1000000,
            1000,
            100,
            10,
            1,
            0.1,
            0.01,
            0.001,
            0.000001,
            0.000000001,
            0.000000000001,
            0.002204623,
            0.03527396,
            1.102311e-6
        ]
    }
    
    possibleUnits = []
    possibleConversions = []

    standardWidth = 200
    def convert(inConversion, inUnit, outConversion, outUnit, inValue):
        getcontext().rounding=ROUND_HALF_UP
        ratio = (Decimal(str(1)) / Decimal(str(inUnitConversion))) * Decimal(str(outUnitConversion))
        outValue = Decimal(str(ratio * Decimal(str(inValue))))
        return ("INPUT * " + ratio), outValue
    def convertButtonClicked(e):
        global possibleUnits
        global possibleConversions
        
        inputValue = inValue.value
        inUnit = inDrop.value
        outUnit = outDrop.value
        
        inUnitConversion = possibleConversions[possibleUnits.index(inUnit)]
        outUnitConversion = possibleConversions[possibleUnits.index(outUnit)]
        #outValue = Decimal(str(inputValue)) * (Decimal(str(1)) / Decimal(str(inUnitConversion))) * Decimal(str(outUnitConversion))
        ratio = Fraction(str(Fraction(str(inputValue)) * 1 / Fraction(str(inUnitConversion)) * Fraction(str(outUnitConversion))))
        conversionFactor = Fraction(str(Fraction(1) / Fraction(str(inUnitConversion)) * Fraction(str(outUnitConversion))))
        conversionFactorRatio = Fraction(conversionFactor)
        resultLabel.value = f"""{str(inputValue)} {inUnit} = {str(outValue)} {outUnit}
= {ratio.numerator} / {ratio.denominator} {outUnit} \n
Conversion Factor:
INPUT * (1 / {Decimal(str(inUnitConversion))}) * {Decimal(str(outUnitConversion))} = {conversionFactorRatio.numerator} / {conversionFactorRatio.denominator}"""
        page.update()
    

    def unitTypeChanged(e):
        global possibleUnits
        global possibleConversions

        unitType = unitTypeDrop.value

        if unitType == "Distance":
            possibleUnits = distanceUnits
            possibleConversions = distanceConversions
        elif unitType == "Weight":
            possibleUnits = weightUnits
            possibleConversions = weightConversions
        
        possibleUnitOptions = (flet.dropdown.Option(i) for i in possibleUnits)
        inDrop.options = possibleUnitOptions
        possibleUnitOptions = (flet.dropdown.Option(i) for i in possibleUnits)
        outDrop.options = possibleUnitOptions
        
        page.update()
        print(possibleUnits)


    def inChanged(e):
        global possibleUnits
        unitInIndex = possibleUnits.index(inDrop.value)


    def outChanged(e):
        pass


    #unitTypeDrop = flet.Dropdown(
    #    label="Unit Type",
    #    on_change=unitTypeChanged,
    #    width=standardWidth,
    #    options=[
    #        flet.dropdown.Option("Distance"),
    #        flet.dropdown.Option("Weight")
    #    ]
    #)

    unitTypeDrop = flet.Dropdown(
        label="Unit Type",
        on_change=lamda unitTypeChanged(unitTypeDrop.value),
        width=standardWidth,
        options=[
            flet.dropdown.Option("Distance"),
            flet.dropdown.Option("Weight")
        ]
    )

    inDrop = flet.Dropdown(
        label="Input Unit",
        on_change=inChanged,
        width=standardWidth
    )

    inValue = flet.TextField(
        label="Input Value",
        width=standardWidth
    )

    outDrop = flet.Dropdown(
        label="Output Unit",
        on_change=outChanged,
        width=standardWidth
    )

    convertButton = flet.ElevatedButton(
        text="Convert",
        on_click=convertButtonClicked
    )

    resultLabel = flet.Text(
        value="Output will appear here."
    )
    
    page.add(flet.Column(
        controls=[
            unitTypeDrop,
            inDrop,
            inValue,
            outDrop,
            convertButton,
            resultLabel
        ],
        alignment=flet.alignment.center
        )
    )
    
flet.app(target=main)
