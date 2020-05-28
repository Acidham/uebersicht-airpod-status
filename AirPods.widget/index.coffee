command: 'python /Users/jjung/UebersichtWidgets/AirPods.widget/bt.py'

refreshFrequency: '2s'

update: (output, domEl) ->
    $(domEl).empty().append("#{output}")

style: """
margin:0
padding:0px
right: 10px
bottom: 10px
background:rgba(#000, .40)
border:1px solid rgba(#000, .25)
border-radius:10px
color: white
padding: 10px
font-size: 12pt
font-family: Helvetica Neue
width:240px
lineheight: 1.6

img
    height: 20px
    width: 20px
    margin-bottom: 0px
    float: right

"""
