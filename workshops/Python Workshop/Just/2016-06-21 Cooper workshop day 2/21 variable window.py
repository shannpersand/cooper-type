# create small ui element for variables in the script

Variable([
    # create a variable called 'w' 
    # and the related ui is a Slider.
    dict(name="w", ui="Slider"),
    # # create a variable called 'h'
    # # and the related ui is a Slider.
    dict(name="h", ui="Slider", 
            args=dict( 
                # some vanilla specific 
                # setting for a slider
                value=20, 
                minValue=50, 
                maxValue=300,
                tickMarkCount=7,
                stopOnTickMarks=True,
                continuous=False)),
    dict(name="txt", ui="EditText"),

    ], globals())

print h

rect(50, 50, w, h)
font("Curlz MT")
fontSize(200)
text(txt, (40, 200))
