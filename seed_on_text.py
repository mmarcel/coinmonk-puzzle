text = "The faint lines across the lonely expanse make scale hard to determine. As I walk towards the gate, I sling my camera over my shoulder and prepare to enter the old palace. The door pushes open easily and I walk into the courtyard - no adult in sight. I place my camera on the table and get to work searching through the waste. As I dust off an ancient board game, something shiny catches my eye. I reach towards the cupboard and pick up a gold medal. Upon closer inspection, I notice an inscription that seems to resemble a foreign language. I pocket the trinket with the hope that this might make for a good enough payment at the border. Any valuable will do."
palavras = text.split()
print(palavras)
positions = [2,6,9,18,22,25,45,70,86,100,113,116]

for i in positions:
    print(palavras[i-1])