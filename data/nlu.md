## intent: greet
- Hi
- Hey
- hi
- hey
- Hello
- hello
- Hi Sera
- hi Sera
- Hey Sera
- hey Sera
- Hello Sera
- hello Sera
- Good morning
- Gud morning
- Gud Morning Sera
- Good morning Sera
- hi again
- hi folks
- Howdy
- howdy

## regex:greet
- hey[^\\s]*
- Hey[^\\s]*
- Hi[^\\s]*
- hi[^\\s]*

## intent: goodbye
- goodbye
- goodbye Sera
- bye
- bye Sera
- bye bye
- bye bye Sera
- good night
- good night Sera
- goodnight
- goodnight Sera
- seeya
- see you
- seeya later
- see you later
- farewell
- farewell Sera
- bye take care
- bye tc

## regex: goodbye
- bye[^\\s]*
- Bye[^\\s]*
- Goodbye[^\\s]*
- goodbye[^\\s]*

## intent: fine_normal
- I am doing great
- I'm doing great
- I'm fine
- I'm good

## intent: fine_ask
- I am good, how are you doing?
- I'm fine, how are you?
- I'm good, how are you?

## intent:thanks
- Thanks
- thanks
- thank you
- Thank you
- Thank you so much
- thank you so much
- Thanks a lot
- thanks a lot
- you are a great help
- Wow, Thanks

## regex:thanks
- Thanks[^\\s]*
- thanks[^\\s]*

## intent: inform
- What's the weather today?
- What's the weather in [London](location) today?
- Show me what's the weather in [Paris](location)
- I wonder what is the weather in [New York](location) right now?
- How is the weather at [Barcelona](location:) today?
- I am going to [Berlin](location) today and I wonder what is the weather there?
- I am planning my trip to [Amsterdam](location:). What is the weather out there?
- Show me the weather in [Dublin](location), please
- in [Mumbai](location)
- [Singapore](location)
- Oh, sorry, in [Venice](location)
- Tell me the weather in [Moscow](location)
- The weather condition in [Sydney](location)
- What's the temperature today?
- What's the temperature in [London](location) today?
- Show me what's the weather in [Paris](location)
- I wonder what is the weather in [Vilnius](location) right now?
- How is the weather at [Barcelona](location) today?
- I am going to [Berlin](location) today and I wonder what is the temperature there?
- I am planning my trip to [Amsterdam](location). What is the temperature out there?
- Show me the temperature in [Dublin](location), please
- Temperature in [Mumbai](location)
- Tell me the temperature in [Moscow](location)
