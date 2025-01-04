## 1 - Analisar os textos de exemplos
- [x] Verificar os arquivos em ordem em que aparecem e seguindo o tipo de lógica informada - NÃO FUNCIONA
- [x] Verificar os textos de exemplo usando a dica de forma invertida: Exemplo1 com dica do 2 e vice versa. - NÃO FUNCIONA

## 2 - Analisar algum outro texto (sugestões)
- [x] teste1.py: No início do texto existe a palavra **time** destacada, criei o teste1.py para verificar se as palavras do início do texto até esta palavra fazem parte do dicionário. - NÃO FUNCIONA
- [x] Outro teste foi pegar a frase: "The beauty of trithemian seeds is that they hide in plain sight. If you’ve read this far, you’ve read every word required to access a wallet with .03 BTC. Good luck!" e verificar quais palavras fazem parte do dicionário, mas apenas 10 fazem. - NÃO FUNCIONA

- [ ] teste2.py: Além de pegar as frases selecionadas também fas a permutação de todas as palavras informadas, quanto mais palavras maior a demora de processamento. A quantidade de tentativas é o fatoria no número de palavras, ex: 5 plavras será 5!, que é: 5 * 4 * 3 * 2 * 1 = 120. No código tem todas as frases já testadas com alguns ainda não processados por que são muito grandes. - Em validação.

- [ ] teste3.py: Lê o texto puro retirado do site e armazena na ordem em que aparecem todas as palavras que fazem parte do dicionário BIP39 em uma lista.
Em seguida verifica sequencialmente se 12 palavras geram o BIP39 até o final da lista.
Ex: inicia na posição [0,12], em seguida [1,13], em seguida, [2,14], e assim por diante.
OBS: Percebi que existem palavras que fazem parte do dicionário porém estão contraídas, ex: "you've" que representa "you have", o "have" faz parte do dicionário, porém não está sendo inserido/validado por essa contração da lingua inglesa, talvez seja necessário fazer uma mudança nestas palavras. Por isso exitem os arquivos "texto_puro.txt" que não tem alteração e o "texto_editado.txt", que tem essas alterações nas palavras. - Em validação

- [x] example1_pos113: voltando ao exemplo1, onde não é possível gerar o BIP39 por que na posição 113 não existe uma palavra que faz parte do dicionário, criei o example1_pos113.py que testa a substituição da palavra "a" (posição 113) por todas as outras palavras do dicionário. - Não funcionou



## 3 - Analisar as imagens
