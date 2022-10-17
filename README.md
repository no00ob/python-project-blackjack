# Python Projekti

Johdatus insinööriopintoihin (INTIP22A6) syksy 2022 Python -projekti

Aki Kanervo 2022

Ohjelmani on yksinkertaistettu blackjack-korttipeli, eli 21 card game -nimisen korttipelin tyylinen peli. Alussa molemmat saavat saman summan rahaa (muokattavissa) ja voivat laittaa siitä osuuden panoksekseen. Pelin alkaessa, voit valita otatko vuorollasi kortin vai et. Pelaat tietokone vastustajan kanssa kunnes molemmat eivät ota korttia vuoroillaan, täten pysäyttäen pelin tai toisen teidän korttien arvo menee yli tavoitteen, joka on tavallisesti 21 (Kuitenkin muokattavissa). Erän päätteeksi voit valita lopetatko pelaamisen vai jatkatko, jos jatkat niin edellisen erän rahat siirtyvät seuraavaan ja voit pelata kunnes toinen teistä häviää kaikki rahansa. Peli toimii kahdella kielellä, suomi tai englanti ja kielestä riippuen kysymysten vastaus vaihtuu. Suomeksi peli etenee kun vastaat 'k', 'kyl', 'kyllä', 'j', 'joo', 'e' tai 'ei' ja englanniksi taas 'y', 'ye', 'yes', 'n' tai 'no'. Jotkut pelin arvoista ovat myös muokattavissa config.json -nimisen tiedoston kautta. "goal"-arvon muokkaaminen tosin saattaa rikkoa tietokonevastustajan.
