# Grunnlegende oppgave for IT-utvikling

1. Formål, bruksområde og ansvarlige

1.1 Hva skal systemet brukes til.

Systemet er ett spill som man bruker til å spille et Pong-style spill. Det er kodet i Python
og tar i bruk PyGame-modulen for å lage systemet. PyGame fungerer slik at du skriver all logikken og data
du skal bruke først og deretter bruker du løkker for å tegne fram og oppdatere systemet. Det blir da en 
konstant løkke som vi manipulerer til å kjøre som ett spil. 

1.2 Hvordan det fungerer.

Systemet fungerer ved at det tar imot input hvor du styrer ett rektangel for å treffe en ball. Du har en
motstander på andre siden som også treffer ballen. Denne motstanderen styres ikke men beveger seg basert 
på om ballen registreres over eller under motstanderen. Når ballen registrer at den treffer en av sidene
vil det bli registrert poeng basert på hvilken side den treffer. Deretter når spilleren velger å avslutte
runden vil poengsummen bli lagret og systemet vil da sjekke om poengsummen du fikk den runden var høyere
enn den tidligere registrerte poengsummen i databasen. Dersom den er høyere enn tidligere registrert sum eller
om det ikke finnes noen tidligere registrert poengsum vil den bli lagret som høyeste poengsum.

1.3 Hvilke andre systemet løsningen jobber med. Inndata og utdata 

Systemet tar i bruk Python og MySQL.

3. Systembeskrivelse

3.1 Versjon

Commit: 7172cb4

3.2	En beskrivelse av grensesnitt mot andre IT-systemer, manuelle eller maskinelle, som angir type, format og
på import- og eksportdata.

Systemet tar importerer data fra MySQL-databasen i form av datatype tuple. Systemet sender ut data som blir
lagret som en interger i MySQL-databasen

3.3	En beskrivelse av IT-systemets oppbygging med programmer, registre, tabeller, database, inndata og utdata, 
metadata, samt avhengigheter og dataflyt mellom disse. Dersom det er en database, bør både den fysiske og
logiske strukturen beskrives. 

Systemet tar imot og sender ut informasjon om spillerens høyeste poengsum. Poengsummen blir lagret som en interger 
og sendes til databasen som blir lagret i en tabell som heter "highscore" med 1 kolonne som heter "score". Denne er 
av type "INT" med egenskapen "NOT NULL" dette er slik at databasen ikke vil bli tilsendt en sum med verdi 0 dersom
spilleren bestemmer seg for å avslutte systemet. Systemet lagrer ikke nye summer i ny rad men oppdaterer
samme rad med ny poengsum. Her er det også viktig å legge merke til at det ikke er satt noe form for PK (PrimaryKey)
fordi vi ikke bruker det i noen sammenheng og trenger derfor ikke å sette det Dette åpner opp for lettere 
videreutvikling dersom vi skal begynne å binde ID'er i systemet eller implementere f.eks scoreboards. 
Siden databasen vil oppdatere hver kolonne åpner det for lettere implementering av f.eks brukersystem

3.4	En beskrivelse av IT-systemets funksjoner med angivelse av hensikt/bruksområde, inndata, behandlingsregler
,innebygd ”arbeidsflyt”, feilmeldinger og utdata. Beskrivelsen omfatter også oppdatering av registre/tabeller. 

Systemet henter inn data først etter at spilleren har avsluttet en runde. Da spilleren trykker ESCAPE vil det kjøre
en funksjon som henter inn spillerens tidligere poengsum og vis den summen spilleren har fått er større vil spilleren
få en ny høyeste poengsum. Dersom systemet ikke finner en tidligere poengsum vil den lagre den nåværende poengsummen 
som høyeste poengsum.

3.5	Programmeringsspråk og versjon. 
Python 3.11 og MySQL 8.0.31


4. Kontroller i og rundt IT-systemet 


4.1	Enkel risikovurdering av IT-systemets konfidensialitet, integritet og tilgjengelighet.

