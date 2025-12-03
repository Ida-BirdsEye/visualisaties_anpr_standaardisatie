# 3. Functionele eisen

In dit hoofdstuk worden de belangrijkste functionele eisen beschreven die voortkomen uit de informatiebehoefte van gemeenten en de technische randvoorwaarden van de keten. Deze eisen vormen de brug tussen beleidsvragen, visualisaties en het onderliggende datamodel.

## 3.1 Informatiebehoefte van gemeenten

Gemeenten gaven in gesprekken en werksessies aan vooral behoefte te hebben aan:

- **Inzicht in volumes en tijdpatronen**
  - Aantallen voertuigen per uur, dag, maand en jaar.
  - Onderscheid tussen werkdag en weekend.
  - Inzicht in piekmomenten voor logistiek verkeer.

- **Samenstelling van het verkeer**
  - Verdeling naar voertuigcategorie (bestelauto, vrachtauto, personenauto, etc.).
  - Verdeling naar brandstoftype (diesel, benzine, elektrisch, etc.).
  - Verdeling naar emissieklasse, met specifieke aandacht voor de impact van toekomstige aanscherpingen (bijvoorbeeld overgang naar Euro 5 en Euro 6).

- **Herkomst en type gebruikers**
  - Herkomst van voertuigen (bijvoorbeeld op provincie- of NUTS3-niveau).
  - Verdeling naar economische sector (SBI) van de kentekenhouder.
  - Verdeling naar bedrijfsgrootte (micro, klein, middelgroot, groot).
  - Inzicht in bezoekgedrag: eenmalig, incidenteel of dagelijks/structureel.

- **Beleidsrelevante kruisverbanden**
  - SBI ↔ emissieklasse (welke sectoren rijden met welke emissieklassen?).
  - Emissieklasse ↔ voertuigtype en carrosserietype (welke voertuigen zijn schoon/vuil?).
  - SBI ↔ voertuigtype, carrosserietype en brandstoftype.
  - Brandstoftype ↔ emissieklasse en carrosserietype.

Deze inzichten zijn nodig om vragen te kunnen beantwoorden zoals: *Welke doelgroepen worden geraakt door ZE-maatregelen?*, *Welke sectoren veroorzaken de meeste logistieke druk?* en *Hoe ontwikkelt de verschoning van het wagenpark zich in de tijd?*

## 3.2 Eisen aan datavelden en tabellen

Op basis van deze informatiebehoefte is een set van functionele eisen aan de dataset geformuleerd:

- **Minimale datavelden per visualisatie**
  - Voor elke visualisatie is een minimale set velden benoemd (zoals ZoneID, VoertuigType, Emissieklasse, SBI-code, tijdsdimensies).
  - Deze velden moeten in gestandaardiseerde vorm beschikbaar zijn in de CBS-outputtabellen.

- **Afstemming tussen verschillende tabellen**
  - Tabellen moeten via consistente sleutels (zoals ZoneID, periodevelden en categorievelden) met elkaar te koppelen zijn.
  - Bezoekfrequentie-tabellen (eenmalig/incidenteel/structureel) moeten aansluiten op de basisaggregaties per zone en per periode.

- **Ondersteuning van meerdere aggregatieniveaus**
  - Aggregatie op camera- of portallocatie (bijvoorbeeld in-/uitrijdende bewegingen per uur).
  - Aggregatie op zoneniveau (bijvoorbeeld totale instroom per voertuigcategorie).
  - Aggregatie op herkomstregio (bijvoorbeeld provincie, NUTS3).
  - Aggregatie naar sector (SBI) en bedrijfsgrootte.

- **Herbruikbaarheid voor dashboards**
  - Tabellen en velden moeten zodanig zijn opgezet dat ze eenvoudig in bestaande dashboard- en digital twin-omgevingen kunnen worden ingelezen, zonder veel maatwerk per gemeente.

## 3.3 Naming conventions en taal

Binnen de keten bestaan verschillende voorkeuren en praktijken rond naamgeving:

- Digital twin-leveranciers werken bij voorkeur met **camelCase**, terwijl cameraleveranciers velden veelal in **snake_case** aanleveren.
- CBS gebruikt in de outputtabellen doorgaans **Nederlandse veldnamen**, terwijl leveranciers en technische documentatie vaak **Engelstalige namen** hanteren.

Om parsingproblemen, fouten en interpretatieverschillen te voorkomen, wordt aanbevolen:

- één duidelijke **naming convention** af te spreken voor uitwisseling (bijvoorbeeld camelCase in API’s en Nederlandse labels in de gebruikerslaag);
- waar mogelijk te zorgen voor **consistentie in taalgebruik**, zodat het voor alle partijen helder is welke velden op elkaar aansluiten;
- velden als ZoneID, VoertuigType, Emissieklasse, TypeBrandstof en TypeCarrosserie eenduidig te definiëren en gedocumenteerd vast te leggen.

Daarnaast wordt aanbevolen om één **gestandaardiseerde ZoneID** te gebruiken, bij voorkeur een numerieke code die bij de bronhouder (NDW) wordt beheerd. Dit vergemakkelijkt koppelingen tussen datasets en systemen.

## 3.4 Statistische beveiliging en beperkingen

Omdat het CBS verantwoordelijk is voor de statistische beveiliging van de outputtabellen, gelden de volgende functionele randvoorwaarden:

- Tabellen moeten zodanig worden opgezet dat kleine cellen (met lage aantallen) zoveel mogelijk worden voorkomen.
- Waar cellen toch onder de drempel vallen, worden waarden **niet teruggegeven** en verschijnen deze als lege velden in de dataset.
- Vooral bij kruisverbanden tussen meerdere kenmerken (zoals Emissieklasse × VoertuigType × SBI × Carrosserietype) ontstaan snel kleine cellen; daarom zijn deze relaties opgesplitst in meerdere, eenvoudiger tabellen met minder dimensies.

Daarnaast zijn er beperkingen rond:

- de volledigheid en juistheid van venstertijden (gemeenten moeten deze in NDW up-to-date houden; anders wordt teruggevallen op een generieke tijdvakkenindeling);
- de beschikbaarheid van camerastatusgegevens (bij sommige leveranciers alleen maandelijks beschikbaar).

Deze randvoorwaarden zijn meegenomen in de uitwerking van het datamodel en de visualisatievoorbeelden.
