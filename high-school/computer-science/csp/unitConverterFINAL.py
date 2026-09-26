# Flet is a Graphical User Interface design library that is licensed
# under the Apache 2.0 license. More information can be found at 
# https://flet.dev
# FLET MUST BE INSTALLED FOR THE PROGRAM TO WORK.
# Install Flet using:
# pip install flet
import flet
# The decimal library had to be imported to provide accurate and
# precise calculations.
# Example:
# Without using Decimal: 0.1 + 0.1 + 0.1 returns 0.30000000000000004
# With using Decimal: Decimal("0.1") + Decimal("0.1") + Decimal("0.1") returns Decimal("0.3").
# The values are stored as strings inside Decimal to preserve their precision.
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN, localcontext
# Similar to Decimal, fractions uses Decimal but returns a fractional
# value.
from fractions import Fraction


# This represents the main procedure for the application that is run
# when the application starts
def main(page: flet.Page):
    # Here are variables that configure the basic application (Title,
    # light or dark mode, window height, window width, and padding)
    page.title = "Unit Converter"
    page.theme_mode = 'DARK' # 'DARK' or 'LIGHT'
    page.window_height = 720
    page.window_width = 640
    page.padding = 50

    # This list represents options for the user to choose between.
    # The procedure getUnitNames takes one of these values as input,
    # either Distance or Weight
    inUnits = ["Distance", "Weight"]
    
    # Here other lists are defined for use in storing values of items
    # in dropdown menus.
    possibleUnits = []
    possibleConversions = []

    # This is the standard width of a dropdown menu component, which
    # ensures all text is nicely readable.
    standardWidth = 200

    # This procedure takes the parameter unitType, which is either
    # Distance or Weight, and returns either units for distance or
    # units for weight based on the input parameter
    def getUnitNames(unitType):
        if unitType == "Distance":
            distanceUnits = [
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
                'terameters',
                'inches',
                'feet',
                'miles',
                'lightyears'
            ]
            return distanceUnits
        
        elif unitType == "Weight":
            weightUnits = [
                'picograms',
                'nanograms',
                'milligrams',
                'centigrams',
                'decigrams',
                'grams',
                'decagrams',
                'hectograms',
                'kilograms',
                'tons (metric)',
                'gigagrams',
                'terragrams',
                'pounds',
                'ounces',
                'tons (imperial)'
            ]
            return weightUnits
    
    # This procedure takes the parameter unitType, which is either
    # Distance or Weight, and returns either conversions for distance
    # or conversions for weight based on the input parameter
    # The conversions are based on a base unit which is meters for
    # distance or grams for weight.
    # The conversions for distance represent "how many" of the input
    # unit are in one meter, and the conversions for weight
    # represents "how many" of the input unit are in one gram.
    def getConversions(unitType):
        # if the parameter unitType was Distance
        if unitType == "Distance":
            distanceConversions = [
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
            ]
            return distanceConversions
        
        # if the parameter unitType was Weight
        elif unitType == "Weight":
            weightConversions = [
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
            return weightConversions

    # This procedure is called when the unitTypeDrop dropdown is
    # changed.
    # The parameter e is not used but is required to be passed to a
    # procedure by the Flet GUI library.
    def unitTypeChanged(e):
        # Global variables needed to be used as parameters cannot be
        # passed in procedures that are called when data in a Flet
        # component is changed.
        # Otherwise, procedure parameters would be far better.
        global possibleUnits
        global possibleConversions

        # Get the value of the unitTypeDrop dropdown menu (either
        # Weight or Distance)
        unitType = unitTypeDrop.value
        # Create a possibleUnits list that contains the unit names in
        # the selected unit category
        if unitType == "Distance":
            possibleUnits = getUnitNames("Distance")
        elif unitType == "Weight":
            possibleUnits = getUnitNames("Weight")
        inDrop.options = (
            flet.dropdown.Option(i) for i in possibleUnits
        )
        
        # Create a possibleConversions list that contains the
        # conversions that correspond to the units in possibleUnits
        if unitType == "Distance":
            possibleConversions = getConversions("Distance")
        elif unitType == "Weight":
            possibleConversions = getConversions("Weight")
        outDrop.options = (
            flet.dropdown.Option(i) for i in possibleUnits
        )

        # update the page
        page.update()


    # This procedure is used when converting input to output.
    # The parameter e is not used but is required to be passed to a
    # procedure by the Flet GUI library.
    def convert(e):
        # By default, the Decimal library will round a 5 at the end
        # of a decimal down, which is incorrectly rounded.
        # Thus, to recieve a correct answer, Decimal must round 5 up
        # to 10 instead of to 0.
        getcontext().rounding=ROUND_HALF_UP

        # Global variables needed to be used as parameters cannot be
        # passed in procedures that are called when data in a Flet
        # component is changed.
        # Otherwise, procedure parameters would be far better.
        global possibleUnits
        global possibleConversions
        
        # This part gets the values of all the user inputs. Firstly
        # the input unit from inDrop, next the value of the input
        # unit, and finally the output unit.
        inUnit = inDrop.value
        inputValue = inValue.value
        outUnit = outDrop.value
        
        # Here the appropriate conversions are obtained from the
        # possibleConversions list for both the input and output
        # units.
        # The conversions are selected using the corresponding index
        # of the input and output units in the possibleUnits list.
        # The index of the conversions in the possibleConversions
        # list corresponds with the index of each unit in the
        # possibleUnits list.
        inUnitConversion = possibleConversions[
            possibleUnits.index(inUnit)
        ]
        outUnitConversion = possibleConversions[
            possibleUnits.index(outUnit)
        ]
        
        decInVal = Decimal(str(inputValue))
        decInUnitConv = Decimal(str(inUnitConversion))
        decOutUnitConv = Decimal(str(outUnitConversion))
        # Compute the output value by actually converting the unit.
        outValue = decInVal * (Decimal("1") / decInUnitConv) * decOutUnitConv

        # Find the ratio of the conversion
        fracInVal = Fraction(str(inputValue))
        fracInUnitConv = Fraction(str(inUnitConversion))
        fracOutUnitConv = Fraction(str(outUnitConversion))
        ratio = Fraction(str(fracInVal * 1 / fracInUnitConv * fracOutUnitConv))

        conversionFactor = Fraction(str(Fraction(1) / fracInUnitConv * fracOutUnitConv))
        conversionFactorRatio = Fraction(conversionFactor)
        # Display the output and ratio to the user as a formatted
        # string
        resultLabel.value = f"""{str(inputValue)} {inUnit}
= {str(outValue)} {outUnit}
= {ratio.numerator} / {ratio.denominator} {outUnit} \n
Conversion Factor:
INPUT * (1 / {Decimal(str(inUnitConversion))}) * {Decimal(str(outUnitConversion))}
= INPUT * {conversionFactorRatio.numerator} / {conversionFactorRatio.denominator}"""

        # Update the Graphical User Interface with the new label
        # value for resultLabel
        page.update()

    # This is the dropdown menu that lets the user select the unit
    # type (either Distance or Weight)
    unitTypeDrop = flet.Dropdown(
        label="Unit Type",
        on_change=unitTypeChanged,
        width=standardWidth,
        options=[
            flet.dropdown.Option(i) for i in inUnits
        ]
    )
    # This is the dropdown menu that lets the user select the input
    # unit
    inDrop = flet.Dropdown(
        label="Input Unit",
        #on_change=inChanged,
        width=standardWidth
    )
    # Here the user gives the value of the input
    inValue = flet.TextField(
        label="Input Value",
        width=standardWidth
    )
    # This is the dropdown menu that lets the user select the desired
    # output unit
    outDrop = flet.Dropdown(
        label="Output Unit",
        width=standardWidth
    )
    # This is the button that initiates the conversion
    convertButton = flet.ElevatedButton(
        text="Convert",
        on_click=convert
    )
    # This label displays the conversion output
    resultLabel = flet.Text(
        value="Output will appear here."
    )
    # Here all the UI components are added to the page
    page.add(
        unitTypeDrop,
        inDrop,
        inValue,
        outDrop,
        convertButton,
        resultLabel
    )

# Start the app
flet.app(target=main)