Systemet lagrer ingen form for informasjon om spiller, enhet eller lignende. Det er ingen funskjoner som tar imot inputs
som kan bli gjort om til querry-søk så det er heller ingen muligheten for sql-injections selv i de querry relaterte
funksjonene systemet bruker. Utenom dette er systemet avhengig av PyGame-modulen for at det skal fungere men MySQL-connector kan bli byttet ut med andre database alternativer som f.eks SQLAlchemy vis det skal trenges en ORM. MySQL-connector har ingen andre
dependencies enn Python Standard Library. PyGame derimot er per dags dato (20.12.2022) avhengig av følgende biblioteker:

(>= betyr lik eller nyere versjon)

CPython >= 3.6 eller PyPy3

SDL >= 2.0.0

SDL_mixer >= 2.0.0

SDL_image >= 2.0.0

SDL_ttf >= 2.0.11

NumPy >= 1.6.2 (valgfritt)

5. Driftsmessige krav og ressurser.

5.1 Maskinvare

Minimum kravet for å kunne kjøre systemet: Raspberry Pi 1.

6. Systembenyttende standarer 

6.1 Verktøystandarder (en beskrivelse av regler for hvilke og hvordan verktøy skal brukes når
løsning lages) 

Kodetspråket som brukes er Python. I dette systemet blir Python 3.10.9 brukt. Du kommer også til
å trenge en MySQL-server. I dette systemet blir MySQL-Community Server 8.0.31 brukt. For å få disse til
å kunne kommunisere bruker vi MySQL-connector 8.0.31.  For selve designet av systemet tas PyGame 2.1.2 i bruk.

6.2 Spesifikasjonsstandarder. (En beskrivelse av regler for hvordan funksjoner, programmer, data
og dokumenter skal beskrives.) 

Når kodet skal kommenteres er det viktig å beskrive hva deler av koden gjør. Det vil si at det er viktig at vi
beskriver hver ny deler av kodet, hva den tar inn, hva den returnerer eller hva hensikten med den er. Vis den tar inn
andre deler av koden som er spesifisert ett annet sted er det også viktig å forklare hvorfor den gjør det og hva det brukes
til.

6.3 Brukergrensesnitt. (En beskrivelse av regler for oppbygging av skjermbilde og meny, hva en
kommando utfører, standard betydning av tastene på tastaturet, fellestrekk ved dialogene
etc.)

For oppygning av bildet og meny bruker vi PyGame UI og får å bevege på spilleren bruker vi ARROW_UP, ARROW_DOWN.
Dette vil da bevege på spilleren på Y-aksen opp elller ned. For å navigere til slutt meny'en trykker du ESCAPE som
da vil ta i bruk de funksjonene vi har definert som skal skje når runden er over. Du kan da trykke på SPACE for å 
restarte spillet vis du er på slutt-skjermen.

6.5	Navnestandarder variabler.

Variablene er beskrevet på en forståelig måte som er relatert til det de gjør, som f.eks score_list er en liste
over poengsum. Når du navngir variabler er det viktig å ikke starte med _ de skal heller ikke være bare en bosktav
men heller få de som leser koden din til å fortstå hva den inneholder. Vis du har variabler som forklarer True eller
False eer det også lurt å navngi de etter True-tilstanden. 

Du har tre typer "skriving" som blir brukt mest i koding idag la oss vise eksempel ved å lage en variabel
som heter "variabel en" som vi angir en verdi på 0

Snakecase:
(vært nytt ord er separert med _ )

variabel_en = 0 

Pascalcase:
(vært nytt ord starter med stor forbokstav )

VariabelEn = 0

Camelcase:

(vært nytt ord starter med stor forbokstav UTENOM det første order)

variabelEn = 0

Du kan generelt velge hvilken av dem du vil og det er opp til koderen selv av hva de liker. I dette systemet er det Snakecase
som blir brukt (NB! De skal blandes så lite som mulig alltid prøv å hold de samme navnstanderene til alt gjennom hele prosjektet.)

7. Programdokumentasjon

7.1	Det er viktig med flittig bruk av kommentarer i programkoden for å gjøre denne lettere å forstå. Et minimum er å forklare programmets funksjon, variabler, behandlingsregler og avhengighet av/ påvirkning på andre programmer. 

Koden inneholder kommentarer på engelsk. All kode er også navngitt på engelsk

8. Kjente feil og mangler 

9.1	Oversikt over FAQ og kjente feil og mangler med beskrivelse av mulige løsninger – primært for brukere/brukerstøttefunksjon og driftspersonell. 

