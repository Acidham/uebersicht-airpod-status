command: 'python3 AirPods.widget/bt.py'

refreshFrequency: '2s'

update: (output, domEl) ->
    $(domEl).empty().append("#{output}")

style: """
margin: 0px
right: 10px
bottom: 10px
background:rgba(#000, .40)
border:1px solid rgba(#000, .25)
border-radius:10px
color: white
padding: 10px
font-size: 11pt
font-family: Helvetica Neue
width: 250px
lineheight: 1.6
text-indent: 15px
white-space: nowrap

.s-box
    display: flex
    align-items:center

.s-txt
    margin-left: 15px
    font-size: 8pt

img
    height: 32px
    width: 32px
    margin-top: 2px
    float: left

.s-img
    height: 20px
    width: 20px

"""
