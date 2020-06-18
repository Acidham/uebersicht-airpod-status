command: 'python3 AirPods.widget/bt.py'

refreshFrequency: '2s'

update: (output, domEl) ->
    $(domEl).empty().append("#{output}")

style: """
margin:0
padding: 0px
right: 10px
bottom: 10px
background:rgba(#000, .40)
border:1px solid rgba(#000, .25)
border-radius:10px
color: white
padding: 10px
font-size: 11pt
font-family: Helvetica Neue
width:250px
lineheight: 1.6

img
    height: 32px
    width: 32px
    margin-top: 2px
    float: right

"""
