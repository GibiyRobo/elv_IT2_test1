
   # Safe-avstand     (arduino-PRJ)

  * ###### kilder
  * (www.elvebakken.vgs.no/konto) 
  * https://www.arduinolibraries.info/libraries/hcsr04
  * https://create.arduino.cc/projecthub/rowan07/make-a-simple-led-circuit-ce8308
  * (../../../../hcsr04.jpg)
  * (../../../../README.md)
  * (../../Downloads/WhatsApp%20Image%202022-12-07%20at%2012.37.27.jpeg)

## Introduksjon
dette prosjektet tar bruk i majoolet _SR04_ og processor _Arduino uno_. verket kan gi ut beskjed og advare om avstandet til den nærmeste objektet er mindre enn 20 cm. dette gjøres ved hjelp av enkelte og klassikere, nemlig en rød, og en grønn LED. som sagt tar programmet hensikt i _SR04-modellen_ som kan hjelpe å **regn avstand** med å sende en infra-rød stråling og motta det som kommer tilbake fra det samtidig som det holder **tiden** på det. dermed sendes det til arduino programmet som regner ut avstandet med det! deretter tar programmet hensikt i avstandet som ble regnet og avgjører om den er i safe området. 

prosjektet innebærer følgende _elektroniske komponenter_ :
* rød-LED
* grønn-LED
* 2x resistanter 
* SR04
* arduino uno

Vi har følgende filer som inneholder kode
* safe-avstand.ino

### ArduinoCar.ino
Dette programmet har følgende metoder i tillegg til void setup() og void loop()

* float distance_check():
  * Tar ingen argumenter, men returnerer en float-verid for avstandet 
  * sender ut et bølge (infra-rød stråling) og tas imot bølgen
  * bruker paramenterne blant med tid til å regne avstandet

* bibilioteket Servo:
    * brukt til å kommunisere og aktivere SR04

# Slutten 

til slutt så er det programmet og der arduino uno som styrer systemet, hvor koden tar styre over trigger Pin på SR04 og sender bølgen og deretter regner hvormye bølgen har gått fram og tilbake med et tid velocity og strekning forhold og deretter deles det på 2 for å få strekning deretter sjekkes det om den er over safe avstand (f.eks. 20cm) og viser det til brukern med å slå på de grønn og rød LED-ene! koden kjøres veldig fort og gjennom void loop() som gjør at man får den konstant og jevnt! 
