## Exercício proposto

Elabore um algoritmo que possa descobrir, através de perguntas e respostas, em qual área de um restaurante uma pessoa ou grupo de pessoas precisa ser alocada.
O restaurante tem três áreas: térreo, 1ro andar, e área externa.
Clientes fumantes ou com animais de estimação precisam ser alocadas na área externa.
Grupos de 5 ou mais precisam ser alocados no 1º andar, pois não dá para juntar mesas no térreo.
Qualquer outro grupo de pessoas pode ser alocado no térreo. 

Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo.

## Resolução


```

var

maiorQueCinco : logico = false
fumante : logico = false
animal : logico = false
aux : caracter

INICIO

escreva("O cliente esta com algum animal? s-sim n-não"
 leia(aux);

se aux=s
 entao animal = true
fimse

escreva("O cliente é fumante? s-sim n-não");
 leia(aux)

se aux=s
 entao fumante = true
fimse

escreva("Grupo maior que cinco?");
leia(aux)

se aux=s
 entao maiorQueCinco = true
fimse

se fumante = true ou animal = true entao
 escreva("Cliente deve ficar no andar terreo");
senao se maiorQueCinco = true entao
 escreva("Cliente deve ficar no primeiro andar");
senao entao
 escreva("Cliente deve ficar no terreo");
fimse

FIMALGORITMO

```

